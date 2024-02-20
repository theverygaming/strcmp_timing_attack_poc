#!/usr/bin/env python3
import argparse
import math
import sys


# CCITT-2
baudot_table = {
    0b00011: ["a", "-"],
    0b11001: ["b", "?"],
    0b01110: ["c", ":"],
    0b01001: ["d", ""],
    0b00001: ["e", "3"],
    0b01101: ["f", ""],
    0b11010: ["g", ""],
    0b10100: ["h", ""],
    0b00110: ["i", "8"],
    0b01011: ["j", "\a"],
    0b01111: ["k", "("],
    0b10010: ["l", ")"],
    0b11100: ["m", "."],
    0b01100: ["n", ","],
    0b11000: ["o", "9"],
    0b10110: ["p", "0"],
    0b10111: ["q", "1"],
    0b01010: ["r", "4"],
    0b00101: ["s", "'"],
    0b10000: ["t", "5"],
    0b00111: ["u", "7"],
    0b11110: ["v", "="],
    0b10011: ["w", "2"],
    0b11101: ["x", "/"],
    0b10101: ["y", "6"],
    0b10001: ["z", "+"],
    0b00100: [" ", " "],
    0b01000: ["\r", "\r"],
    0b00010: ["\n", "\n"],
}

def encode_baudot(st):
    chars = st.lower()
    chars = list(filter(lambda x: x in set("".join([x[0]+x[1] for x in baudot_table.values()])), chars))

    alpha_tr = {v[0]:k for k, v in baudot_table.items()}
    sym_tr = {v[1]:k for k, v in baudot_table.items()}
    output = []
    if chars[0] in alpha_tr.keys():
        symmode = False
        output.append(0b11111) # baudot switch to letters
    else:
        symmode = True
        output.append(0b11011) # baudot switch to symbols

    for c in chars:
        tr = sym_tr if symmode else alpha_tr
        if c not in tr.keys():
            symmode = not symmode
            tr = sym_tr if symmode else alpha_tr
            if not symmode:
                output.append(0b11111) # baudot switch to letters
            else:
                output.append(0b11011) # baudot switch to symbols
        output.append(tr[c])

    return output


def decode_baudot(syms):
    symmode = False
    out_str = ""
    for sym in syms:
        if sym == 0b11111:
            symmode = False
        elif sym == 0b11011:
            symmode = True
        else:
            if sym not in baudot_table.keys():
                continue
            out_str += baudot_table[sym][int(symmode)]
    return out_str

# basically itoa
def encode(val, charset):
    base = len(charset)
    set_chars_per_alpha = math.ceil(5 / math.log2(len(charset)))
    result = ""
    while val > 0:
        m = val % base
        result += charset[m]
        val //= base
    result = "".join(reversed(result))
    return result.rjust(set_chars_per_alpha, charset[0])

# basically atoi
def decode(st, charset):
    base = len(charset)
    result = 0
    for c in st:
        result = (base * result) + charset.index(c)
    return result

parser = argparse.ArgumentParser(description="encodes & decodes alphanumeric messages using a specified set of ASCII characters")
parser.add_argument("-s", "--set", help="character set (string)", default=",.", type=str)
parser.add_argument("-d", "--decode", action="store_true")
args, unknownargs = parser.parse_known_args()

charset = sorted(list(set(args.set)))

set_chars_per_alpha = math.ceil(5 / math.log2(len(charset)))

input_str = ""
for fname in unknownargs:
    with open(fname, "r", encoding="utf-8") as f:
        input_str = f.read()

if len(unknownargs) == 0:
    input_str = sys.stdin.read()

if args.decode:
    input_str = "".join(list(filter(lambda x: x in charset, input_str)))
    # https://stackoverflow.com/a/13673133
    input_strs = [ input_str[i:i+set_chars_per_alpha] for i in range(0, len(input_str), set_chars_per_alpha) ]
    print(decode_baudot([decode(st, charset) for st in input_strs]))
else:
    print("".join([encode(x, charset) for x in encode_baudot(input_str)]))
