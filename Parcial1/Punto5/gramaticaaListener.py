# Generated from gramaticaa.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .gramaticaaParser import gramaticaaParser
else:
    from gramaticaaParser import gramaticaaParser

import math


# This class defines a complete listener for a parse tree produced by gramaticaaParser.
class gramaticaaListener(ParseTreeListener):

    # Enter a parse tree produced by gramaticaaParser#file.
    def enterFile(self, ctx:gramaticaaParser.FileContext):
        pass

    # Exit a parse tree produced by gramaticaaParser#file.
    def exitFile(self, ctx:gramaticaaParser.FileContext):
        pass


    # Enter a parse tree produced by gramaticaaParser#expr.
    def enterExpr(self, ctx:gramaticaaParser.ExprContext):
        pass

    # Exit a parse tree produced by gramaticaaParser#expr.
    def exitExpr(self, ctx:gramaticaaParser.ExprContext):
        pass


    # Enter a parse tree produced by gramaticaaParser#trigFunc.
    def enterTrigFunc(self, ctx:gramaticaaParser.TrigFuncContext):
        pass

    # Exit a parse tree produced by gramaticaaParser#trigFunc.
    def exitTrigFunc(self, ctx:gramaticaaParser.TrigFuncContext):
        pass



del gramaticaaParser