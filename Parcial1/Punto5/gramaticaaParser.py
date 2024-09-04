# Generated from gramaticaa.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


import math

def serializedATN():
    return [
        4,1,7,34,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,3,0,9,8,0,5,0,11,8,0,10,
        0,12,0,14,9,0,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,3,2,32,8,2,1,2,0,0,3,0,2,4,0,0,34,0,12,1,0,0,0,2,17,
        1,0,0,0,4,31,1,0,0,0,6,8,3,2,1,0,7,9,5,6,0,0,8,7,1,0,0,0,8,9,1,0,
        0,0,9,11,1,0,0,0,10,6,1,0,0,0,11,14,1,0,0,0,12,10,1,0,0,0,12,13,
        1,0,0,0,13,15,1,0,0,0,14,12,1,0,0,0,15,16,5,0,0,1,16,1,1,0,0,0,17,
        18,3,4,2,0,18,3,1,0,0,0,19,20,5,1,0,0,20,21,5,5,0,0,21,22,5,2,0,
        0,22,32,6,2,-1,0,23,24,5,3,0,0,24,25,5,5,0,0,25,26,5,2,0,0,26,32,
        6,2,-1,0,27,28,5,4,0,0,28,29,5,5,0,0,29,30,5,2,0,0,30,32,6,2,-1,
        0,31,19,1,0,0,0,31,23,1,0,0,0,31,27,1,0,0,0,32,5,1,0,0,0,3,8,12,
        31
    ]

class gramaticaaParser ( Parser ):

    grammarFileName = "gramaticaa.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Sin('", "')'", "'Cos('", "'Tan('" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NUMBER", "NEWLINE", "WS" ]

    RULE_file = 0
    RULE_expr = 1
    RULE_trigFunc = 2

    ruleNames =  [ "file", "expr", "trigFunc" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    NUMBER=5
    NEWLINE=6
    WS=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class FileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(gramaticaaParser.EOF, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaaParser.ExprContext)
            else:
                return self.getTypedRuleContext(gramaticaaParser.ExprContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaaParser.NEWLINE)
            else:
                return self.getToken(gramaticaaParser.NEWLINE, i)

        def getRuleIndex(self):
            return gramaticaaParser.RULE_file

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFile" ):
                listener.enterFile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFile" ):
                listener.exitFile(self)




    def file_(self):

        localctx = gramaticaaParser.FileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_file)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 26) != 0):
                self.state = 6
                self.expr()
                self.state = 8
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==6:
                    self.state = 7
                    self.match(gramaticaaParser.NEWLINE)


                self.state = 14
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 15
            self.match(gramaticaaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def trigFunc(self):
            return self.getTypedRuleContext(gramaticaaParser.TrigFuncContext,0)


        def getRuleIndex(self):
            return gramaticaaParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = gramaticaaParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.trigFunc()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TrigFuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.number = None # Token

        def NUMBER(self):
            return self.getToken(gramaticaaParser.NUMBER, 0)

        def getRuleIndex(self):
            return gramaticaaParser.RULE_trigFunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrigFunc" ):
                listener.enterTrigFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrigFunc" ):
                listener.exitTrigFunc(self)




    def trigFunc(self):

        localctx = gramaticaaParser.TrigFuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_trigFunc)
        try:
            self.state = 31
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                self.match(gramaticaaParser.T__0)
                self.state = 20
                localctx.number = self.match(gramaticaaParser.NUMBER)
                self.state = 21
                self.match(gramaticaaParser.T__1)
                print(math.sin(math.radians(int((None if localctx.number is None else localctx.number.text)))))
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 23
                self.match(gramaticaaParser.T__2)
                self.state = 24
                localctx.number = self.match(gramaticaaParser.NUMBER)
                self.state = 25
                self.match(gramaticaaParser.T__1)
                print(math.cos(math.radians(int((None if localctx.number is None else localctx.number.text)))))
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 27
                self.match(gramaticaaParser.T__3)
                self.state = 28
                localctx.number = self.match(gramaticaaParser.NUMBER)
                self.state = 29
                self.match(gramaticaaParser.T__1)
                print(math.tan(math.radians(int((None if localctx.number is None else localctx.number.text)))))
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





