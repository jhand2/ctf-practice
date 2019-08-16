#include <stdio.h>
#include <string.h>

int main() {
    // Symbols gotten from problem with r2
    char *key = "IdontKnowWhatsGoingOn"; // strlen == 21
    char key2[84];

    // Got this by going into gdb and taking every 4th byte
    // at the address for symbol str. These are just bytes written
    // into the image
    char str[21] = {
        8, 6, 44, 58, 50, 48, 28, 92, 1, 50, 26,
        18, 69, 29, 32, 48, 13, 27, 3, 124, 19
    };

    char msg[21];

    for (int i = 0; i <= strlen(key); i++) {
        key2[i*4] = key[i];
        msg[i] = key2[i*4] ^ str[i];
    }

    msg[strlen(key)+1] = '\0';
    puts(msg);

    return 0;
}
