#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

/**
 * infinite_while - puts the program to sleep indefinitely
 *
 * Returni: 0 for success
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - main function to create 5 zombie processes
 *
 * Return: 0 for success
 */
int main(void)
{
	pid_t zombie_pid[5];

	for (int i = 0; i < 5; i++)
	{
		zombie_pid[i] = fork();
		if (zombie_pid[i] == 0)
		{
			exit(0);
		}
		else if (zombie_pid[i] < 0)
		{
			printf("Fork error!\n");
			exit(1);
		}
		else
		{
			printf("Zombie process created, PID: %d\n", zombie_pid[i]);
		}
	}
	for (int i = 0; i < 5; i++)
	{
		wait(NULL);
	}
	infinite_while();
	return (0);
}

