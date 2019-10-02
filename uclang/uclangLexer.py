# Generated from /home/codetector/projects/course/cs2200/mcgen/uclang.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\21")
        buf.write("^\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\3\3\3\3\4\3\4\3\5")
        buf.write("\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\n\7")
        buf.write("\n\66\n\n\f\n\16\n9\13\n\3\n\3\n\3\13\3\13\7\13?\n\13")
        buf.write("\f\13\16\13B\13\13\3\f\6\fE\n\f\r\f\16\fF\3\r\3\r\3\r")
        buf.write("\3\r\6\rM\n\r\r\r\16\rN\3\16\3\16\3\16\3\16\6\16U\n\16")
        buf.write("\r\16\16\16V\3\17\3\17\3\17\3\17\3\20\3\20\2\2\21\3\3")
        buf.write("\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21\3\2\t\4\2\f\f\17\17\5\2C\\aac|\7\2")
        buf.write("//\62;C\\aac|\3\2\62;\5\2\62;CHch\3\2\62\63\4\2\13\13")
        buf.write("\"\"\2b\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2")
        buf.write("\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\3!\3\2\2\2\5#\3")
        buf.write("\2\2\2\7%\3\2\2\2\t\'\3\2\2\2\13)\3\2\2\2\r+\3\2\2\2\17")
        buf.write("-\3\2\2\2\21/\3\2\2\2\23\61\3\2\2\2\25<\3\2\2\2\27D\3")
        buf.write("\2\2\2\31H\3\2\2\2\33P\3\2\2\2\35X\3\2\2\2\37\\\3\2\2")
        buf.write("\2!\"\7<\2\2\"\4\3\2\2\2#$\7B\2\2$\6\3\2\2\2%&\7#\2\2")
        buf.write("&\b\3\2\2\2\'(\7&\2\2(\n\3\2\2\2)*\7]\2\2*\f\3\2\2\2+")
        buf.write(",\7_\2\2,\16\3\2\2\2-.\7.\2\2.\20\3\2\2\2/\60\7?\2\2\60")
        buf.write("\22\3\2\2\2\61\62\7\61\2\2\62\63\7\61\2\2\63\67\3\2\2")
        buf.write("\2\64\66\n\2\2\2\65\64\3\2\2\2\669\3\2\2\2\67\65\3\2\2")
        buf.write("\2\678\3\2\2\28:\3\2\2\29\67\3\2\2\2:;\b\n\2\2;\24\3\2")
        buf.write("\2\2<@\t\3\2\2=?\t\4\2\2>=\3\2\2\2?B\3\2\2\2@>\3\2\2\2")
        buf.write("@A\3\2\2\2A\26\3\2\2\2B@\3\2\2\2CE\t\5\2\2DC\3\2\2\2E")
        buf.write("F\3\2\2\2FD\3\2\2\2FG\3\2\2\2G\30\3\2\2\2HI\7\62\2\2I")
        buf.write("J\7z\2\2JL\3\2\2\2KM\t\6\2\2LK\3\2\2\2MN\3\2\2\2NL\3\2")
        buf.write("\2\2NO\3\2\2\2O\32\3\2\2\2PQ\7\62\2\2QR\7d\2\2RT\3\2\2")
        buf.write("\2SU\t\7\2\2TS\3\2\2\2UV\3\2\2\2VT\3\2\2\2VW\3\2\2\2W")
        buf.write("\34\3\2\2\2XY\t\b\2\2YZ\3\2\2\2Z[\b\17\2\2[\36\3\2\2\2")
        buf.write("\\]\t\2\2\2] \3\2\2\2\b\2\67@FNV\3\b\2\2")
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
    T__7 = 8
    COMMENT = 9
    IDENTIFIER = 10
    T_DEC = 11
    T_HEX = 12
    T_BIN = 13
    WHITESPACE = 14
    NEWLINE = 15

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':'", "'@'", "'!'", "'$'", "'['", "']'", "','", "'='" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "IDENTIFIER", "T_DEC", "T_HEX", "T_BIN", "WHITESPACE", 
            "NEWLINE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "COMMENT", "IDENTIFIER", "T_DEC", "T_HEX", "T_BIN", 
                  "WHITESPACE", "NEWLINE" ]

    grammarFileName = "uclang.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


