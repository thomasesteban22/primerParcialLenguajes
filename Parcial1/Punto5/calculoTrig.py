import sys
from antlr4 import *
from gramaticaaLexer import gramaticaaLexer
from gramaticaaParser import gramaticaaParser

def main():
    # Leer el archivo de entrada
    input_stream = FileStream('input.txt')

    # Crear el lexer y parser
    lexer = gramaticaaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = gramaticaaParser(stream)

    # Parsear la entrada y ejecutar la gramática
    tree = parser.file_()  # Nota el cambio aquí de 'file' a 'file_'

if __name__ == '__main__':
    main()
