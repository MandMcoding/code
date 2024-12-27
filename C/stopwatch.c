#include <stdio.h>
#include <unistd.h> 

int main(){
	printf("Minutes or Sec\n");
	char answer;
	scanf("%c", &answer);

	printf("Time\n");
	int time;
	scanf("%d", &time);

	if(answer == 'm'| answer == 'M') sleep(60*time);
	else sleep(time);

	for(int i = 0; i < 5; i++){
		printf("%c", '\a');
		fflush(stdout);
		usleep(100000);
	}

	return 0;
}
