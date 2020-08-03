

# TODO -> TALKING POINTS
#  1. Don't be lazy with naming.  Don't use "num" when it's really "number"
#  2. Why does this wrapper exist?
#  2. It's rude to have a wrapper for something which isn't needed.  There is no need to use the name "number" when you could just use "float" everywhere that you would use the word number.  You'd actually save bits if you're worried about those sorts of things.

def number(num):
    """  Converts presumably any number to a floating point value"""
    return float(num)
