from decimal import Decimal,getcontext
from collections import Counter

getcontext().prec = 15

def generate_probability_range(symbols):
    total_count = len(symbols)
    symbol_count = Counter(symbols)
    prob_range = {}
    low = Decimal(0)
    for symbol, count in symbol_count.items():
        prob = Decimal(count) / Decimal(total_count)
        high = low + prob
        prob_range[symbol] = (low, high)
        low = high
    
    return prob_range

def encode(symbols,prob_range):
    low = Decimal(0)
    high = Decimal(1)
    for symbol in symbols:
        symbol_low, symbol_high = prob_range[symbol]
        range_width = high - low
        high = low + range_width * symbol_high
        low = low + range_width * symbol_low
        print(symbol, low, high)
    
    return (low,high)

def decode(encoded_message,prob_range,message_length):
    low, high = encoded_message
    message = ""
    print(prob_range.items())
    for i in range(message_length):
        for symbol, symbol_range in prob_range.items():
            symbol_low, symbol_high = symbol_range
            symbol_width = symbol_high - symbol_low
            if low >= symbol_low and high <= symbol_high:
                message += symbol
                high = (high - symbol_low) / symbol_width
                low = (low - symbol_low) / symbol_width
                break
    
    return message

with open("input.txt","r") as input_file:
    input_string = input_file.read()

prob_range = generate_probability_range(input_string)
encoded_message = encode(input_string,prob_range)
decoded_message = decode(encoded_message,prob_range,len(input_string))

with open("encoded_output.txt","w") as encoded_file:
    encoded_file.write(str(encoded_message))

with open("decoded_output.txt","w") as decoded_file:
    decoded_file.write(decoded_message)  