#encoding
def encode_lzw(data):
    dictionary = {chr(i): i for i in range(256)}
    next_code = 256
    
    #intialize variables for encoding
    current_string = data[0]
    encoded_data = []
    
    for symbol in data[1:]:
        if current_string + symbol in dictionary:
            current_string = current_string + symbol
        else:
            encoded_data.append(dictionary[current_string])
            dictionary[current_string + symbol] = next_code
            next_code += 1
            current_string = symbol
    #add the last code to the encoded data
    encoded_data.append(dictionary[current_string])
    return encoded_data

#decoding
def decode_lzw(data):
    dictionary = {i: chr(i) for i in range(256)}
    next_code = 256
    
    #intialize variables for decoding
    current_code = data[0]
    decoded_data = dictionary[current_code]
    previous_string = decoded_data
    
    for code in data[1:]:
        if code in dictionary:
            current_string = dictionary[code]
        else:
            current_string = previous_string + previous_string[0]
            
        decoded_data += current_string
        #add new entry to the dictionary
        dictionary[next_code] = previous_string + current_string[0]
        next_code += 1
        
        previous_string = current_string
    return decoded_data    

#read the data form input file
with open("input.txt","r") as input_file:
    data = input_file.read().strip().replace(' ','')

#encode the data with lzw and write to output file
encoded_data = encode_lzw(data)
with open("encoded_output.txt","w") as encoded_file:
    for value in encoded_data:
        encoded_file.write(str(value) + " ")
# decode the data with LZW and write to output file
decoded_data = decode_lzw(encoded_data)
with open("decoded_output.txt", "w") as decoded_file:
    decoded_file.write(decoded_data)