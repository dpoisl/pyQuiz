from decimal import Decimal
from itertools import izip_longest
izl = izip_longest


def i10n_number_unobfuscated(number, thousands=".", comma=","):
    integer = str(abs(int(number)))
    rest = str(abs(number - int(number)))[2:]
    decimal_places = str(rest)[2:]
    segments = []
    for triplet in izip_longest(integer[-1::-3], integer[-2::-3], integer[-3::-3]):
        string_triplet = ""
        for digit in triplet:
            if digit is not None:
                string_triplet += digit
        segments.append(string_triplet)
    result = thousands.join(segments)
    result = result[::-1]
    if rest != "":
        result = result + comma + rest
    if number < 0:
        result = "-" + result
    return result


def i10n_number_obfuscated(n, t=".", c=","):
    return ("-" if n < 0 else "")+t.join("".join(d for d in t if d is not None) for t in izl(str(abs(int(n)))[-1::-3],str(abs(int(n)))[-2::-3],str(abs(int(n)))[-3::-3]))[::-1]+((c+str(abs(n-int(n)))[2:]) if str(abs(n-int(n)))[2:] != "" else "")


def test():
    import sys
    if len(sys.argv) < 2:
        sys.stderr.write("Usage: %s number\n" % sys.argv[0])
        sys.exit(1)
    print("----- UNOBFUSCATED -----")
    print("as float: %s -> %s" % (float(sys.argv[1]), i10n_number_unobfuscated(float(sys.argv[1]))))
    print("as Decimal: %s -> %s" % (Decimal(sys.argv[1]), i10n_number_unobfuscated(Decimal(sys.argv[1]))))
    try:
        print("as int: %s -> %s" % (int(sys.argv[1]), i10n_number_unobfuscated(int(sys.argv[1]))))
    except ValueError:
        print("no int")
    print("----- OBFUSCATED -----")
    print("as float: %s -> %s" % (float(sys.argv[1]), i10n_number_obfuscated(float(sys.argv[1]))))
    print("as Decimal: %s -> %s" % (Decimal(sys.argv[1]), i10n_number_obfuscated(Decimal(sys.argv[1]))))
    try:
        print("as int: %s -> %s" % (int(sys.argv[1]), i10n_number_obfuscated(int(sys.argv[1]))))
    except ValueError:
        print("no int")
    sys.exit(0)

if __name__ == "__main__":
    test()
