#!/usr/bin/env python3
import argparse
import math
import sys

def encode_msg(data):
    return [int(b) for b in data]

def decode_msg(syms):
    out_bytes = bytearray()
    for sym in syms:
        out_bytes.append(sym)
    return out_bytes

# basically itoa
def encode(val, charset):
    base = len(charset)
    set_chars_per_alpha = math.ceil(8 / math.log2(len(charset)))
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

set_chars_per_alpha = math.ceil(8 / math.log2(len(charset)))


if args.decode:
    input_str = ""
    for fname in unknownargs:
        with open(fname, "r", encoding="utf-8") as f:
            input_str = f.read()

    if len(unknownargs) == 0:
        input_str = sys.stdin.read()

    input_str = "".join(list(filter(lambda x: x in charset, input_str)))
    # https://stackoverflow.com/a/13673133
    input_strs = [ input_str[i:i+set_chars_per_alpha] for i in range(0, len(input_str), set_chars_per_alpha) ]
    sys.stdout.buffer.write(decode_msg([decode(st, charset) for st in input_strs]))
else:
    input_data = ""
    for fname in unknownargs:
        with open(fname, "rb") as f:
            input_data = f.read()

    if len(unknownargs) == 0:
        input_data = sys.stdin.buffer.read()

    print("".join([encode(x, charset) for x in encode_msg(input_data)]))
