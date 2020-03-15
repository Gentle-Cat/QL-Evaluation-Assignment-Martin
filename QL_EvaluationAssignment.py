# 1.1
# Function


def function_1_1(input_string):
    new_string = input_string[0]  # First character is always added to the new string
    count = 0
    for index, c in enumerate(input_string[1:]):
        if input_string[index + 1] == input_string[index]:  # Check if previous character is the same as the current
            count += 1
            if count > 2:                   # If count reaches 3 or higher this means we have a -
                continue                    # sequence of 4 or more identical characters. -
        else:                               # (The first character in the sequence doesn't increase count)
            count = 0                   # Reset count if we don't have a sequence of identical characters
        new_string += c

    return new_string


# Test strings

print(function_1_1("ffdttttyy"))
print(function_1_1("iiikigggg"))
print(function_1_1("ggggaipapakfpaorooookokgkappapppapppppppkgkgkkdssöööömmgmmamgkfkkkkkagma"
                   "giangoailkdllkkfkkfkgkfgkaldkfgnkknnnngnnnnnnfkksfjosliiiiidllslkdlk"))


# Followup question, for strings > 20*10^6 :
# As strings in Python are immutable we need to make a new string in the function rather than remove the undesirable
# characters. However, significant amount of copying may lead to inefficiencies, which makes it so that it may be more
# desirable to use a join function in line 15 rather than copying from the original to the new string. Also for
# efficiency reasons, I would try to create an algorithm using as few loops as possible.
# For languages other than Python, where values may be limited by the number of bits, you may encounter issues with
# memory. However I'm not knowledgeable in the types of issues this may cause or how to address them.


# 1.2
# Function


def function_1_2(input_array):
    temp_array = input_array.copy()     # Using a temporary array as to not manipulate the content of the original
    max1 = max(temp_array)              # As the largest odd number from addition will always contain both an even and -
    temp_array.remove(max1)             # an odd number we know that the largest number in the array will be used.
    max2 = max(temp_array)
    temp_array.remove(max2)

    while (max1 + max2) % 2 == 0:       # Check if the largest number and current second largest added is even
        max2 = max(temp_array)          # If not, get a new second largest number
        temp_array.remove(max2)         # Remove the used number from the temporary array
        if len(temp_array) == 0 and (max1 + max2) % 2 == 0:  # Check to see if there is a possible solution in the array
            print("No possible combination of numbers in the array adds to an odd number.")
            return 0

    return max1 + max2


# Test arrays
print(function_1_2([19, 2, 42, 18]))
print(function_1_2([61, 32, 51]))
print(function_1_2([64, 24, 105, 703, 34, 226, 24, 342, 13, 66, 121, 76, 525]))
