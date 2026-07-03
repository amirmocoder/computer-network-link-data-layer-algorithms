# simulation of bit stuffing on a binary string as data link layer data framing method on sender machine side
# framing flag is `01111110`

# using bit_stuffing method prevents to creation a substring in string that look like flag's binary pattern thats why on receiver sides de-framing frames is correctly available

# in string converts every `11111` substrings to `111110`
def bit_stuffing(string):
    result = ""
    counter = 0

    for i in string:
        result += i

        if i == "1":
            counter += 1

            if counter == 5:
                result += "0"
                counter = 0
        else:
            counter = 0

    return result


# simulation of bit stuffing on a binary string as data link layer data framing method on receiver machine side
# in string converts every `111110` substrings to `11111`
# bit destuffing on receiver side is required ot recovery true and main stuffed data
def bit_destuffing(string):
    result = ""
    counter = 0
    i = 0

    while i < len(string):
        bit = string[i]
        result += bit

        if bit == "1":
            counter += 1

            if counter == 5:
                if i + 1 < len(string) and string[i + 1] == "0":
                    i += 1 # skips bit `0` value to write on result
                counter = 0
        else:
            counter = 0

        i += 1

    return result


# get input from user
data = input("Enter a binary string with maximum 100 bits: ")

# check that input maximum has 100 bits
if len(data) > 100:
    print("Error: Input size must be less than 101 bits.")

# check that input is a binary string value
elif not all(bit in "01" for bit in data):
    print("Error: Input must contain only 0 and 1.")

else:
    stuffed_data = bit_stuffing(data)
    destuffed_data = bit_destuffing(stuffed_data)

    print("Original data:     ", data)
    print("Bit stuffed data:  ", stuffed_data)
    print("Bit destuffed data:", destuffed_data)

    if data == destuffed_data:
        print("Data recovery was successful.")
    else:
        print("Data recovery failed.")