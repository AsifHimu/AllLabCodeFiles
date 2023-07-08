from decimal import Decimal,getcontext
from collections import Counter

getcontext.prec = 15

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

