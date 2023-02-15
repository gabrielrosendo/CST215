  # check each character in the string
    check_loop:
        # check if the counter is equal to the length of the string
        bne $t3, $t0, check_char

        # if the counter is equal to the length, then break the loop
        j end_check_loop
    
    check_char:
        # load the current character from the string into register $t1
        lb $t1, string($t3)

        # compare the current character with the corresponding character from the end
        lb $t4, string($t0-$t3-1)
        bne $t1, $t4, not_palindrome

        # increment the counter
        addi $t3, $t3, 1

        # repeat the loop
        j check_loop

    not_palindrome:
        # if the characters are not equal, set the result to 0 (false)
        li $t2, 0

        # break the loop
        j end_check_loop

    end_check_loop:
        # store the result into the result label
        sw $t2, result

    # end the program
    li $v0, 10
    syscall
