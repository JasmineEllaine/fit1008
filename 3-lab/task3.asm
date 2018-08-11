# Task 3b
#     Faithful translation of task 3a

.data
	arrayPrompt:		.asciiz	"\nEnter size: "
	arraySize: 		.word	0
	array: 			.word	0
	
	index:			.word	0
	elemPrompt: 		.asciiz "Enter element "
	colon: 			.asciiz ": "
	
	compTempPrompt:		.asciiz	"\nComparison temperature: "
	compTemp: 		.word	0
	count:			.word 	0
	indext:			.word 	0
	
	tempPrint1:		.asciiz "\nTemperature was exceeded "
	tempPrint2:		.asciiz " time(s)"
.text
    	li      $v0, 4	 			# prints prompt
    	la      $a0, arrayPrompt 
    	syscall

    	li	$v0, 5         			# gets input for size of array
    	syscall
    	sw	$v0, arraySize			# stores input in arraySize

	# memory to allocate = size * 4 + 4
	addi	$s0, $0, 4			# $s0 = 4
	mul  	$t0, $s0, $v0 			# compute size * 4	
	addi 	$s0, $t0, 4			# s0 = size *4 + 4
	
	# $a0 must hold size of memory to allocate
	move 	$a0, $t0			# move $s0 into $a0
	li	$v0, 9 				# allocate memory syscall
	syscall

	# initiate array
	sw	$v0, array			# store in array the address of first byte allocated

	makeArrayLoop:
		lw 	$s0, index 		# $s0 = index
		lw 	$s1, arraySize 		# $s1 = arraySize
		bge 	$s0, $s1, getCompTemp	# if index >= arraySize goto endloop

		# compute the address to store word
		lw 	$s2, array 		# $s2 = the START of the list (where the size)
		addi 	$s2, $s2, 4 		# shift s2 to be talking about the 0th element in array
		
		addi 	$t0, $0, 4 		# $t0 = 4
		mul 	$t1, $t0, $s0 		# computing (index)*4 to give us the offset AFTER size from the address
						# t1 holds offset in bytes
		add 	$s2, $s2, $t1 		# s2 holds the address of the element to store

		# get element to store
		li      $v0, 4          	# prints elemPrompt
		la      $a0, elemPrompt
		syscall

		li	$v0, 1			# prints index
		lw	$a0, index
		syscall 

		li      $v0, 4          	# prints colon
		la      $a0, colon
		syscall

		li 	$v0, 5          	# gets input element for current index
		syscall
		sw	$v0, ($s2)		# stores input element in array

		updateIndex:
			addi	$s0, $s0, 1	# add 1 to index
			sw	$s0, index	
		j makeArrayLoop
		
	getCompTemp:
    		li      $v0, 4	 		# prints prompt
    		la      $a0, compTempPrompt 
    		syscall

    		li	$v0, 5         		# gets input for size of array
		syscall
    		sw	$v0, compTemp		

	compTemptoArrayLoop:
		lw 	$s0, indext		# $s0 = index
		lw 	$s1, arraySize 		# $s1 = arraySize
		bge 	$s0, $s1, temperaturePrint	# if index >= arraySize goto endloop

		# compute the address of element to check
		lw 	$s2, array 		# $s2 = the START of the list (where the size)
		addi 	$s2, $s2, 4 		# shift s2 to be talking about the 0th element in array
		
		addi 	$t0, $0, 4 		# $t0 = 4
		mul 	$t1, $t0, $s0 		# computing (index)*4 to give us the offset AFTER size from the address
						# t1 = offset in bytes
		add 	$s2, $s2, $t1 		# s2 = the address of the current element
		
		# get current element and comparison temp
		lw	$s3, ($s2)		# s3 = current element
		lw	$s4, compTemp		# s4 = comparison element
		
		# increase tally if greater than comp temp
		ble 	$s3, $s4, updateTempIndex	# if currElem <= compTemp updateIndex
		
		updateCount:			# else update count
			lw	$s5, count	# s5 = count
			addi	$s5, $s5, 1	# add 1 to count
			sw	$s5, count	# update count

		updateTempIndex:
			addi	$s0, $s0, 1	# add 1 to index
			sw	$s0, indext	
		j compTemptoArrayLoop

	temperaturePrint:
		li      $v0, 4          	# prints tempPrint1
		la      $a0, tempPrint1
		syscall

		li	$v0, 1			# prints count
		lw	$a0, count
		syscall 

		li      $v0, 4          	# printst tempPrint2
		la      $a0, tempPrint2
		syscall
	
	exit: 
		addi	$v0, $0, 10 
		syscall