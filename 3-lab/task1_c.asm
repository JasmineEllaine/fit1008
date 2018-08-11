# Task 1b
#     Faithful translation of task 1 b

.data
    prompt:     .asciiz "Enter a year: "
    isLeap:     .asciiz "Is a leap year"
    isNotLeap:  .asciiz "Is not a leap year"
    year: 	.word 	0
.text
    li      $v0, 4          # prints prompt
    la      $a0, prompt
    syscall
    
    li 	    $v0, 5          # gets integer input
    syscall
    sw	    $v0, year
    lw      $s0, year

    li      $t0, 100        # div by 100
    div     $s0, $t0
    mfhi    $t1             # t1 = remainder
    bne     $t1, $0, isDivBy4   # jump to 4 if not true

    li      $t0, 400        # div by 400
    div     $s0, $t0        # t1 = rem
    mfhi    $t1
    beq     $t1, $0, printLeap  # go to printLeap if div by 400
    j printNot

isDivBy4:
    li      $t0, 4          # div by 4
    div     $s0, $t0
    mfhi    $t1
    bne     $t1, $0, printNot     

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