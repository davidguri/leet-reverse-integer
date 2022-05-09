def check_32_bit(n):
    if n in range(-2 ** 31, (2 ** 31) -1):
        return True
    else:
        return False
    
def split_str(str):
    return [char for char in str]

integer_input = int(input("Input 32-bit number >>> "))

if check_32_bit(integer_input) == True:
    integer_to_str = str(integer_input)
    integer_array = split_str(integer_to_str)
    # print(integer_array)

if integer_array[0] == "-":
    integer_array.pop(0)
    integer_negative = True
    # print(integer_array)
else:
    integer_negative = False

length_of_array = int(len(integer_array))
i = length_of_array
# print("i = " + str(length_of_array))
reversed_array = []
while i > 0:
    highest_len = i - 1
    reversed_array.insert((len(reversed_array) + 1), integer_array[highest_len])
    # print(reversed_array)
    i -= 1

if i == 0 and integer_negative == True:
    reversed_array.insert(0, "-")
    # print(reversed_array)
    
reversed_integer = "".join(reversed_array)
print("Reversed Integer: "+ str(reversed_integer))
