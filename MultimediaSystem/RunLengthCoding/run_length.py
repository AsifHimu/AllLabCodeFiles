#encoding
def encode_RLE(data):
    encoded_data = ""
    count = 1
    char = data[0]
    for i in range(1, len(data)):
        if(data[i] == char):
            count += 1
        else:
            encoded_data += str(count) + char
            count = 1
            char = data[i]
    encoded_data += str(count) + char
    return encoded_data

#decoding
def decode_RLE(data):
    decoded_data = ""
    count = ""
    for i in data:
        if i.isdigit():
            count += i
        else:
            decoded_data += int(count) * i
            count = ""
    return decoded_data

#read the data from input files
with open("input.txt","r") as input_file:
    data = input_file.read().strip().replace(' ','')
#print(data)
encoded_data = encode_RLE(data)
#print(encoded_data)

#write the encoded data in a file
with open("encoded_output.txt","w") as encoded_file:
    encoded_file.write(encoded_data)

#decode the data with RLE and write to output file
decoded_data = decode_RLE(encoded_data)
with open("decoded_output.txt","w") as decoded_file:
    decoded_file.write(decoded_data)