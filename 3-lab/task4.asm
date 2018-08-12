.data
	arrayPrompt:	.asciiz	"\nEnter list size: "
	arraySize: 		.word	0
	array: 			.word	0

    index:			.word	0
	elemPrompt: 	.asciiz "Enter element "
	colon: 			.asciiz ": "
	currElem:  		.word	0
	currMax:		.word 	0

	bitList:		.word 	0
	bitListSize:	.word	0
    temperature:    .word   0

	appears: 		.asciiz " appears "
	times: 			.asciiz " time(s)\n"

.text
	li      $v0, 4	 			# prints prompt
	la      $a0, arrayPrompt 
	syscall

    li 	    $v0, 5         		# gets input for size of array
	syscall
	sw	    $v0, arraySize		# stores input in arraySize

    # memory to allocate = size * 4
	addi	$s0, $0, 4			# s0 = 4
	mul  	$s0, $s0, $v0 		# s0 = size * 4
	
	# a0 must hold size of memory to allocate
	move 	$a0, $s0			
	li	    $v0, 9 				# allocate memory syscall
	syscall

    # initiate array
	sw	$v0, array			    # store in array the address of first byte allocated

	Loop:
		lw 	    $s0, index 		    # s0 = index
		lw 	    $s1, arraySize 		# s1 = arraySize
		bge 	$s0, $s1, endLoop	# if index >= arraySize goto endloop

		# compute the address to store word
		lw 	    $s2, array 		    # $s2 = the START of the list
		addi 	$t0, $0, 4 		    # $t0 = 4
		mul 	$t1, $t0, $s0 		# computing (index)*4 to give us the offset AFTER size from the address
						            #   t1 holds offset in bytes
		add 	$s2, $s2, $t1 		# s2 holds the address of the element to store

		# get element to store
		li      $v0, 4          	# prints elemPrompt
		la      $a0, elemPrompt
		syscall

		li	$v0, 1			        # prints index
		lw	$a0, index
		syscall 

		li      $v0, 4          	# prints colon
		la      $a0, colon
		syscall

		li 	$v0, 5          	    # gets input element for current index
		syscall
		sw	$v0, currElem		    # stores input in currElem
		
		lw	$s3, currElem		    # gets currElem
		sw	$s3, ($s2)		        # stores currElem in array

		# finding max of array
		bne	$0, $s0, findMax	    # if not first index, compare to current max/min
		sw	$s3, currMax		    # else set first elem to max

		updateIndex:
			# update index
			addi	$s0, $s0, 1	# add 1 to index
			sw	    $s0, index	
		j Loop

        # conditions for finding maximum and minimum
        findMax:
            lw	$s4, currMax		    # $s4 = current max value
            ble	$s3, $s4, updateIndex	# if currElem <= currMax then findMin
            sw	$s3, currMax		    # else set currMax = currElem
            j updateIndex

	endLoop:

    # bitList mmory allocation
    lw      $s0, currMax
    addi    $s0, $s0, 1         # size of bitList = currMax + 1
    sw      $s0, bitListSize
    lw      $s0, bitListSize    # s0 = size of bitList
    addi	$t0, $0, 4			# t0 = 4
	mul  	$s0, $s0, $t0 		# s0 = size * 4
	
	# a0 must hold size of memory to allocate
	move 	$a0, $s0			
	li	    $v0, 9 				# allocate memory syscall
    syscall

    # initiate bitList
	sw	    $v0, bitList	    # store in bitList the address of first byte allocated

    # re-initialise index
    sw      $0, index

    bitLoop:
		lw 	    $s0, index 		    # s0 = index
		lw 	    $s1, arraySize 		# s1 = arraySize
		bge 	$s0, $s1, endBitLoop    # if index >= arraySize goto endloop

		# compute the address to get temperature from array
		lw 	    $s2, array 		    # s2 = the START of the list
		addi 	$t0, $0, 4 		    # t0 = 4
		mul 	$t1, $t0, $s0 		# computing (index)*4 to give us the offset AFTER size from the address
						            #   t1 = offset in bytes
		add 	$s2, $s2, $t1 		# s2 = address of the current temperature
        lw      $s3, ($s2)          # s3 = current temperature
        sw      $s3, temperature    

        # compute address of bitList tally
    	lw 	    $s2, bitList 		# s2 = the START of the list
		addi 	$t0, $0, 4 		    # t0 = 4

        lw      $s3, temperature    # s3 = current temperature
		mul 	$t1, $t0, $s3 		# computing (currTemp)*4 to give us the offset AFTER size from the address
						            #   t1 = offset in bytes
		add 	$s2, $s2, $t1 		# s2 = address of the bitList index
        lw      $s3, ($s2)          # s3 = current frequency tally for temperature
        addi    $s3, $s3, 1         # cnt += 1
        sw      $s3, ($s2)          

        # update index
        addi	$s0, $s0, 1	# add 1 to index
        sw	    $s0, index	

		j bitLoop

    endBitLoop:

    # re-initialise index
    sw      $0, index

    printBitLoop:
		lw 	    $s0, index          # s0 = index
		lw 	    $s1, bitListSize 	# s1 = bitListSize
		bge 	$s0, $s1, exit      # if index >= bitListSize goto endloop

		# compute the address to get tally
		lw 	    $s2, bitList 		# $s2 = the START of the list
		addi 	$t0, $0, 4 		    # $t0 = 4
		mul 	$t1, $t0, $s0 		# computing (index)*4 to give us the offset AFTER size from the address
						            #   t1 = offset in bytes
		add 	$s2, $s2, $t1 		# s2 = address of the current tally to print
        lw      $s3, ($s2)          # s3 = current tally
        beq		$s3, $0, updateBitIndex     # do not print tally if occurs 0 times
        
        li	    $v0, 1			    # prints index/temperature
		lw	    $a0, index
		syscall 

		li      $v0, 4          	# prints appears
		la      $a0, appears
		syscall

		li	    $v0, 1			    # prints tally
		move 	$a0, $s3
		syscall 

		li      $v0, 4          	# prints times
		la      $a0, times
		syscall

        updateBitIndex:
            addi	$s0, $s0, 1	# add 1 to index
            sw	    $s0, index	

		j printBitLoop

	# exit program
	exit: 
		addi	$v0, $0, 10 
		syscall