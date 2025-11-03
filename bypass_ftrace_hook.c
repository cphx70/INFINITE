#include <unistd.h>
#define _XOPEN_SOURCE 500
#include <stdio.h>
#include <sys/syscall.h>
#include <stdlib.h>
#include <fcntl.h> // Necesaria para open()


int main() {
    int fd = open("/proc/sys/kernel/ftrace_enabled", O_WRONLY); 
    if (fd == NULL) {
        printf("ERROR AL ABRIR");
    }

    pwrite(fd, "0", 1, 0)
    // "0" contenido a escribir
    // 1 <- numero de bytes a escribir
    // 0 <- OFFSET

    close(fd); 
    return 0; 
}