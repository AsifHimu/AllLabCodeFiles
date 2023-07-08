#encoding
def encode_lzw(data):
    dictionary = {chr(i): i for i in range(256)}
    current_string = data[0]
    next_code = 256
    encoded_data = []
    
    for symbol in data[1:]:
        if(current_string + symbol) in dictionary:
            current_string = current_string + symbol
        else:
            encoded_data.append(dictionary[current_string])
            dictionary[current_string + symbol] = next_code
            next_code+=1
            current_string = symbol
            
    encoded_data.append(dictionary[current_string])
    return encoded_data

def decode_lzw(data):
    dictionary = {i: chr(i) for i in range(256)}
    next_code = 256
    current_code = data[0]
    decoded_data = dictionary[current_code]
    previous_string = decoded_data
    
    for code in data[1:]:
        if code in dictionary:
            current_string = dictionary[code]
        else:
            current_string = previous_string + previous_string[0]
        
        decoded_data += current_string
        dictionary[next_code] = previous_string + current_string[0]
        next_code += 1
        previous_string = current_string
        
    return decoded_data

def main():
    with open("input.txt","r") as input_file:
        data = input_file.read().strip()
    
    encoded_data = encode_lzw(data)
    with open("encoded_output.txt","w") as encoded_file:
        for value in encoded_data:
            encoded_file.write(str(value) + " ")
    
    decoded_data = decode_lzw(encoded_data)
    with open("decoded_output.txt","w") as decoded_file:
        decoded_file.write(decoded_data)
    
    ratio = len(data) / len(encoded_data)
    print(ratio)

if __name__ == '__main__':
    main()