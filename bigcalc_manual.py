"""Manual big integer calculator using digit operations only."""

import sys


def _strip_leading_zeros(txt):
    idx = 0
    ln = len(txt)
    while idx < ln and txt[idx] == '0':
        idx += 1
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
        return -1
    i = 0
    while i < la:
        ca = a[i]
        cb = b[i]
        if ca > cb:
            return 1
        if ca < cb:
            return -1
        i += 1
    return 0


def add_strings(a, b):
    a = a[::-1]
    b = b[::-1]
    la = len(a)
    lb = len(b)
    mx = la if la > lb else lb
    carry = 0
    out = []
    i = 0
    while i < mx:
        da = ord(a[i]) - 48 if i < la else 0
        db = ord(b[i]) - 48 if i < lb else 0
        s = da + db + carry
        carry = s // 10
        digit = s % 10
        out.append(chr(48 + digit))
        i += 1
    if carry:
        out.append(chr(48 + carry))
    return ''.join(reversed(out))


def sub_strings(a, b):
    if _compare(a, b) < 0:
        raise ValueError('Negative result')
    a = a[::-1]
    b = b[::-1]
    la = len(a)
    lb = len(b)
    out = []
    borrow = 0
    i = 0
    while i < la:
        da = ord(a[i]) - 48
        db = ord(b[i]) - 48 if i < lb else 0
        temp = da - borrow
        if temp < db:
            temp += 10
            borrow = 1
        else:
            borrow = 0
        digit = temp - db
        out.append(chr(48 + digit))
        i += 1
    result = ''.join(reversed(out))
    return _strip_leading_zeros(result)


def mul_strings(a, b):
    a = a[::-1]
    b = b[::-1]
    la = len(a)
    lb = len(b)
    res = [0 for _ in range(la + lb)]
    ia = 0
    while ia < la:
        carry = 0
        da = ord(a[ia]) - 48
        ib = 0
        while ib < lb:
            db = ord(b[ib]) - 48
            pos = ia + ib
            prod = da * db + carry + res[pos]
            carry = prod // 10
            res[pos] = prod % 10
            ib += 1
        res[ia + lb] += carry
        ia += 1
    out = ''.join(chr(48 + d) for d in reversed(res))
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
        rem = _strip_leading_zeros(rem + ch)
        digit = 0
        while _compare(rem, b) >= 0:
            rem = sub_strings(rem, b)
            digit += 1
        out.append(chr(48 + digit))
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
