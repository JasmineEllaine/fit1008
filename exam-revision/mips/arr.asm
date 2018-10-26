.data

.text
    

    buildArray:
    # ArguementStack:
    #     # must be allocated before
    #     size =  8($fp): size of the array 
    #     # must be set in this function
    #     oldfp = 4($fp): old frame prointer
    #     ra =    0($fp): return address
    # Registers:
    #     newfp = after the above values
    # LocalStack:
    #     none
    # Returns:
    #     $v1 = array
    
    # $t0 = size
    lw      $t0, ($sp)
    # save oldfp and ra
    addi    $sp, $sp, -8
    sw      $fp, 4($sp)
    sw      $ra, ($sp)
    add     $fp, $sp, $0

    # calculate space needed for array = size*4 + 4
    # $t1 = size needed for array
    li      $t1, 4
    mult    $t0, $t1
    mflo    $t1
    addi    $t1, $t1, 4
    # allocate space for array
    move    $a0, $t1
    li      $v0, 9 
    syscall

    # set length as first item of array
    sw      $t0, $v0

    # set return value
    # $v1 = address of first byte allocated
    move    $v0, $v1

    # restore fp, ra
    lw      $fp, 4($sp)
    lw      $ra, ($sp)
    # destroy local stack
    addi    $sp, $sp, -8
    
    jr $ra