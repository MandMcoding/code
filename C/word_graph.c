#include <stdio.h>
/* Write a program to print a histogram of 
the lengths of words in its input. It is 
easy to draw the histogram with the bars 
horizontal; a vertical orientation is more 
challenging.

Write a program to print a histogram of the 
frequencies of different characters in its input.*/
#define IN   1  /* inside a word */
#define OUT  0  /* outside a word */
int main()
{
    int c, i, state, wordnum, j, q;
    int lengths[20];
    state = wordnum = q = 0;
    for (i = 0; i < 10; ++i)
        lengths[i] = 0;

    while (((c = getchar()) != EOF) && (wordnum < 20)) {
        if (c == ' ' || c == '\n' || c == '\t'){
            state = OUT;
        }
        else if (state == OUT){
            state = IN;
            ++wordnum;
        }

        if(state == IN){
            ++lengths[wordnum];
        }
    }

    int height = 0;
    for(i = 0; i < 20; ++i){
        lengths[i] = lengths[i] / 2;
        if(lengths[i] > height)
            height = lengths[i];
    }
    //Horizontal bars
    // for(j = 0; j < 20; ++j){
    //     for(i = 0; i < lengths[j]; ++i){
    //         putchar('#');
    //     }
    //     putchar('\n');
    // }

    //Vertical bars
    for(j = height; j >= 0; --j){
        for(i = 0; i < 20; ++i){
            if(lengths[i]-j>=0){
                putchar('#');
            }
            else{
                putchar(' ');
            }
        }
        putchar('\n');
    }
}