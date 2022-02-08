codes = {'A' : '%', 'a' : '9',
        'B' : '@', 'b' : '2',
        'C' : '!', 'c' : '1',
        'D' : '#', 'd' : '4',
        'E' : '$', 'e' : '5',
        'F' : '^', 'f' : '6',
        'G' : '&', 'g' : '3',
        'H' : '*', 'h' : '7',
        'I' : '(', 'i' : '8',
        'J' : ')', 'j' : '0',
        'K' : '_', 'k' : 'Ò',
        'L' : '-', 'l' : 'Ó',
        'M' : '=', 'm' : 'Ô',
        'N' : '+', 'n' : '¬',
        'O' : '~', 'o' : 'Õ',
        'P' : '`', 'p' : '×',
        'Q' : '?', 'q' : 'Ö',
        'R' : '/', 'r' : '¨',
        'S' : '>', 's' : 'ê',
        'T' : '.', 't' : 'æ',
        'U' : '<', 'u' : 'Á',
        'V' : ',', 'v' : '¾',
        'W' : '"', 'w' : 'À',
        'X' : "'", 'x' : '»',
        'Y' : '[', 'y' : '´',
        'Z' : '|', 'z' : '╣'}



security_file= open("C:/Users/Riley/Downloads/MSIS Homework/AdvancedPython/mydictionaries/info_security.txt", 'r')

infile = security_file.read()
security_file.close()

outfile= open("encrypted_info_security.txt", 'w')

for ch in infile:
    if ch in codes:
        outfile.write(codes[ch])

    else:
        outfile.write(ch)

outfile.close()
outfile = open ("C:/Users/Riley/Downloads/MSIS Homework/AdvancedPython/mydictionaries/info_security.txt", 'r')
infile = outfile.read()
outfile.close()
codes_items = codes.items()

for ch in infile:
    if not ch in codes.values() or ch == '.'or ch == ',' or ch == '!':
        print(ch)
    else:
        for key, value in codes_items:
            if ch == value and ch != '.':
                print(key, end='')