listSize = int(input("Enter list size: "))
array = [0]*listSize
index = 0
while index < listSize:
    msg = "Enter element " + str(index) + ": "
    array[index] = int(input(msg))
    index += 1
print("The range of this list (max-min) is", max(array)-min(array))


"""

.data
the_list: .word 0
num: .word 1


.text

# $a0 must hold size * 4 + 4
addi $t2, $0, 5
addi $t3, $0, 4
mult $t3, $t2 #compute 5*4
mflo $t4 #t4 = 5*4
addi $t4, $t4, 4 #t4 = 5*4 + 4

#getting the right amount to allocate
add $a0, $t4, $0 #a0 holds the value of t4 + 0
addi $v0, $0, 9 #allocate memory syscall
syscall
#initiate list
sw $v0, the_list
addi $t2, $0, 5 #the size
lw $t6, the_list
sw $t2, ($t6)

Loop:
	lw $t0, num #get num
	addi $t1, $0, 5 #get the 5
	addi $t1, $t1, 1 #get 5+1
	bge $t0, $t1, endLoop #where num >= (5+1) goto endloop

	lw $t6, num
	addi $t6, $t6, -1 #t6 = num-1
	
	#compute the address
	lw $t7, the_list #the START of the list (where the size)
	addi $t7, $t7, 4 #shift t7 to be talking about the 0th element in the_list
	
	addi $t1, $0, 4 #get 4
	mult $t1,$t6 #computing (num-1)*4 to give us the offset AFTER size from the address
	mflo $t1 #t1 holds offset in bytes
	add $t7, $t7, $t1 #t7 holds the address of the element to store

	lw $t5, num
	mult $t5, $t5
	mflo $t5 #t5 = num*num

	sw $t5, ($t7)

	lw $t0, num #reget num
	addi $t0, $t0, 1 #$t0 = num + 1
	sw $t0, num #num = num + 1
	j Loop

endLoop:
	addi $v0, $0, 10 #halt syscall
	syscall
"""