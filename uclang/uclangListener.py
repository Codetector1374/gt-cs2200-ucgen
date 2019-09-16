# Generated from /home/codetector/projects/course/cs2200/mcgen/uclang.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .uclangParser import uclangParser
else:
    from uclangParser import uclangParser

# This class defines a complete listener for a parse tree produced by uclangParser.
class uclangListener(ParseTreeListener):

    # Enter a parse tree produced by uclangParser#ucprog.
    def enterUcprog(self, ctx:uclangParser.UcprogContext):
        pass

    # Exit a parse tree produced by uclangParser#ucprog.
    def exitUcprog(self, ctx:uclangParser.UcprogContext):
        pass


    # Enter a parse tree produced by uclangParser#ucStmt.
    def enterUcStmt(self, ctx:uclangParser.UcStmtContext):
        pass

    # Exit a parse tree produced by uclangParser#ucStmt.
    def exitUcStmt(self, ctx:uclangParser.UcStmtContext):
        pass


    # Enter a parse tree produced by uclangParser#ucSignalStmt.
    def enterUcSignalStmt(self, ctx:uclangParser.UcSignalStmtContext):
        pass

    # Exit a parse tree produced by uclangParser#ucSignalStmt.
    def exitUcSignalStmt(self, ctx:uclangParser.UcSignalStmtContext):
        pass


    # Enter a parse tree produced by uclangParser#ucSequencerStmt.
    def enterUcSequencerStmt(self, ctx:uclangParser.UcSequencerStmtContext):
        pass

    # Exit a parse tree produced by uclangParser#ucSequencerStmt.
    def exitUcSequencerStmt(self, ctx:uclangParser.UcSequencerStmtContext):
        pass


    # Enter a parse tree produced by uclangParser#ucCmpStmt.
    def enterUcCmpStmt(self, ctx:uclangParser.UcCmpStmtContext):
        pass

    # Exit a parse tree produced by uclangParser#ucCmpStmt.
    def exitUcCmpStmt(self, ctx:uclangParser.UcCmpStmtContext):
        pass


    # Enter a parse tree produced by uclangParser#signalList.
    def enterSignalList(self, ctx:uclangParser.SignalListContext):
        pass

    # Exit a parse tree produced by uclangParser#signalList.
    def exitSignalList(self, ctx:uclangParser.SignalListContext):
        pass


    # Enter a parse tree produced by uclangParser#signals.
    def enterSignals(self, ctx:uclangParser.SignalsContext):
        pass

    # Exit a parse tree produced by uclangParser#signals.
    def exitSignals(self, ctx:uclangParser.SignalsContext):
        pass


    # Enter a parse tree produced by uclangParser#signal.
    def enterSignal(self, ctx:uclangParser.SignalContext):
        pass

    # Exit a parse tree produced by uclangParser#signal.
    def exitSignal(self, ctx:uclangParser.SignalContext):
        pass


    # Enter a parse tree produced by uclangParser#number.
    def enterNumber(self, ctx:uclangParser.NumberContext):
        pass

    # Exit a parse tree produced by uclangParser#number.
    def exitNumber(self, ctx:uclangParser.NumberContext):
        pass


    # Enter a parse tree produced by uclangParser#dec_num.
    def enterDec_num(self, ctx:uclangParser.Dec_numContext):
        pass

    # Exit a parse tree produced by uclangParser#dec_num.
    def exitDec_num(self, ctx:uclangParser.Dec_numContext):
        pass


    # Enter a parse tree produced by uclangParser#hex_num.
    def enterHex_num(self, ctx:uclangParser.Hex_numContext):
        pass

    # Exit a parse tree produced by uclangParser#hex_num.
    def exitHex_num(self, ctx:uclangParser.Hex_numContext):
        pass


    # Enter a parse tree produced by uclangParser#bin_num.
    def enterBin_num(self, ctx:uclangParser.Bin_numContext):
        pass

    # Exit a parse tree produced by uclangParser#bin_num.
    def exitBin_num(self, ctx:uclangParser.Bin_numContext):
        pass


