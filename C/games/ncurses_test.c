#include <ncurses.h>

int main() {
    int ch;

    // Initialize ncurses
    initscr();
    cbreak();            // Disable line buffering
    noecho();            // Don't echo input to the screen
    keypad(stdscr, TRUE); // Enable special keys like arrow keys
    nodelay(stdscr, TRUE); // Make getch non-blocking

    // Instructions
    printw("Use W/A/S/D or Arrow keys to control. Press 'q' to quit.\n");

    while (1) {
        ch = getch(); // Get keyboard input

        // Switch for handling input
        switch (ch) {
            case 'w' || KEY_UP:
                printw("Moving up!\n");
                break;
            case 'a' || KEY_LEFT:
                printw("Moving left!\n");
                break;
            case 's' || KEY_DOWN:
                printw("Moving down!\n");
                break;
            case 'd' || KEY_RIGHT:
                printw("Moving right!\n");
                break;
            case 'q':
                printw("Quitting game...\n");
                endwin(); // Restore terminal to normal mode
                return 0;
            default:
                // No key pressed or unhandled key
                break;
        }
    }

    endwin(); // Clean up ncurses
    return 0;
}

