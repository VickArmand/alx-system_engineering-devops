#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
/**
 * infinite_while - runs infinitely
 * Return: 0 (Success)
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
 * main - creates 5 zombie processes
 * Return: 0 (Success)
 */
int main(void)
{
	pid_t child;
	int i;

	while (i < 5)
	{
		child = fork();
		if (child > 0)
		{
			printf("Zombie process created, PID: %d\n", child);
			sleep(1);
			i++;
		}
		else
			exit(0);
	}
	infinite_while();
	return (0);
}

