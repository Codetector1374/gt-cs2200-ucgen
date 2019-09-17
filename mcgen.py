
from typing import List
import argparse
import math
import heapq
from antlr4 import *
from uclang.uclangLexer import uclangLexer
from uclang.uclangParser import uclangParser

AvailableSignals = {
    'nextstate': 6,
    'drreg': 1,
    'drmem': 1,
    'dralu': 1,
    'drpc': 1,
    'droff': 1,
    'ldpc': 1,
    'ldir': 1,
    'ldmar': 1,
    'lda': 1,
    'ldb': 1,
    'ldcmp': 1,
    'wrreg': 1,
    'wrmem': 1,
    'regsel': 2,
    'alu': 2,
    'optest': 1,
    'chkcmp': 1,
}

MainRomSignalValues = {}
MainRomSymbolTable = {}
MainRomEntries = []
MainRomContent = []
SequencerRomContent = []
SequencerRomEntries = []
heapq.heapify(SequencerRomEntries)
CondRomContent =[]
CondRomEntries = []
heapq.heapify(CondRomEntries)

class SequencerEntry:
    def __init__(self, name: str, value: int, target: str):
        self.name = name
        self.value = value
        self.target = target
        pass

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self):
        return "SEQ: (%s)[%01X]: %s" % (self.name, self.value, self.target)


class CondEntry:
    def __init__(self, name: str, value: int, target: str):
        self.name = name
        self.value = value
        self.target = target
        pass

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self):
        return "COND: (%s)[%01X]: %s" % (self.name, self.value, self.target)

class MicrocodeSignal:
    def __init__(self, name, value):
        self.name:str = name
        self.value:int = value
        pass
    def __repr__(self) -> str:
        return self.__str__()
    def __str__(self) -> str:
        return '{%s}->%i' % (self.name, self.value)


class MicrocodeEntry:
    def __init__(self, symbol: str, signals: List[MicrocodeSignal], target: str = None):
        self.symbol = symbol
        self.signals = signals
        self.target = target
        pass

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return '%s: %s ==> %s' % (self.symbol, self.signals, self.target)


def computeSignalValueTable():
    current_shift = 0
    for signal in AvailableSignals:
        MainRomSignalValues[signal] = current_shift
        current_shift += AvailableSignals[signal]
    print(MainRomSignalValues)
    pass


def toText(it: TerminalNode):
    return it.getText()

class uclangListener(ParseTreeListener):

    def __init__(self):
        self.location = 0

    # Exit a parse tree produced by uclangParser#ucSeqencerStmt.
    def exitUcSequencerStmt(self, ctx:uclangParser.UcSequencerStmtContext):
        ids = list(map(toText, ctx.IDENTIFIER()))
        num = ctx.number().numVal
        seqEnt = SequencerEntry(ids[0], num, ids[1])
        heapq.heappush(SequencerRomEntries, (num, seqEnt))
        pass

    # Exit a parse tree produced by uclangParser#ucCmpStmt.
    def exitUcCmpStmt(self, ctx:uclangParser.UcCmpStmtContext):
        ids = list(map(toText, ctx.IDENTIFIER()))
        num = ctx.number().numVal
        condEnt = CondEntry(ids[0], num, ids[1])
        heapq.heappush(CondRomEntries, (num, condEnt))
        pass

    # Exit a parse tree produced by uclangParser#ucSignalStmt.
    def exitUcSignalStmt(self, ctx:uclangParser.UcSignalStmtContext):
        ids = list(map(toText, ctx.IDENTIFIER()))
        signal_list = ctx.signalList().signals().signalObjs
        if len(ids) == 1:
            stmt = MicrocodeEntry(ids[0], signal_list)
        else:
            stmt = MicrocodeEntry(ids[0], signal_list, ids[1])
        ctx.stmt = stmt
        if ids[0] in MainRomSymbolTable:
            print("ERROR: Symbol %s is defined more than once" % ids[0])
            exit(-1)
        MainRomSymbolTable[ids[0]] = self.location
        self.location += 1
        MainRomEntries.append(stmt)
        pass

    # Exit a parse tree produced by uclangParser#signalList.
    def exitSignalList(self, ctx:uclangParser.SignalListContext):
        ctx.signalObjs = ctx.signals().signalObjs
        pass

    # Exit a parse tree produced by uclangParser#signals.
    def exitSignals(self, ctx:uclangParser.SignalsContext):
        signals = ctx.signal()
        signalObjs = []
        for signal in signals:
            if type(signal) == uclangParser.SignalContext:
                signalObjs.append(signal.signalObj)
        ctx.signalObjs = signalObjs
        pass

    # Exit a parse tree produced by uclangParser#signal.
    def exitSignal(self, ctx:uclangParser.SignalContext):
        signalName = ctx.IDENTIFIER().getText()

        value = ctx.number()
        if type(value) == uclangParser.NumberContext:
           num_value = value.numVal
        else:
            num_value = 1
        ctx.signalObj = MicrocodeSignal(signalName, num_value)
        pass

    # Exit a parse tree produced by uclangParser#number.
    def exitNumber(self, ctx:uclangParser.NumberContext):
        ctx.numVal = ctx.children[0].numVal
        pass

    # Exit a parse tree produced by uclangParser#dec_num.
    def exitDec_num(self, ctx:uclangParser.Dec_numContext):
        ctx.numVal = int(ctx.getText())

    # Exit a parse tree produced by uclangParser#hex_num.
    def exitHex_num(self, ctx:uclangParser.Hex_numContext):
        ctx.numVal = eval(ctx.getText())

    # Exit a parse tree produced by uclangParser#bin_num.
    def exitBin_num(self, ctx:uclangParser.Bin_numContext):
        ctx.numVal = eval(ctx.getText())


