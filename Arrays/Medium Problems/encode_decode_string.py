def encode(input_string):
    result = []
    for char in input_string.split():
        new_char = char + ":;"
        result.append(new_char)

    return "".join(result)


def decode_string(encoded_string):
    result = []
    remove_symbols = [":", ";"]
    for char in encoded_string:
        if char not in remove_symbols:
            result.append(char)
        
  
    return "".join(result)


if __name__ == "__main__":
    input_string = "hello world"
    encoded_string = encode(input_string)
    decoded_string = decode_string(encoded_string)
    print(decoded_string)

    