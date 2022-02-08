course_dict = {'CS101': '3004',
                'CS102': '4501',
                'CS103': '6755',
                'NT110': '1244',
                'CM241': '1411'}
instructor_dict = {'CS101': 'Haynes',
                'CS102': 'Alvarado',
                'CS103': 'Rich',
                'NT110': 'Burke',
                'CM241': 'Lee'}

meeting_time_dict = {'CS101': '8:00 a.m.',
                'CS102': '9:00 a.m.',
                'CS103': '10:00 a.m.',
                'NT110': '11:00 a.m.',
                'CM241': '1:00 p.m.'}

course= (input("Please enter the course number:"))

if course in course_dict:
    print ("The room number for", course, "is:", course_dict[course])
    print ("The intructor name for", course, "is:", instructor_dict[course])
    print ("The meeting time for", course, "is:", meeting_time_dict[course])

else:
    print ("The Course ID you have entered is invalid.")


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
        'K' : '_', 'k' : 'Y',
        'L' : '-', 'l' : 'U',
        'M' : '=', 'm' : 'W',
        'N' : '+', 'n' : 'R',
        'O' : '~', 'o' : 'S',
        'P' : '`', 'p' : 'P',
        'Q' : '?', 'q' : 'L',
        'R' : '/', 'r' : 'K',
        'S' : '>', 's' : 'N',
        'T' : '.', 't' : 'B',
        'U' : '<', 'u' : 'V',
        'V' : ',', 'v' : 'T',
        'W' : '"', 'w' : 'Q',
        'X' : "'", 'x' : 'A',
        'Y' : '[', 'y' : 'Z',
        'Z' : '|', 'z' : 'X'}

#The program should open a specified text file, read its contents, then use the dictionary to write an encrypted version of the file’s contents to a second file. 
#Each character in the second file should contain the code for the corresponding character in the first file

security_file= open("C:/Users/Riley/Downloads/MSIS Homework/AdvancedPython/mydictionaries/info_security.txt", 'r')

infile = security_file.read()
security_file.close()

outfile= open("encrypted_info_security.txt", 'w')

for character in infile:
    if character in codes:
        outfile.write(codes[character])

    else:
        outfile.write(character)

outfile.close()
