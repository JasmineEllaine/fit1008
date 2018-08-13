# Task 5
#     Faithful translation of task 1a with functions

.data
    prompt:     .asciiz "Enter a year: "
    isLeap:     .asciiz "Is a leap year"
    isNotLeap:  .asciiz "Is not a leap year"
    year: 	.word 	0

.text
    main: 
        li      $v0, 4          # prints prompt
        la      $a0, prompt
        syscall
        
        li 	    $v0, 5          # gets integer input
        syscall
        sw	    $v0, year       # store input in year

        # prepare to call function isLeapYear
        lw      $a0, year
        jal		isLeapYear		# jump to isLeapYear and save position to $ra
        beq		$v1, $0, printNot	# if false then printNot

        printLeap:
            li      $v0, 4          # prints leap
            la      $a0, isLeap
            syscall
            j exit

        printNot:
            li      $v0, 4          # prints not leap
            la      $a0, isNotLeap
            syscall

    exit:
        li      $v0, 10
        syscall

    isLeapYear:
    # Checks if a given year is a leap year
    # Args:
    #     $a0 (int): year
    # Returns:
    #     $v1: 0 - if leap year
    #          1 - if not leap year
    # Precondition:
    #     No preconditons
    # Complexity:
    #     O(1)
        li      $t0, 100        # div by 100
        div     $a0, $t0
        mfhi    $t1             # t1 = remainder
        bne     $t1, $0, isDivBy4   # jump to 4 if not true

        li      $t0, 400        # div by 400
        div     $a0, $t0        # t1 = rem
        mfhi    $t1
        beq     $t1, $0, returnTrue  # go to printLeap if div by 400
        j returnFalse

    isDivBy4:
        li      $t0, 4          # div by 4
        div     $a0, $t0
        mfhi    $t1
        bne     $t1, $0, returnFalse     

    returnTrue:
        addi    $v1, $0, 1
        jr		$ra					# jump to $ra

    returnFalse:
        addi    $v1, $0, 0
        jr		$ra					# jump to $ra