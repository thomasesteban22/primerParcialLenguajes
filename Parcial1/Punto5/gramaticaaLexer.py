# Generated from gramaticaa.g4 by ANTLR 4.13.1
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
        4,0,7,49,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,
        3,1,3,1,3,1,4,4,4,34,8,4,11,4,12,4,35,1,5,4,5,39,8,5,11,5,12,5,40,
        1,6,4,6,44,8,6,11,6,12,6,45,1,6,1,6,0,0,7,1,1,3,2,5,3,7,4,9,5,11,
        6,13,7,1,0,3,1,0,48,57,2,0,10,10,13,13,2,0,9,9,32,32,51,0,1,1,0,
        0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,
        0,13,1,0,0,0,1,15,1,0,0,0,3,20,1,0,0,0,5,22,1,0,0,0,7,27,1,0,0,0,
        9,33,1,0,0,0,11,38,1,0,0,0,13,43,1,0,0,0,15,16,5,83,0,0,16,17,5,
        105,0,0,17,18,5,110,0,0,18,19,5,40,0,0,19,2,1,0,0,0,20,21,5,41,0,
        0,21,4,1,0,0,0,22,23,5,67,0,0,23,24,5,111,0,0,24,25,5,115,0,0,25,
        26,5,40,0,0,26,6,1,0,0,0,27,28,5,84,0,0,28,29,5,97,0,0,29,30,5,110,
        0,0,30,31,5,40,0,0,31,8,1,0,0,0,32,34,7,0,0,0,33,32,1,0,0,0,34,35,
        1,0,0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,10,1,0,0,0,37,39,7,1,0,0,
        38,37,1,0,0,0,39,40,1,0,0,0,40,38,1,0,0,0,40,41,1,0,0,0,41,12,1,
        0,0,0,42,44,7,2,0,0,43,42,1,0,0,0,44,45,1,0,0,0,45,43,1,0,0,0,45,
        46,1,0,0,0,46,47,1,0,0,0,47,48,6,6,0,0,48,14,1,0,0,0,4,0,35,40,45,
        1,6,0,0
    ]

class gramaticaaLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    NUMBER = 5
    NEWLINE = 6
    WS = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Sin('", "')'", "'Cos('", "'Tan('" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "NEWLINE", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "NUMBER", "NEWLINE", "WS" ]

    grammarFileName = "gramaticaa.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


