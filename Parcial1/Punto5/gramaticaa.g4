grammar gramaticaa;

@header {
import math
}

file:   (expr NEWLINE?)* EOF;

expr:   trigFunc;

trigFunc
    : 'Sin(' number=NUMBER ')' {print(math.sin(math.radians(int($number.text))))}
    | 'Cos(' number=NUMBER ')' {print(math.cos(math.radians(int($number.text))))}
    | 'Tan(' number=NUMBER ')' {print(math.tan(math.radians(int($number.text))))}
    ;

NUMBER
    : [0-9]+
    ;

NEWLINE
    :   [\r\n]+
    ;

WS  :   [ \t]+ -> skip ;
