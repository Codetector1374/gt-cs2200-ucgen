# Generated from /home/codetector/projects/course/cs2200/mcgen/uclang.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("Y\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2\3\2")
        buf.write("\3\2\7\2\36\n\2\f\2\16\2!\13\2\3\3\3\3\3\3\3\3\5\3\'\n")
        buf.write("\3\3\4\3\4\3\4\3\4\5\4-\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\b\5\b@\n\b\3")
        buf.write("\b\3\b\7\bD\n\b\f\b\16\bG\13\b\3\t\3\t\3\t\5\tL\n\t\3")
        buf.write("\n\3\n\3\n\5\nQ\n\n\3\13\3\13\3\f\3\f\3\r\3\r\3\r\2\2")
        buf.write("\16\2\4\6\b\n\f\16\20\22\24\26\30\2\2\2V\2\32\3\2\2\2")
        buf.write("\4&\3\2\2\2\6(\3\2\2\2\b.\3\2\2\2\n\64\3\2\2\2\f:\3\2")
        buf.write("\2\2\16?\3\2\2\2\20H\3\2\2\2\22P\3\2\2\2\24R\3\2\2\2\26")
        buf.write("T\3\2\2\2\30V\3\2\2\2\32\37\5\4\3\2\33\34\7\20\2\2\34")
        buf.write("\36\5\4\3\2\35\33\3\2\2\2\36!\3\2\2\2\37\35\3\2\2\2\37")
        buf.write(" \3\2\2\2 \3\3\2\2\2!\37\3\2\2\2\"\'\5\6\4\2#\'\5\b\5")
        buf.write("\2$\'\5\n\6\2%\'\3\2\2\2&\"\3\2\2\2&#\3\2\2\2&$\3\2\2")
        buf.write("\2&%\3\2\2\2\'\5\3\2\2\2()\7\13\2\2)*\7\3\2\2*,\5\f\7")
        buf.write("\2+-\7\13\2\2,+\3\2\2\2,-\3\2\2\2-\7\3\2\2\2./\7\4\2\2")
        buf.write("/\60\7\13\2\2\60\61\7\3\2\2\61\62\5\22\n\2\62\63\7\13")
        buf.write("\2\2\63\t\3\2\2\2\64\65\7\5\2\2\65\66\7\13\2\2\66\67\7")
        buf.write("\3\2\2\678\5\22\n\289\7\13\2\29\13\3\2\2\2:;\7\6\2\2;")
        buf.write("<\5\16\b\2<=\7\7\2\2=\r\3\2\2\2>@\5\20\t\2?>\3\2\2\2?")
        buf.write("@\3\2\2\2@E\3\2\2\2AB\7\b\2\2BD\5\20\t\2CA\3\2\2\2DG\3")
        buf.write("\2\2\2EC\3\2\2\2EF\3\2\2\2F\17\3\2\2\2GE\3\2\2\2HK\7\13")
        buf.write("\2\2IJ\7\t\2\2JL\5\22\n\2KI\3\2\2\2KL\3\2\2\2L\21\3\2")
        buf.write("\2\2MQ\5\24\13\2NQ\5\26\f\2OQ\5\30\r\2PM\3\2\2\2PN\3\2")
        buf.write("\2\2PO\3\2\2\2Q\23\3\2\2\2RS\7\f\2\2S\25\3\2\2\2TU\7\r")
        buf.write("\2\2U\27\3\2\2\2VW\7\16\2\2W\31\3\2\2\2\t\37&,?EKP")
        return buf.getvalue()


