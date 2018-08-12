# Task 2c
#     Faithful translation of task 2b

.data
	arrayPrompt:	.asciiz	"\nEnter list size: "
	arraySize: 		.word	0
	array: 			.word	0
	
	index:			.word	0
	elemPrompt: 		.asciiz "Enter element "
	colon: 			.asciiz ": "
	currElem:  		.word	0
	currMax:		.word 	0

	bitList:		.word 	0
	bitListSize:	.word	0

	appears: 		.asciiz " appears "
	times: 			.asciiz " time(s)\n"
	
.text
	li      $v0, 4	 			# prints prompt
	la      $a0, arrayPrompt 
	syscall

	li 	    $v0, 5         		# gets input for size of array
	syscall
	sw	    $v0, arraySize		# stores input in arraySize

	# memory to allocate = size * 4 + 4
	addi	$s0, $0, 4			# $s0 = 4
	mul  	$t0, $s0, $v0 			# compute size * 4	
	addi 	$s0, $t0, 4			# s0 = size *4 + 4
	
	# $a0 must hold size of memory to allocate
	move 	$a0, $s0			# move $s0 into $a0
	li	$v0, 9 				# allocate memory syscall
	syscall

	# initiate array
	sw	$v0, array			# store in array the address of first byte allocated

	Loop:
		lw 	$s0, index 		# $s0 = index
		lw 	$s1, arraySize 		# $s1 = arraySize
		bge 	$s0, $s1, endLoop	# if index >= arraySize goto endloop

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
		sw	$v0, currElem		# stores input in currElem
		
		lw	$s3, currElem		# gets currElem
		sw	$s3, ($s2)		# stores currElem in array

		# finding max of array
		bne	$0, $s0, findMax	# if not first index, compare to current max/min
		sw	$s3, currMax		# else set first elem to max

		updateIndex:
			# update index
			addi	$s0, $s0, 1	# add 1 to index
			sw	$s0, index	
		j Loop

        # conditions for finding maximum and minimum
        findMax:
            lw	$s4, currMax		# $s4 = current max value
            ble	$s3, $s4, updateIndex	# if currElem <= currMax then findMin
            sw	$s3, currMax		# else set currMax = currElem
            j updateIndex

	endLoop:
    	# start of tallying frequencies
		# re-initialise index
		sw	    $0, index

	# make bitList
	# memory to allocate to bitList = (currMax + 1) * 4 + 4
	addi	$s0, $0, 4			# $s0 = 4
	lw		$t0, currMax		# $t0 = currMax + 1
	sw 		$t0, bitListSize
	lw		$t0, bitListSize
	addi	$t0, $t0, 1
	mul  	$t0, $t0, $s0 			# compute (currMax + 1) * 4	
	addi 	$s0, $t0, 4			# s0 = (currMax * 4) + 4
	
	# $a0 must hold size of memory to allocate
	move 	$a0, $s0			# move $s0 into $a0
	li	$v0, 9 				# allocate memory syscall
	syscall

	# initiate bitList
	sw	$v0, bitList			# store in bitList the address of first byte allocated

	bitLoop:
		lw 	$s0, index 		# $s0 = index
		lw 	$s1, arraySize 		# $s1 = arraySize
		bge 	$s0, $s1, printBitList	# if index >= arraySize goto endloop

		# compute the address to get word
		lw 	$s2, bitList 		# $s2 = the START of the list (where the size)
		addi 	$s2, $s2, 4 		# shift s2 to be talking about the 0th element in array
		
		addi 	$t0, $0, 4 		# $t0 = 4
		mul 	$t1, $t0, $s0 		# computing (index)*4 to give us the offset AFTER size from the address
						# t1 holds offset in bytes
		add 	$s2, $s2, $t1 		# s2 holds the address of the element to get

		lw		$s3, ($s2)		# $s3 = current temp in array
		addi	$s5, $0, 5		# $s5 = 4
		mul		$s4, $s3, $s5	# $s4 = currentTemp * 4 
		add		$s4, $s2, $s4	# $s4 = address of index of bitList to be updated

		lw		$s5, ($s4)		# $s5 = holds current tally
		addi	$s5, $s5, 1		# $s5 = holds updated tally
		sw		$s5, ($s4)		# update bitList tally

		updateIndex:
			# update index
			addi	$s0, $s0, 1	# add 1 to index
			sw	$s0, index	
		j bitLoop

	# prints temperature frequency neatly
	printBitList:









		#print all elements (may succeed with indirect addressing) 
		lw		$t0, 0($t0) 
		li		$v0, 1 		# load system call (print integer) into syscall register 
		move 	$a0, $t0 	# load argument for syscall 
		syscall 			# print element 
















	endPrintBitList

	# exit program
	exit: 
		addi	$v0, $0, 10 
		syscall