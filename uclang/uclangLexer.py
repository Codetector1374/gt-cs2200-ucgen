# Generated from /home/codetector/projects/course/cs2200/mcgen/uclang.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("Z\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3")
        buf.write("\6\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\t\7\t\62\n\t\f\t\16\t")
        buf.write("\65\13\t\3\t\3\t\3\n\3\n\7\n;\n\n\f\n\16\n>\13\n\3\13")
        buf.write("\6\13A\n\13\r\13\16\13B\3\f\3\f\3\f\3\f\6\fI\n\f\r\f\16")
        buf.write("\fJ\3\r\3\r\3\r\3\r\6\rQ\n\r\r\r\16\rR\3\16\3\16\3\16")
        buf.write("\3\16\3\17\3\17\2\2\20\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\3\2\t\4\2\f\f\17")
        buf.write("\17\5\2C\\aac|\7\2//\62;C\\aac|\3\2\62;\5\2\62;CHch\3")
        buf.write("\2\62\63\4\2\13\13\"\"\2^\2\3\3\2\2\2\2\5\3\2\2\2\2\7")
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2")
        buf.write("\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2")
        buf.write("\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\3\37\3\2\2\2")
        buf.write("\5!\3\2\2\2\7#\3\2\2\2\t%\3\2\2\2\13\'\3\2\2\2\r)\3\2")
        buf.write("\2\2\17+\3\2\2\2\21-\3\2\2\2\238\3\2\2\2\25@\3\2\2\2\27")
        buf.write("D\3\2\2\2\31L\3\2\2\2\33T\3\2\2\2\35X\3\2\2\2\37 \7<\2")
        buf.write("\2 \4\3\2\2\2!\"\7B\2\2\"\6\3\2\2\2#$\7#\2\2$\b\3\2\2")
        buf.write("\2%&\7]\2\2&\n\3\2\2\2\'(\7_\2\2(\f\3\2\2\2)*\7.\2\2*")
        buf.write("\16\3\2\2\2+,\7?\2\2,\20\3\2\2\2-.\7\61\2\2./\7\61\2\2")
        buf.write("/\63\3\2\2\2\60\62\n\2\2\2\61\60\3\2\2\2\62\65\3\2\2\2")
        buf.write("\63\61\3\2\2\2\63\64\3\2\2\2\64\66\3\2\2\2\65\63\3\2\2")
        buf.write("\2\66\67\b\t\2\2\67\22\3\2\2\28<\t\3\2\29;\t\4\2\2:9\3")
        buf.write("\2\2\2;>\3\2\2\2<:\3\2\2\2<=\3\2\2\2=\24\3\2\2\2><\3\2")
        buf.write("\2\2?A\t\5\2\2@?\3\2\2\2AB\3\2\2\2B@\3\2\2\2BC\3\2\2\2")
        buf.write("C\26\3\2\2\2DE\7\62\2\2EF\7z\2\2FH\3\2\2\2GI\t\6\2\2H")
        buf.write("G\3\2\2\2IJ\3\2\2\2JH\3\2\2\2JK\3\2\2\2K\30\3\2\2\2LM")
        buf.write("\7\62\2\2MN\7d\2\2NP\3\2\2\2OQ\t\7\2\2PO\3\2\2\2QR\3\2")
        buf.write("\2\2RP\3\2\2\2RS\3\2\2\2S\32\3\2\2\2TU\t\b\2\2UV\3\2\2")
        buf.write("\2VW\b\16\2\2W\34\3\2\2\2XY\t\2\2\2Y\36\3\2\2\2\b\2\63")
        buf.write("<BJR\3\b\2\2")
        return buf.getvalue()


class uclangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    COMMENT = 8
    IDENTIFIER = 9
    T_DEC = 10
    T_HEX = 11
    T_BIN = 12
    WHITESPACE = 13
    NEWLINE = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':'", "'@'", "'!'", "'['", "']'", "','", "'='" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "IDENTIFIER", "T_DEC", "T_HEX", "T_BIN", "WHITESPACE", 
            "NEWLINE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "COMMENT", "IDENTIFIER", "T_DEC", "T_HEX", "T_BIN", "WHITESPACE", 
                  "NEWLINE" ]

    grammarFileName = "uclang.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


