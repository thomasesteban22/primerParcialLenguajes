#!/usr/bin/awk -f

# Definimos las expresiones regulares para cada token
{
    if ($0 ~ /^\+$/) {
        print "SUMA"
    }
    else if ($0 ~ /^\+\+$/) {
        print "INCR"
    }
    else if ($0 ~ /^[0-9]+$/) {
        print "ENTERO"
    }
    else if ($0 ~ /^[0-9]+\.[0-9]+$/) {
        print "REAL"
    }
    else {
        print "Token no reconocido: " $0
    }
}
