.data
    prompt:     .asciiz     "Enter two numbers: "
    a_val:      .word       0
    b_val:      .word       0
    q_val:      .float       0
    r_val:      .word       0
    quot:       .asciiz     "\nQuotient is "
    remain:     .asciiz     "\nRemainder is "

.text
    # print input prompt
    li  $v0, 4
    la  $a0, prompt
    syscall

    # ask for integer input
    li  $v0, 5
    syscall
    # move input to variable a
    sw  $v0, a_val

    # repeat for variable b
    li  $v0, 5
    syscall
    # move input to variable a
    sw  $v0, b_val

    # store a_val in $t0, b_val in $t1
    lw  $t0, a_val
    lw  $t1, b_val
    # calc q, r and store in q_val, r_val
    div     $t2, $t0, $t1
    #mflo    $t2
    sw      $t2, q_val
    mfhi    $t2
    sw      $t2, r_val

    # print quotient
    li  $v0, 4
    la  $a0, quot
    syscall
    li  $v0, 1
    lw  $a0, q_val
    syscall

    # print remainder
    li  $v0, 4
    la  $a0, remain
    syscall
    li  $v0, 1
    lw  $a0, r_val
    syscall

    # exit
    li  $v0, 10
    syscall \