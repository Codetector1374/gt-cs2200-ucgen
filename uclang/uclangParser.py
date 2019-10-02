# Generated from /home/codetector/projects/course/cs2200/mcgen/uclang.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\21")
        buf.write("b\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\3\2\3\2\3\2\7\2 \n\2\f\2\16\2#\13\2\3\3\3\3\3\3\3")
        buf.write("\3\3\3\5\3*\n\3\3\4\3\4\3\4\3\4\5\4\60\n\4\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\b\3\b\3\b\3\b\3\t\5\tI\n\t\3\t\3\t\7\tM\n\t\f")
        buf.write("\t\16\tP\13\t\3\n\3\n\3\n\5\nU\n\n\3\13\3\13\3\13\5\13")
        buf.write("Z\n\13\3\f\3\f\3\r\3\r\3\16\3\16\3\16\2\2\17\2\4\6\b\n")
        buf.write("\f\16\20\22\24\26\30\32\2\2\2_\2\34\3\2\2\2\4)\3\2\2\2")
        buf.write("\6+\3\2\2\2\b\61\3\2\2\2\n\67\3\2\2\2\f=\3\2\2\2\16C\3")
        buf.write("\2\2\2\20H\3\2\2\2\22Q\3\2\2\2\24Y\3\2\2\2\26[\3\2\2\2")
        buf.write("\30]\3\2\2\2\32_\3\2\2\2\34!\5\4\3\2\35\36\7\21\2\2\36")
        buf.write(" \5\4\3\2\37\35\3\2\2\2 #\3\2\2\2!\37\3\2\2\2!\"\3\2\2")
        buf.write("\2\"\3\3\2\2\2#!\3\2\2\2$*\5\6\4\2%*\5\b\5\2&*\5\n\6\2")
        buf.write("\'*\5\f\7\2(*\3\2\2\2)$\3\2\2\2)%\3\2\2\2)&\3\2\2\2)\'")
        buf.write("\3\2\2\2)(\3\2\2\2*\5\3\2\2\2+,\7\f\2\2,-\7\3\2\2-/\5")
        buf.write("\16\b\2.\60\7\f\2\2/.\3\2\2\2/\60\3\2\2\2\60\7\3\2\2\2")
        buf.write("\61\62\7\4\2\2\62\63\7\f\2\2\63\64\7\3\2\2\64\65\5\24")
        buf.write("\13\2\65\66\7\f\2\2\66\t\3\2\2\2\678\7\5\2\289\7\f\2\2")
        buf.write("9:\7\3\2\2:;\5\24\13\2;<\7\f\2\2<\13\3\2\2\2=>\7\6\2\2")
        buf.write(">?\7\f\2\2?@\7\3\2\2@A\5\24\13\2AB\7\f\2\2B\r\3\2\2\2")
        buf.write("CD\7\7\2\2DE\5\20\t\2EF\7\b\2\2F\17\3\2\2\2GI\5\22\n\2")
        buf.write("HG\3\2\2\2HI\3\2\2\2IN\3\2\2\2JK\7\t\2\2KM\5\22\n\2LJ")
        buf.write("\3\2\2\2MP\3\2\2\2NL\3\2\2\2NO\3\2\2\2O\21\3\2\2\2PN\3")
        buf.write("\2\2\2QT\7\f\2\2RS\7\n\2\2SU\5\24\13\2TR\3\2\2\2TU\3\2")
        buf.write("\2\2U\23\3\2\2\2VZ\5\26\f\2WZ\5\30\r\2XZ\5\32\16\2YV\3")
        buf.write("\2\2\2YW\3\2\2\2YX\3\2\2\2Z\25\3\2\2\2[\\\7\r\2\2\\\27")
        buf.write("\3\2\2\2]^\7\16\2\2^\31\3\2\2\2_`\7\17\2\2`\33\3\2\2\2")
        buf.write("\t!)/HNTY")
        return buf.getvalue()


