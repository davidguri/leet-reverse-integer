# remove highest value from first array, append to second array (reverse int)

def check_32_bit(n):
    if n in range(-2 ** 31, (2 ** 31) -1):
        return True
    else:
        return False
# this code makes sure that the inputed integer is 32 bit and not 64.
    
def split_str(str):
    return [char for char in str]
# this code splits the characters of the inputed integer in string form.

integer_input = int(input("input 32-bit number >>> "))
# this has to be an int at first so that it can be checked if 32 bit.

if check_32_bit(integer_input) == True:
    integer_to_str = str(integer_input)
    integer_array = split_str(integer_to_str)
    print(integer_array)

if integer_array[0] == "-":
    integer_array.pop(0)
    integer_negative = True
    print(integer_array)
else:
    integer_negative = False
# this code checks if the inputed integer is negative. It then removes the '-' temporarily. 

length_of_array = int(len(integer_array))
i = length_of_array
print("i = " + str(length_of_array))
while i > 0:
    reversed_array = []
    highest_len = i - 1
    reversed_array.insert(0, integer_array[highest_len])
    print(reversed_array)
    i -= 1
# this code broke. Supposed to remove the elements from the first array into the second

if i == 0 and integer_negative == True:
    reversed_array.insert(0, "-")
    print(reversed_array)
    
reversed_integer = "".join(reversed_array)
print(reversed_integer)