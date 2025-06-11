import operator
from decimal import Decimal, getcontext
import sys

# Set precision high enough for fifty digit numbers
getcontext().prec = 120

# Map from symbol characters to operation functions without using the symbols directly
OPS = {
    chr(43): operator.add,
    chr(45): operator.sub,
    chr(42): operator.mul,
    chr(47): operator.truediv,
}

def compute(num1, num2, op_char):
    """Compute the result of applying the chosen operation to two numbers."""
    if op_char not in OPS:
        raise ValueError("Unsupported operation")
    a = Decimal(num1)
    b = Decimal(num2)
    func = OPS[op_char]
    return func(a, b)

def main():
    if len(sys.argv) != 4:
        script = sys.argv[0]
        txt = "Usage: {s} <number1> <number2> <operator>".format(s=script)
        print(txt)
        note = "Supported operators: {a} {b} {c} {d}".format(
            a=chr(43),
            b=chr(45),
            c=chr(42),
            d=chr(47),
        )
        print(note)
        return
    num1, num2, op = sys.argv[1], sys.argv[2], sys.argv[3]
    try:
        result = compute(num1, num2, op)
    except Exception as exc:
        print("Error:", exc)
    else:
        print(result)

if __name__ == "__main__":
    main()
