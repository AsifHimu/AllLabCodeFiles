import os
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


def main():
    # Read data from input file
    with open('input.txt', 'r') as input_file:
        data = input_file.readlines()

    # Encode the data
    encoded_data = ''
    for line in data:
        encoded_data += encode_RLE(line.rstrip()) + '\n'

    # Write encoded data to output file
    with open('encoded_output.txt', 'w') as encoded_file:
        encoded_file.write(encoded_data)

    # Decode the encoded data
    decoded_data = ''
    for line in encoded_data.splitlines():
        decoded_data += decode_RLE(line.rstrip()) + '\n'

    # Write decoded data to output file
    with open('decoded_output.txt', 'w') as decoded_file:
        decoded_file.write(decoded_data)

    print("Encoding and decoding completed successfully.")
    
    #Finding file size
    input_file_size = os.path.getsize('input.txt')
    encoded_file_size = os.path.getsize('encoded_output.txt')
    print("File Size is :", input_file_size, "bytes")
    print("File Size is :", encoded_file_size, "bytes")
    ratio = input_file_size / encoded_file_size
    print("Compression ratio : %0.2f" %ratio)
if __name__ == '__main__':
    main()
