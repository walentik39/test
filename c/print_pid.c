#include <stdio.h>
#include <unistd.h>

int main(int argc, char* argv[])
{
	pid_t pid = getpid();  /* print процесса PID */
	pid_t ppid = getppid(); /* print родительского процесса PID */
	printf("%d\n%d\n", pid, ppid);
	return 0;
}
