.data 
a:	.word 6
b:	.word 5
succ:	.asciiz "Yes"
nosucc: .asciiz "No"

.text
	# load variables containing ints
	lw $t0, a
	lw $t1, b
	
	# divides variables in registers
	div $t0, $t1
	mfhi $t2
	
	# if statement
	beq $t2, $0, ifDivis
	j ifNot
	 
	# condition if divisble
	ifDivis:
	la	$a0, succ
	addi	$v0, $0, 4
	syscall
	j exit
	
	# condition if not divisible
	ifNot:
	la	$a0, nosucc
	addi	$v0, $0, 4
	syscall
	j exit
	
	# exit
	exit:
	addi $v0, $0, 10
	syscall