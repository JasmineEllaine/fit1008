.data
	arrayPrompt:	.asciiz	"\nEnter list size: "
	arraySize: 		.word	0
	array: 			.word	0

    index:			.word	0
	elemPrompt: 	.asciiz "Enter element "
	colon: 			.asciiz ": "

    currElem:       .word   0
    currMax:        .word   0
    arrayMax:       .word   0

	bitList:		.word 	0
	bitListSize:	.word	0
    temperature:    .word   0

	appears: 		.asciiz " appears "
	times: 			.asciiz " time(s)\n"

.text
    main:
        li      $v0, 4	 			# prints prompt
        la      $a0, arrayPrompt 
        syscall

        li 	    $v0, 5         		# gets input for size of array
        syscall
        sw	    $v0, arraySize		# stores input in arraySize

        lw      $a0, arraySize      # argument for function call
        jal		buildArray		    # jump to buildArray and save position to $ra

        lw      $a0, arraySize      # argument for function call
        lw      $a1, array
        jal     getMax
        sw      $v1, arrayMax       # store arrayMax

        lw      $s1, arrayMax
        addi    $s1, $s1, 1
        sw      $s1, bitListSize    # get bitListSize

        lw      $a0, bitListSize    # arguments for function call
        lw      $a1, arraySize
        lw      $a2, array
        jal     makeBitList

        lw      $a0, bitListSize
        lw      $a1, bitList
        jal		printBitLoop		# jump to printBitLoop and save position to $ra

    exit: 
        addi	$v0, $0, 10 
        syscall

    buildArray:
        # Args:   $a0 = arraySize
        # Return: None

        # calculating memory to allocate for array
        lw      $a0, arraySize
        addi	$t0, $0, 4			# t0 = 4
        mul  	$a0, $t0, $a0 		# s0 = size * 4

        li	    $v0, 9 				# allocate memory syscall
        syscall

        # initiate array
        sw	    $v0, array			    # store in array the address of first byte allocated

        Loop:
            lw 	    $s0, index 		    # s0 = index
            lw      $a0, arraySize
            bge 	$s0, $a0, endLoop	# if index >= arraySize goto endloop

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

            sw	$v0, ($s2)              # store input in array

            # update index
            addi	$s0, $s0, 1	# add 1 to index
            sw	    $s0, index	

            j Loop

        endLoop:
            jr		$ra					# jump to $ra

    getMax:
        # Args: $a0 = arraySize
        #       $a1 = address of first byte of array
        # Return: $v1 = arrayMax

        # re-initialise index to 0
        maxLoop:
            sw      $0, index       
            lw 	    $s0, index 		    # s0 = index
            lw      $a0, arraySize
            bge 	$s0, $a0, endMaxLoop	# if index >= arraySize goto endloop

            # compute the address to get word
            addi 	$t0, $0, 4 		    # $t0 = 4
            mul 	$t1, $t0, $s0 		# computing (index)*4 to give us the offset AFTER size from the address
                                        #   t1 holds offset in bytes
            add 	$s2, $a1, $t1 		# s2 holds the address of the element to get

            lw      $s3, ($s2)          # currElem = current element
            sw      $s3, currElem      
            lw      $s3, currElem 

            bne	    $0, $s0, findMax	# if not first index, compare to current max/min
            sw	    $s3, currMax		# else set first elem to max

            updateIndex:
                # update index
                addi	$s0, $s0, 1	    # add 1 to index
                sw	    $s0, index	
            j maxLoop

            # conditions for finding maximum and minimum
            findMax:
                lw	$s4, currMax		    # $s4 = current max value
                ble	$s3, $s4, updateIndex	# if currElem <= currMax then findMin
                sw	$s3, currMax		    # else set currMax = currElem
                j updateIndex
        
        endMaxLoop:
            lw      $v1, currMax        # maximum in v1
            jr		$ra					# jump to $ra
            
    makeBitList:
        # Args:   $a0 = bitListSize
        #         $a1 = arraySize
        #         $a2 = array

        # bitList memory allocation
        lw      $a0, bitListSize

        addi	$t0, $0, 4			# t0 = 4
        mul  	$a0, $t0, $a0 		# s0 = size * 4

        li	    $v0, 9 				# allocate memory syscall
        syscall
        
        sw	    $v0, bitList	        # store in bitList the address of first byte allocated

        # re-initialise index
        sw      $0, index

        bitLoop:
            lw 	    $s0, index 		    # s0 = index
            lw      $a1, arraySize
            bge 	$s0, $a1, endBitLoop    # if index >= arraySize goto endloop

            # compute the address to get temperature from array
            lw      $a2, array
            addi 	$t0, $0, 4 		    # t0 = 4
            mul 	$t1, $t0, $s0 		# computing (index)*4 to give us the offset AFTER size from the address
                                        #   t1 = offset in bytes
            add 	$s2, $a2, $t1 		# s2 = address of the current temperature
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
            jr		$ra					# jump to $ra

    printBitLoop:
        # Args:   $a0 = bitListSize
        #         $a1 = bitList

        # re-initialise index
        sw      $0, index

        lw 	    $s0, index          # s0 = index
        bge 	$s0, $a0, endPrintBitLoop      # if index >= bitListSize goto endloop

        # compute the address to get tally
        addi 	$t0, $0, 4 		    # $t0 = 4
        mul 	$t1, $t0, $s0 		# computing (index)*4 to give us the offset AFTER size from the address
                                    #   t1 = offset in bytes
        add 	$s2, $a1, $t1 		# s2 = address of the current tally to print
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

    endPrintBitLoop:
        jr		$ra					# jump to $ra