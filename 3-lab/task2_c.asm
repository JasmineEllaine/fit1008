.data
	arrayPrompt:		.asciiz	"\nEnter list size: "
	arraySize: 		.word	0
	array: 			.word	0
	
	index:			.word	0
	elemPrompt: 		.asciiz "Enter element "
	colon: 			.asciiz ": "
	currElem:  		.word	0
	
	currMax:		.word 	0
	currMin:		.word	0
	range: 			.word	0
	rangePrint:		.asciiz	"The range of this list (max - min) is: "
	
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
	move 	$a0, $t0			# move $s0 into $a0
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

		# finding range of array
		bne	$0, $s0, findMax	# if not first index, compare to current max/min
		sw	$s3, currMax		# else set first elem to max/min
		sw	$s3, currMin

		updateIndex:
			# update index
			addi	$s0, $s0, 1	# add 1 to index
			sw	$s0, index	
		j Loop

	endLoop:
		# calculating range of array
		lw	$s5, currMin
		lw 	$s4, currMax
		sub	$s6, $s4, $s5		# max - min
		sw	$s6, range		# store range

		# printing range of array
		li      $v0, 4          	# prints rangePrint
		la      $a0, rangePrint
		syscall

		li	$v0, 1			# prints range
		lw	$a0, range
		syscall 

		j exit

	# conditions for finding maximum and minimum
	findMax:
		lw	$s4, currMax		# $s4 = current max value
		ble	$s3, $s4, findMin	# if currElem <= currMax then findMin
		sw	$s3, currMax		# else set currMax = currElem

	findMin:
		lw	$s5, currMin		# $s4 = current max value
		bge	$s3, $s5, updateIndex	# if currElem >= currMin then jump back to loop
		sw	$s3, currMin		# else set currMax = currElem
		j updateIndex

	# exit program
	exit: 
		addi	$v0, $0, 10 
		syscall