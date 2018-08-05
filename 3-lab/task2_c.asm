.data
        listSize:   .word   0
        array:      .space  0
        index:      .word   0
        inputlist:  .asciiz "/nEnter list size: "
        inputelem:  .asciiz "/nInput elem: "
        rangemsg:   .asciiz "The range of this list (max-min) is: "
.text
        li $v0, 4
        la $a0, inputlist
        syscall                 # prints prompt (inputList)

        # ask for int input (listSize)
        li  $v0, 5         		# get size of array
        syscall



lw      $t0, size
addi    $t1, $0, 4
mult    $t1, $t0
mflo    $t2
add     $a0, $t2, $t1   # $a0 = 4*size + 4
addi    $v0, $0, 9      # $v0 = 9
syscall                 # allocate memory

sw      $v0, the_list   # the_list now points to the returned address
sw      $t0, ($v0)