def validate_signal(signal: MicrocodeSignal) -> bool:
    lowerSignalName = signal.name.lower()
    if lowerSignalName not in AvailableSignals:
        print("\n\nERROR: SIG: %s is not a valid signal" % (signal.name))
        return False
    signalBits = AvailableSignals[lowerSignalName]
    if signal.value >= (1 << signalBits):
        print('\n\nERROR: Value for signal %s (%d) exceeds the max value (%d)' % (signal.name, signal.value, (1 << signalBits) - 1))
        return False
    return True

def process_main_rom_entry(entry: MicrocodeEntry):
    signalList = entry.signals
    entryValue = 0
    if entry.target is not None:
        if entry.target not in MainRomSymbolTable:
            print('Unrecognized symbol reference %s' % (entry.target))
            exit(-1)
        signalList.append(
            MicrocodeSignal('nextstate', MainRomSymbolTable[entry.target])
        )
    for signal in signalList:
        if not validate_signal(signal):
            exit(-1)
        entryValue += signal.value << MainRomSignalValues[signal.name.lower()]
    MainRomContent.append("%07x" % entryValue)


def resolve_sequencer_cond_entry(entry) -> str:
    if entry.target not in MainRomSymbolTable:
        print('Symbol (%s) referenced in Sequencer (%s) is not found in main rom'
              % (entry.target, entry.name))
        exit(-1)
    return '%07x' % MainRomSymbolTable[entry.target]
    pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Python uCGen')
    parser.add_argument("-o", required=True, type=str, metavar='output_prefix')
    parser.add_argument('file', type=str)

    args = parser.parse_args()

    print('Py_uCGen 9000')
    print(args)
    # if args.file

    print('Counting Configured Main Rom Bits...')
    computeSignalValueTable()
    totalBits = 0
    for signal in AvailableSignals:
        totalBits += AvailableSignals[signal]
    outputBits = math.ceil(math.log(1 << totalBits, 16))
    print('Main ROM is {} bits, ({} digits of Hex)'.format(totalBits, outputBits))

    print('==================================')

    filename = args.file
    input = FileStream(filename)
    lexer = uclangLexer(input)
    stream = CommonTokenStream(lexer)
    parser = uclangParser(stream)
    tree = parser.ucprog()  # Parse Root

    listener = uclangListener()
    walker = ParseTreeWalker()

    walker.walk(listener, tree)

    print('MAIN SYMBOL TABLE: ', MainRomSymbolTable)
    print('MAIN Entries: ')
    for entry in MainRomEntries:
        process_main_rom_entry(entry)
        print(entry)

    print('SEQ Entries: ')
    while len(SequencerRomEntries) > 0:
        entry = heapq.heappop(SequencerRomEntries)
        resolvedValue = resolve_sequencer_cond_entry(entry[1])
        while len(SequencerRomContent) < entry[0]:
            SequencerRomContent.append('%07x' % 0)
        if len(SequencerRomContent) != entry[0]:
            print("Something very bad happened")
            exit(-1)
        else:
            SequencerRomContent.append(resolvedValue)
        print(entry[1])
        pass

    print('COND Entries: ')
    while len(CondRomEntries) > 0:
        entry = heapq.heappop(CondRomEntries)
        resolvedValue = resolve_sequencer_cond_entry(entry[1])
        while len(CondRomContent) < entry[0]:
            CondRomContent.append('%07x' % 0)
        if len(CondRomContent) != entry[0]:
            print("Something very bad happened")
            exit(-1)
        else:
            CondRomContent.append(resolvedValue)
        print(entry[1])

    print('===========OUTPUT===============')
    print("MAIN: ", MainRomContent)
    print("SEQ:  ", SequencerRomContent)
    print("COND: ", CondRomContent)
    output = args.o
    with open(('%s_main.dat' % output), 'w') as mainFile:
        mainFile.write(' '.join(MainRomContent))
        mainFile.flush()
    with open(('%s_seq.dat' % output), 'w') as seqFile:
        seqFile.write(' '.join(SequencerRomContent))
        seqFile.flush()
    with open(('%s_cond.dat' % output), 'w') as condFile:
        condFile.write(' '.join(CondRomContent))
        condFile.flush()
