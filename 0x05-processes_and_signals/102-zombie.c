#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
/**
 * infinite_while: runs infinitely
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
 * main: main function
 * Return: 0 (Success)
 */
int main(void)
{
	pid_t child;
	int i;

	for (i = 0; i < 5; i++)
	{
		child = fork();
		if (child > 0)
		{
			printf("Zombie process created, PID: %d\n", child);
			sleep(1);
		}
	}
	infinite_while();
	return (0);
}

