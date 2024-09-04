%{
#include <stdio.h>
%}

%%

"lambda"            { printf("ACEPTA\n"); }
[a-zA-Z_][a-zA-Z0-9_]*    { /* Identificador, variable */ }
"="                 { /* Asignación */ }
"**"                { /* Operador de potencia */ }
"("                 { /* Paréntesis izquierdo */ }
")"                 { /* Paréntesis derecho */ }
"[0-9]+"            { /* Números enteros */ }
[ \t\n]+            { /* Espacios en blanco */ }
.                   { /* Cualquier otro carácter */ }

%%

int main(int argc, char **argv)
{
    if (argc > 1) {
        FILE *input = fopen(argv[1], "r");
        if (!input) {
            perror(argv[1]);
            return 1;
        }
        yyin = input;
        yylex();
        fclose(input);
    } else {
        yylex();
    }
    return 0;
}

int yywrap() {
    return 1;
}