class uclangParser ( Parser ):

    grammarFileName = "uclang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "'@'", "'!'", "'['", "']'", "','", 
                     "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "COMMENT", "IDENTIFIER", "T_DEC", "T_HEX", "T_BIN", 
                      "WHITESPACE", "NEWLINE" ]

    RULE_ucprog = 0
    RULE_ucStmt = 1
    RULE_ucSignalStmt = 2
    RULE_ucSequencerStmt = 3
    RULE_ucCmpStmt = 4
    RULE_signalList = 5
    RULE_signals = 6
    RULE_signal = 7
    RULE_number = 8
    RULE_dec_num = 9
    RULE_hex_num = 10
    RULE_bin_num = 11

    ruleNames =  [ "ucprog", "ucStmt", "ucSignalStmt", "ucSequencerStmt", 
                   "ucCmpStmt", "signalList", "signals", "signal", "number", 
                   "dec_num", "hex_num", "bin_num" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    COMMENT=8
    IDENTIFIER=9
    T_DEC=10
    T_HEX=11
    T_BIN=12
    WHITESPACE=13
    NEWLINE=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class UcprogContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ucStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(uclangParser.UcStmtContext)
            else:
                return self.getTypedRuleContext(uclangParser.UcStmtContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(uclangParser.NEWLINE)
            else:
                return self.getToken(uclangParser.NEWLINE, i)

        def getRuleIndex(self):
            return uclangParser.RULE_ucprog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUcprog" ):
                listener.enterUcprog(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUcprog" ):
                listener.exitUcprog(self)




    def ucprog(self):

        localctx = uclangParser.UcprogContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_ucprog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.ucStmt()
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==uclangParser.NEWLINE:
                self.state = 25
                self.match(uclangParser.NEWLINE)
                self.state = 26
                self.ucStmt()
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UcStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ucSignalStmt(self):
            return self.getTypedRuleContext(uclangParser.UcSignalStmtContext,0)


        def ucSequencerStmt(self):
            return self.getTypedRuleContext(uclangParser.UcSequencerStmtContext,0)


        def ucCmpStmt(self):
            return self.getTypedRuleContext(uclangParser.UcCmpStmtContext,0)


        def getRuleIndex(self):
            return uclangParser.RULE_ucStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUcStmt" ):
                listener.enterUcStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUcStmt" ):
                listener.exitUcStmt(self)




    def ucStmt(self):

        localctx = uclangParser.UcStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_ucStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [uclangParser.IDENTIFIER]:
                self.state = 32
                self.ucSignalStmt()
                pass
            elif token in [uclangParser.T__1]:
                self.state = 33
                self.ucSequencerStmt()
                pass
            elif token in [uclangParser.T__2]:
                self.state = 34
                self.ucCmpStmt()
                pass
            elif token in [uclangParser.EOF, uclangParser.NEWLINE]:
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UcSignalStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(uclangParser.IDENTIFIER)
            else:
                return self.getToken(uclangParser.IDENTIFIER, i)

        def signalList(self):
            return self.getTypedRuleContext(uclangParser.SignalListContext,0)


        def getRuleIndex(self):
            return uclangParser.RULE_ucSignalStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUcSignalStmt" ):
                listener.enterUcSignalStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUcSignalStmt" ):
                listener.exitUcSignalStmt(self)




    def ucSignalStmt(self):

        localctx = uclangParser.UcSignalStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_ucSignalStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(uclangParser.IDENTIFIER)
            self.state = 39
            self.match(uclangParser.T__0)
            self.state = 40
            self.signalList()
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==uclangParser.IDENTIFIER:
                self.state = 41
                self.match(uclangParser.IDENTIFIER)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UcSequencerStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(uclangParser.IDENTIFIER)
            else:
                return self.getToken(uclangParser.IDENTIFIER, i)

        def number(self):
            return self.getTypedRuleContext(uclangParser.NumberContext,0)


        def getRuleIndex(self):
            return uclangParser.RULE_ucSequencerStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUcSequencerStmt" ):
                listener.enterUcSequencerStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUcSequencerStmt" ):
                listener.exitUcSequencerStmt(self)




    def ucSequencerStmt(self):

        localctx = uclangParser.UcSequencerStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_ucSequencerStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(uclangParser.T__1)
            self.state = 45
            self.match(uclangParser.IDENTIFIER)
            self.state = 46
            self.match(uclangParser.T__0)
            self.state = 47
            self.number()
            self.state = 48
            self.match(uclangParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UcCmpStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(uclangParser.IDENTIFIER)
            else:
                return self.getToken(uclangParser.IDENTIFIER, i)

        def number(self):
            return self.getTypedRuleContext(uclangParser.NumberContext,0)


        def getRuleIndex(self):
            return uclangParser.RULE_ucCmpStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUcCmpStmt" ):
                listener.enterUcCmpStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUcCmpStmt" ):
                listener.exitUcCmpStmt(self)




    def ucCmpStmt(self):

        localctx = uclangParser.UcCmpStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ucCmpStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(uclangParser.T__2)
            self.state = 51
            self.match(uclangParser.IDENTIFIER)
            self.state = 52
            self.match(uclangParser.T__0)
            self.state = 53
            self.number()
            self.state = 54
            self.match(uclangParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SignalListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def signals(self):
            return self.getTypedRuleContext(uclangParser.SignalsContext,0)


        def getRuleIndex(self):
            return uclangParser.RULE_signalList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSignalList" ):
                listener.enterSignalList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSignalList" ):
                listener.exitSignalList(self)




    def signalList(self):

        localctx = uclangParser.SignalListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_signalList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(uclangParser.T__3)
            self.state = 57
            self.signals()
            self.state = 58
            self.match(uclangParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SignalsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def signal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(uclangParser.SignalContext)
            else:
                return self.getTypedRuleContext(uclangParser.SignalContext,i)


        def getRuleIndex(self):
            return uclangParser.RULE_signals

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSignals" ):
                listener.enterSignals(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSignals" ):
                listener.exitSignals(self)




    def signals(self):

        localctx = uclangParser.SignalsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_signals)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==uclangParser.IDENTIFIER:
                self.state = 60
                self.signal()


            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==uclangParser.T__5:
                self.state = 63
                self.match(uclangParser.T__5)
                self.state = 64
                self.signal()
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SignalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(uclangParser.IDENTIFIER, 0)

        def number(self):
            return self.getTypedRuleContext(uclangParser.NumberContext,0)


        def getRuleIndex(self):
            return uclangParser.RULE_signal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSignal" ):
                listener.enterSignal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSignal" ):
                listener.exitSignal(self)




    def signal(self):

        localctx = uclangParser.SignalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_signal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(uclangParser.IDENTIFIER)
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==uclangParser.T__6:
                self.state = 71
                self.match(uclangParser.T__6)
                self.state = 72
                self.number()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dec_num(self):
            return self.getTypedRuleContext(uclangParser.Dec_numContext,0)


        def hex_num(self):
            return self.getTypedRuleContext(uclangParser.Hex_numContext,0)


        def bin_num(self):
            return self.getTypedRuleContext(uclangParser.Bin_numContext,0)


        def getRuleIndex(self):
            return uclangParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = uclangParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_number)
        try:
            self.state = 78
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [uclangParser.T_DEC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self.dec_num()
                pass
            elif token in [uclangParser.T_HEX]:
                self.enterOuterAlt(localctx, 2)
                self.state = 76
                self.hex_num()
                pass
            elif token in [uclangParser.T_BIN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 77
                self.bin_num()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dec_numContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def T_DEC(self):
            return self.getToken(uclangParser.T_DEC, 0)

        def getRuleIndex(self):
            return uclangParser.RULE_dec_num

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDec_num" ):
                listener.enterDec_num(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDec_num" ):
                listener.exitDec_num(self)




    def dec_num(self):

        localctx = uclangParser.Dec_numContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_dec_num)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(uclangParser.T_DEC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Hex_numContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def T_HEX(self):
            return self.getToken(uclangParser.T_HEX, 0)

        def getRuleIndex(self):
            return uclangParser.RULE_hex_num

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHex_num" ):
                listener.enterHex_num(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHex_num" ):
                listener.exitHex_num(self)




    def hex_num(self):

        localctx = uclangParser.Hex_numContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_hex_num)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(uclangParser.T_HEX)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bin_numContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def T_BIN(self):
            return self.getToken(uclangParser.T_BIN, 0)

        def getRuleIndex(self):
            return uclangParser.RULE_bin_num

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBin_num" ):
                listener.enterBin_num(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBin_num" ):
                listener.exitBin_num(self)




    def bin_num(self):

        localctx = uclangParser.Bin_numContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_bin_num)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(uclangParser.T_BIN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





