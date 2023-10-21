.file "test3.s"; .data
str: .ascii "test3\n"

.text
.global _start
_start:
/* выводится строка "test3\n" */
movq $1, %rax
movq $1, %rdi
movq $str, %rsi
movq $5, %rdx
syscall

movq $60, %rax
movq $0, %rdi
syscall
