section .data
	
	msg db 'Привет ! Начнем! ...', 0xa, 0xd
	len equ $ - msg

section .text
	
	global _start

_start:
	;код вывода строк на экран
	
	;mov цель источник
	
	mov eax, 4   ;номер системного вызова sys_write
	mov ebx, 1   ;файловый дескриптор stdout
	mov ecx, msg ;наша строка
	mov edx, len ;длина строки

	int 0x80
	
	;код для выхода из программы

	mov eax, 1  ;системный вызов sys_exit
	mov ebx, 0  ;код ошибки
	
	int 0x80
	
