# fetch0: [drPC, ] jmp
#
#
#

import argparse
import re

signals = {
    'NextState': 6,
    'DrReg': 1,
    'DrMEM': 1,
    'DrALU': 1,
    'DrPC': 1,
    'DrOFF': 1,
    'LdPC': 1,
    'LdIR': 1,
    'LdMAR': 1,
    'LdA': 1,
    'LdB': 1,
    'LdCmp': 1,
    'WrReg': 1,
    'WrMEM': 1,
    'RegSel': 2,
    'ALU': 2,
    'OPTest': 1,
    'ChkCmp': 1,
}

MainRomSignalValues = {}

MainRomSymbolTable = {}

def computeSignalValueTable():
    currentShift = 0
    for signal in signals:
        MainRomSignalValues[signal] = currentShift
        currentShift += signals[signal]
    print(MainRomSignalValues)
    pass

def parseLine(line, location):
    line = line.replace('\r\n', '').replace('\n','')

    matcher = re.compile(r'^(?P<symbol>[^:\[\] ]+)[ ]*:[ ]*'   # Line Starter Symbol
                         r'(\[(?P<signals>[A-Za-z0-9=, ]*)\])[ ]*'  # Signal Assertion
                         r'(?P<targetSymbol>[^:\[\] ]*)$')  # Redirection Symbol
    result = matcher.search(line)
    print(result.groupdict())

    symbol = result.group('symbol').replace(' ', '')
    if len(symbol) == 0:
        print("ERROR: Line {} no symbol detected".format(location+1))

    MainRomSymbolTable[symbol] = location

    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Python uCGen')
    parser.add_argument("-o", required=True, type=str)

    args = parser.parse_args()

    print('Py_uCGen 9000')
    print(args)

    print('Counting Configured Main Rom Bits...')
    computeSignalValueTable()
    totalBits = 0
    for signal in signals:
        totalBits += signals[signal]
    print('Main ROM is {} bits'.format(totalBits))

    filename = 'demomc.uc'

    print('\n\nParsing file: {}\n'.format(filename))

    with open(filename, 'r') as file:
        location = 0
        line = file.readline()
        while line:
            parseLine(line, location)
            line = file.readline()
            location += 1
        pass
    print(MainRomSymbolTable)