class uclangParser ( Parser ):

    grammarFileName = "uclang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "'@'", "'!'", "'$'", "'['", "']'", 
                     "','", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "COMMENT", "IDENTIFIER", "T_DEC", "T_HEX", 
                      "T_BIN", "WHITESPACE", "NEWLINE" ]

    RULE_ucprog = 0
    RULE_ucStmt = 1
    RULE_ucSignalStmt = 2
    RULE_ucSequencerStmt = 3
    RULE_ucCmpStmt = 4
    RULE_ucIntStmt = 5
    RULE_signalList = 6
    RULE_signals = 7
    RULE_signal = 8
    RULE_number = 9
    RULE_dec_num = 10
    RULE_hex_num = 11
    RULE_bin_num = 12

    ruleNames =  [ "ucprog", "ucStmt", "ucSignalStmt", "ucSequencerStmt", 
                   "ucCmpStmt", "ucIntStmt", "signalList", "signals", "signal", 
                   "number", "dec_num", "hex_num", "bin_num" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    COMMENT=9
    IDENTIFIER=10
    T_DEC=11
    T_HEX=12
    T_BIN=13
    WHITESPACE=14
    NEWLINE=15

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
            self.state = 26
            self.ucStmt()
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==uclangParser.NEWLINE:
                self.state = 27
                self.match(uclangParser.NEWLINE)
                self.state = 28
                self.ucStmt()
                self.state = 33
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


        def ucIntStmt(self):
            return self.getTypedRuleContext(uclangParser.UcIntStmtContext,0)


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
            self.state = 39
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [uclangParser.IDENTIFIER]:
                self.state = 34
                self.ucSignalStmt()
                pass
            elif token in [uclangParser.T__1]:
                self.state = 35
                self.ucSequencerStmt()
                pass
            elif token in [uclangParser.T__2]:
                self.state = 36
                self.ucCmpStmt()
                pass
            elif token in [uclangParser.T__3]:
                self.state = 37
                self.ucIntStmt()
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
            self.state = 41
            self.match(uclangParser.IDENTIFIER)
            self.state = 42
            self.match(uclangParser.T__0)
            self.state = 43
            self.signalList()
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==uclangParser.IDENTIFIER:
                self.state = 44
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
            self.state = 47
            self.match(uclangParser.T__1)
            self.state = 48
            self.match(uclangParser.IDENTIFIER)
            self.state = 49
            self.match(uclangParser.T__0)
            self.state = 50
            self.number()
            self.state = 51
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
            self.state = 53
            self.match(uclangParser.T__2)
            self.state = 54
            self.match(uclangParser.IDENTIFIER)
            self.state = 55
            self.match(uclangParser.T__0)
            self.state = 56
            self.number()
            self.state = 57
            self.match(uclangParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UcIntStmtContext(ParserRuleContext):

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
            return uclangParser.RULE_ucIntStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUcIntStmt" ):
                listener.enterUcIntStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUcIntStmt" ):
                listener.exitUcIntStmt(self)




    def ucIntStmt(self):

        localctx = uclangParser.UcIntStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ucIntStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(uclangParser.T__3)
            self.state = 60
            self.match(uclangParser.IDENTIFIER)
            self.state = 61
            self.match(uclangParser.T__0)
            self.state = 62
            self.number()
            self.state = 63
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
        self.enterRule(localctx, 12, self.RULE_signalList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(uclangParser.T__4)
            self.state = 66
            self.signals()
            self.state = 67
            self.match(uclangParser.T__5)
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
        self.enterRule(localctx, 14, self.RULE_signals)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==uclangParser.IDENTIFIER:
                self.state = 69
                self.signal()


            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==uclangParser.T__6:
                self.state = 72
                self.match(uclangParser.T__6)
                self.state = 73
                self.signal()
                self.state = 78
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
        self.enterRule(localctx, 16, self.RULE_signal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(uclangParser.IDENTIFIER)
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==uclangParser.T__7:
                self.state = 80
                self.match(uclangParser.T__7)
                self.state = 81
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
        self.enterRule(localctx, 18, self.RULE_number)
        try:
            self.state = 87
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [uclangParser.T_DEC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                self.dec_num()
                pass
            elif token in [uclangParser.T_HEX]:
                self.enterOuterAlt(localctx, 2)
                self.state = 85
                self.hex_num()
                pass
            elif token in [uclangParser.T_BIN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 86
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
        self.enterRule(localctx, 20, self.RULE_dec_num)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
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
        self.enterRule(localctx, 22, self.RULE_hex_num)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
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
        self.enterRule(localctx, 24, self.RULE_bin_num)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(uclangParser.T_BIN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





