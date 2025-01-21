#include <stdio.h>
#include <stdlib.h>
#define map_size 10

char map[map_size][map_size];

int main(){
	key input;
	int alive = 1;
	// Initialize starting snake location
	map[map_size/2][map_size/2] = '#'

	while(alive && input != q && input != esc){
		switch input{
			case w || KP_UP:
			
				break
			case a || KP_LEFT:

				break;
			case s || KP_DOWN:

				break;
			case d || KP_RIGHT:

				break;
			default:
				
				break;
		}
	}
}

void display_map(){
	for(int i = 0; i < map_size; i++){
		fprintf(stdout, "%s\n", map[i]);
	}
}
