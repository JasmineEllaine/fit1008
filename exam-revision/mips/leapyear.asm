.data
    prompt:     .asciiz     "Enter a year: "
    year:       .word       0

.text
    main:
        # ask for year input, store in year
        li      $v0, 4
        la      $a0, prompt
        syscall
        li      $v0, 5
        syscall
        sw      $v0, year

        # prepare for function call
        # allocate memory in stack for argument year, and store
        addi    $sp, $sp, -12
        lw      $t0, year
        sw      $t0, 8($sp)
        jal     printMsg

        # end function call
        # clear stack
        addi    $sp, $sp, 12
        j exit

    isLeap:
        # function call prep
        # store $ra, old $fp on stack
        sw      $ra, ($sp)
        sw      $fp, 4($sp)
        # make new $fp == $sp
        add     $fp, $sp, $0
        # allocate space for locals (year)
        addi    $sp, $sp, -8

        # leap year calculation
        # s0 = year
        year100:
            # $t0 = year % 100
            lw      $s0, 8($fp)
            li      $t0, 100
            div     $s0, $t0
            mfhi    $t0
            bne     $t0, $0, year4

        year400:
            # $t0 = year % 400
            li      $t0, 400
            div     $s0, $t0
            mfhi    $t0
            beq     $t0, $0, true
            b       false

        year4:
            # $t0 = year % 4
            li      $t0, 4
            div     $s0, $t0
            mfhi    $t0
            beq     $t0, $0, true
            b       false

        true:
            # store 1 to bool
            li      $t0, 1
            sw      $t0, 4($sp)
            j endIsLeap

        false:
            # store 0 to bool
            li      $t0, 0
            sw      $t0, 4($sp)
            j endIsLeap

        endIsLeap:
            # return value
            lw      $v1, 4($sp)
            # clear local variables
            addi    $sp, $fp, 0
            # restore old $fp
            lw      $fp, 4($sp)
            # restore $ra
            lw      $ra, ($sp)
            jr      $ra

    printMsg:
        

    exit:
        li  $v0, 10
        syscall