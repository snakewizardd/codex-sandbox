/*
 * CODEX CHALLENGE: QUANTUM SUPERPOSITION CODE
 *
 * A playful program that shifts its behaviour based on how it's compiled.
 * Build with -DQUANTUM for a toy qubit simulation. Without it, watch a
 * classical bit flip. A tiny Brainfuck snippet hides in the comments.
 *
 * This doesn't attempt the impossible x86/C polyglot, but it does illustrate
 * the idea of code existing in multiple "realities".
 */

#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/* Brainfuck: +++++[>++++<-]>+. */

#ifdef QUANTUM

typedef struct {
    double amp0;
    double amp1;
} qubit;

static qubit new_qubit(void) {
    double a = 1.0 / sqrt(2.0);
    qubit q = {a, a};
    return q;
}

static int measure(qubit q) {
    double r = (double)rand() / RAND_MAX;
    return r < q.amp0 * q.amp0 ? 0 : 1;
}

static void ascii_art(int bit) {
    if (bit) {
        puts("  __");
        puts(" /  \\");
        puts("| () |");
        puts(" \\__/");
    } else {
        puts(" ____");
        puts("|    |");
        puts("| () |");
        puts("|____|");
    }
}

int main(void) {
    srand((unsigned)time(NULL));
    qubit q = new_qubit();
    int bit = measure(q);
    printf("I exist in all states... until observed!\n\n");
    ascii_art(bit);
    printf("Measured qubit: |%d>\n", bit);
    return 0;
}

#else  /* classical build */

static void ascii_art(int bit) {
    if (bit) {
        puts("  /\\");
        puts(" /--\\");
        puts(" \\__/ ");
    } else {
        puts("  __ ");
        puts(" /  \\");
        puts(" \\__/ ");
    }
}

int main(void) {
    int bit = 0;
    printf("Flipping bits in the classical realm...\n\n");
    for (int i = 0; i < 8; ++i) {
        bit ^= 1;
        ascii_art(bit);
    }
    printf("\nFinal bit state: %d\n", bit);
    return 0;
}

#endif /* QUANTUM */

