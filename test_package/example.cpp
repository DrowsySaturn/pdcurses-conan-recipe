#include <curses.h>

int main(int argc, char **argv)
{
	initscr();
	printw("Hello!");
	refresh();
	endwin();
	return 0;
}
