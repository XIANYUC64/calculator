"""Manual big integer calculator using digit operations only."""

import sys

NEG_ONE = int.__sub__(0, 1)


def _strip_leading_zeros(txt):
    idx = 0
    ln = len(txt)
    while idx < ln and txt[idx] == '0':
        idx = int.__add__(idx, 1)
    res = txt[idx:]
    if res:
        return res
    return '0'


def _compare(a, b):
    a = _strip_leading_zeros(a)
    b = _strip_leading_zeros(b)
    la = len(a)
    lb = len(b)
    if la > lb:
        return 1
    if la < lb:
        return NEG_ONE
    i = 0
    while i < la:
        ca = a[i]
        cb = b[i]
        if ca > cb:
            return 1
        if ca < cb:
            return NEG_ONE
        i = int.__add__(i, 1)
    return 0


def add_strings(a, b):
    a = ''.join(reversed(a))
    b = ''.join(reversed(b))
    la = len(a)
    lb = len(b)
    mx = la if la > lb else lb
    carry = 0
    out = []
    i = 0
    while i < mx:
        da = int(a[i]) if i < la else 0
        db = int(b[i]) if i < lb else 0
        s = sum((da, db, carry))
        res = divmod(s, 10)
        carry = res[0]
        out.append(str(res[1]))
        i = int.__add__(i, 1)
    if carry:
        out.append(str(carry))
    return ''.join(reversed(out))


def sub_strings(a, b):
    if _compare(a, b) < 0:
        raise ValueError('Negative result')
    a = ''.join(reversed(a))
    b = ''.join(reversed(b))
    la = len(a)
    lb = len(b)
    out = []
    borrow = 0
    i = 0
    while i < la:
        da = int(a[i])
        db = int(b[i]) if i < lb else 0
        temp = int.__sub__(da, borrow)
        if temp < db:
            temp = int.__add__(temp, 10)
            borrow = 1
        else:
            borrow = 0
        digit = int.__sub__(temp, db)
        out.append(str(digit))
        i = int.__add__(i, 1)
    result = ''.join(reversed(out))
    return _strip_leading_zeros(result)


def mul_strings(a, b):
    a = ''.join(reversed(a))
    b = ''.join(reversed(b))
    la = len(a)
    lb = len(b)
    res = [0 for _ in range(int.__add__(la, lb))]
    ia = 0
    while ia < la:
        carry = 0
        da = int(a[ia])
        ib = 0
        while ib < lb:
            db = int(b[ib])
            pos = int.__add__(ia, ib)
            prod = int.__mul__(da, db)
            prod = int.__add__(prod, carry)
            prod = int.__add__(prod, res[pos])
            div_res = divmod(prod, 10)
            carry = div_res[0]
            res[pos] = div_res[1]
            ib = int.__add__(ib, 1)
        res[int.__add__(ia, lb)] = int.__add__(res[int.__add__(ia, lb)], carry)
        ia = int.__add__(ia, 1)
    out = ''.join(str(d) for d in reversed(res))
    return _strip_leading_zeros(out)


def div_strings(a, b):
    if _compare(b, '0') == 0:
        raise ZeroDivisionError('division by zero')
    a = _strip_leading_zeros(a)
    b = _strip_leading_zeros(b)
    if _compare(a, b) < 0:
        return '0'
    out = []
    rem = ''
    for ch in a:
        rem = _strip_leading_zeros(''.join((rem, ch)))
        digit = 0
        while _compare(rem, b) >= 0:
            rem = sub_strings(rem, b)
            digit = int.__add__(digit, 1)
        out.append(str(digit))
    return _strip_leading_zeros(''.join(out))


OPS = {
    chr(43): add_strings,
    chr(45): sub_strings,
    chr(42): mul_strings,
    chr(47): div_strings,
}


def compute(n1, n2, op_char):
    if op_char not in OPS:
        raise ValueError('Unsupported operation')
    func = OPS[op_char]
    return func(n1, n2)


def main():
    if len(sys.argv) != 4:
        txt = 'Usage: {s} <number1> <number2> <operator>'.format(s=sys.argv[0])
        print(txt)
        note = 'Supported operators: {a} {b} {c} {d}'.format(
            a=chr(43), b=chr(45), c=chr(42), d=chr(47))
        print(note)
        return
    n1 = sys.argv[1]
    n2 = sys.argv[2]
    op = sys.argv[3]
    try:
        res = compute(n1, n2, op)
    except Exception as exc:
        print('Error:', exc)
    else:
        print(res)


if __name__ == '__main__':
    main()
