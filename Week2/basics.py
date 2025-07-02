print("HELLO WORLD  AND HELLO HOME !!")
# "\n"(WITH QUOTES) IS USED FOR NEXT LINE IN PYTHON.
# # IS USED FOR GIVING COMMENTS IN PYTHON.
print("HELLO,\nWORLD \nI AM LUFFY!!")
# FOR MULTIPLE LINE COMMENT WE USE ''' '''. SEE DIFFERENCE BETWEEN LINE 6-9 , LINE 10 and LINE 12-17.
'''HIII IAM 
USING 
MULTIPLE LINE
COMMENT'''

#  PYTHON CLI(CLIENT LINE INTERFACE) WHERE USE CAN USE REPL - READ , EVALUATE , PRINT , LOOP USING VS CODE TERMINAL OR EXTERNAL TERMINAL.ONE WAY TO EXIT FROM THIS TERMINAL OR REPL IS TO PRESS Ctrl+d OR exit() .

# DATA TYPES.........................................................................
# a = 3 --- INTEGER DATA TYPE
# b = 3.45 --- FLOAT DATA TYPE 
# c = "khushbu" --- STRING DATA TYPE
# d = True , False ---  BOOLEAN DATA TYPE
# e = None --- NULL DATA TYPE
# AS IN C++ OR C WE CAN USE $ IN VARIABLE NAMING BUT IN PYTHON WE DON'T USE $ IN VAIABLE NAMES.
''' DATA TYPES 
1) NUMERIC DATA TYPE - INT , FLOAT , COMPLEX (2+3j).
2) SEQUENCE DATA TYPE - TUPLE , LIST .
3) TEXT DATA TYPE - STRING .
4) MAPPING DATA TYPES - DICTIONARY .
5) SET DATA TYPE - Unordered collection of unique items.
6) None DATA TYPE - It represents null value and it stores nothing.
'''

# VARIABLES...........................................................................
name = "AAHANA"
age = 23
print(type(name)) # TO CHECK DATA TYPE 
print(type(age))

# CONCATENATION OF STRINGS(ONLY POSSIBLE IN SAME DATA TYPES).........................
print("MY NAME IS " + name + " AND I AM" , age , "YEARS OLD.")
print("@" + "#" + "&")

# PRINTING WITH SEPERATOR.............................................................
print(1,2,3,4,5,6,7,8,9,0, sep  = "#")
print(1234567890 , sep = "#")
print(123, end ="#\n")
print(1,2,3,4,5,6 , end ="#\n")
# ASCII VALUES........................................................................
# ASCII - AMERICAN STANDARD CODE FOR INFORMATION EXCHANGE(COMMON FOR ALL PROGRAMMING LANGUAGES).
# a-z : 97 to 122.
# A-Z : 65 to 90.                    
# 0 to 9 : 48 to 57.
# SPACE : 32
char = "@"
ch = "a"
ch1 = "$"
print(ord(char))
print(ord(ch))
print(ord(ch1))
# ord() is used to display ascii values of a character. This function takes a character of lenth one. Since a character is always of length one. Always use quotes for character.
ascii = 67
ascii1 = 35
ascii2 = 46
print(chr(ascii))
print(chr(ascii1))
print(chr(ascii2))
# chr() is opposite of ord(). It is used to dispaly character from the ascii values.  

# INPUT ...................................................................................
name1 = input("Enter your name : ")
print(name1)
# input() always takes a string as an input . If we want to take input as an integer or float we do TYPECASTING(conversion of one data type to another).
roll_number = int(input("Enter your roll number : "))
print(roll_number)
print(int(3.13))
print(int(3.89))
print(float("123"))
print(str(123))