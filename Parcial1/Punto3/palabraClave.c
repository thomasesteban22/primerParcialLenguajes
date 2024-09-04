#include <stdio.h>
#include <string.h>
#include <regex.h>

int main(int argc, char *argv[]) {
    if (argc != 3) {
        printf("Uso: %s <archivo> <palabra clave>\n", argv[0]);
        return 1;
    }

    char *filename = argv[1];
    char *keyword = argv[2];
    FILE *file = fopen(filename, "r");

    if (file == NULL) {
        printf("No se pudo abrir el archivo %s\n", filename);
        return 1;
    }

    regex_t regex;
    int reti;
    char regex_pattern[256];
    char word[256];
    int count = 0;

    // Crear el patrón de la expresión regular: \bkeyword\b
    snprintf(regex_pattern, sizeof(regex_pattern), "\\b%s\\b", keyword);

    // Compilar la expresión regular
    reti = regcomp(&regex, regex_pattern, REG_EXTENDED | REG_ICASE);
    if (reti) {
        printf("No se pudo compilar la expresión regular\n");
        return 1;
    }

    // Leer el archivo palabra por palabra y buscar coincidencias
    while (fscanf(file, "%255s", word) != EOF) {
        reti = regexec(&regex, word, 0, NULL, 0);
        if (!reti) {
            count++;
        }
    }

    // Liberar la memoria usada por la expresión regular
    regfree(&regex);
    fclose(file);

    printf("La palabra '%s' se repite %d veces en el archivo.\n", keyword, count);

    return 0;
}
