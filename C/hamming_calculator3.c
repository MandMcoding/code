#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv){
	if(argc != 3){
		fprintf(stderr, "Please have two values.");
	}

	int a = atoi(argv[1]); int b = atoi(argv[2]);
	int difference = a^b;
	int count = 0;

	while(difference != 0){
		if(difference % 2 == 1) count++;
		difference/=2;
	}

	printf("%d\n", count);

	return 0;
}
