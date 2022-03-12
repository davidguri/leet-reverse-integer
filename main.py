
# input 32-bit number
# check if number 32-bit
# turn number to string
# check if negative
# remove highest value from first array, append to second array (reverse int)

def check_32_bit(n):
    if n in range(-2 ** 31, (2 ** 31) -1):
        return True
    else:
        return False
    
def split_str(str):
    return [char for char in str]

integer_input = int(input("input 32-bit number >>> "))
if check_32_bit(integer_input) == True:
    integer_to_str = str(integer_input)
    integer_array = split_str(integer_to_str)
    print(integer_array)

if integer_array[0] == "-":
    integer_array.pop(0)
    print(integer_array)
else:
    pass

length_of_array = int(len(integer_array))
i = length_of_array
while i > 0:
    reversed_array = []
    highest_len = i-1
    reversed_array.append(integer_array[highest_len])
    i -= 1
    #this code broke

print(reversed_array)

