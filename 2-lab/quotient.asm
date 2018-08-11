.data 
a:	.word 6
b:	.word 5
succ:	.asciiz "Yes"
nosucc: .asciiz "No"

.text
	lw $t0, a
	lw $t1, b
	
	div $t0, $t1
	mfhi $t2
	
	li $v0, 1
	lw $a0, ($t2)
	syscall
	
	mflo $t3
	li $v0, 1
	lw $a0, ($t3)
	syscall

	addi $v0, $0, 10
	syscall
