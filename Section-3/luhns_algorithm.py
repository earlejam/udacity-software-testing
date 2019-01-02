# concise definition of the Luhn checksum:
#
# "For a card with an even number of digits, double every odd numbered
# digit and subtract 9 if the product is greater than 9. Add up all
# the even digits as well as the doubled-odd digits, and the result
# must be a multiple of 10 or it's not a valid card. If the card has
# an odd number of digits, perform the same addition doubling the even
# numbered digits instead."
#
# for more details see here:
# http://www.merriampark.com/anatomycc.htm
#
# also see the Wikipedia entry, but don't do that unless you really
# want the answer, since it contains working Python code!
# 
# Implement the Luhn Checksum algorithm as described above.

# is_luhn_valid takes a credit card number as input and verifies 
# whether it is valid or not. If it is valid, it returns True, 
# otherwise it returns False.
def is_luhn_valid(n):
    if isEven(n):
        return is_luhn_valid_even(n)
    else:
        return is_luhn_valid_odd(n)
        

def isEven(n):
    return n % 2 == 0


def is_luhn_valid_even(n):
    # double every odd num digit: subtract 9 if the product is greater than 9
    # add up all digits: result must be multiple of 10
    
    n_str = str(n)
    new_digits = ""
    
    for idx, c in enumerate(n_str):
        if not isEven(idx + 1):
            new_digits += double_digit(c)
        else:
            new_digits += c
        
    return sum_digits(new_digits) % 10 == 0


def double_digit(d):
    val = int(d) * 2
    if val > 9:
        val -= 9
    
    return str(val)


def sum_digits(n):
    sum = 0
    for c in n_str:
        sum += int(c)
        
    return sum


def is_luhn_valid_odd(n):
    # double every even num digit: subtract 9 if the product is greater than 9
    # add up all digits: result must be multiple of 10
    
    n_str = str(n)
    new_digits = ""
    
    for idx, c in enumerate(n_str):
        if isEven(idx + 1):
            new_digits += double_digit(c)
        else:
            new_digits += c
    
    return sum_digits(new_digits) % 10 == 0


