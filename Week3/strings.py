# STRINGS.......................................................................................
# STRINGS ARE SEQUENCE OF CHARACTERS WITHIN "", '', ''' '''. THEY ARE  IMMUTABLE WHICH MEANS WE CAN CREATE NEW STRING BY MANIPULATING ORIGINAL STRING. 

# CREATING STRINGS 
name_1 = "COLLEGE WALLAH"
name_2 = 'PHYSICS WALLAH'
name_3 = '''PW SKILLS'''
print(name_1,name_2,name_3 , sep = " , ")
print(type(name_3))

# FOR MULTILINES STRINGS IN FORM OF PARAGRAPH CAN BE WRITTEN USING ''' ''' AND THIS WILL PRINT THE OUTPUT IN NEXT LINE.
print('''I am still trying to be best 
but many obstacles are there
but I will succed someday.''')

# INDEXING IN STRINGS IS JUST LIKE LISTS............................................................................
txt = "Hello world!"
print(txt[-1])
print(txt[0])
print(txt[5])
print(txt[-4])
print("\n")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# TRAVERSING A STRING............................................................
# 1) USING FOR LOOP :
for i in name_1 :
    print(i)
# 2) USING LIST COMPREHENSION :
print("\n")
list = [i for i in name_2]
print(list)
print("\n") 
list_1 = [i for i in name_3]
for i in list_1:
    print(i)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# TO FIND A CHAR/SUBSTRING IN A STRING ..........................................
print(name_1.find('E')) # GIVES THE INDEX OF FIRST OCCURENCE.
print(name_1.find("T")) # GIVES -1 IF CHARACTER OR SUBSTRING IS NOT PRESENT IN THE STRING.
print(name_1.find("LLAH")) 

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# SLICING A STRING...............................................................
# SYNTAX - [start : end : step] 
str = "National Institute Of Technology Raipur"
print(str[ : 14])
print(str[14: ])
print(str[-10 : ])
print(str[ : -20])

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# MODIFYING STRINGS..............................................................
# 1) FOR CONVERTING CHARACTERS TO UPPERCASE
str1 = str.upper() # MAKES A NEW STRING str1 AND DOESNOT CHANGE THE ORIGINAL STRING.
print(str1)

# 2) FOR CONVERTING CHARACTERS TO LOWERCASE
str2 = name_1.lower()
print(str2)
string_1 = "sdhsjJSDDBAJ"
string_2 =string_1.lower()
print(string_2)

# 3) FOR CAPITALISING THE FIRST CHARACTER OF STRING
string_3 = string_2.capitalize()
print(string_3)

# 4) FOE STRIPPING / REMOVING TRAILING WHITE-SPACES
s1 = "   sugfwseui dfgewyh      "
print(s1.strip())
print(s1) # DOESNOT MODIFY ORIGINAL STRING s1

# 5) replace() - REPLACES OLD STRINGS WITH NEW STRINGS . IF COUNT IS NOT GIVEN - ALL OCCURENCE IN OLD STRING IS REPLACED . 
# SNTAX - string.replace(old_substring , new_substring , count)
s2 = "Hello World ! What a beautiful World this is."
print(s2.replace("World" , "Earth")) # COUNT IS NOT GIVEN , SO IT REPLACES BOTH THE World WITH Earth .
s3 = "Hello ! This is me. Hello , welcome to python programming."
print(s3.replace("Hello" , "Namaskaram" , 1)) # COUNT IS GIVEN SO IT REPLACES ONLY 1 Hello WHICH OCCURS FIRST WITH Namaste .

# 6) split() - USED TO SPLIT THE STRING INTO A LIST OF SUBSTRINGS. BY DEFAULLT SEPERATOR IS " "
# SYNTAX - string.split(sep,maxsplit) WHERE sep , maxslpit ARE OPTIONAL PARAMETERS. sep ="," MEANS STRINGS SEPERATES FROM COMMA AND maxsplit = 1 MEANS ONLY AT ONE SEP STRINGS SPLITS AFTER THAR STRING WON'T SPLIT(i.e how many times we want to split at the seperator.)
s4 = s3.split()
print(s4)
s5 = "ria,pia,sia,mia,nia,kia"
print(s5.split(","))
print(s5.split("," , 2))

# 7) CONCATENATION OF A STRING
strr1 = "HELLO PW"
strr2 = "HELLO CW"
print(strr1+ strr2)

# 8) format() - THIS IS USED TO INSERT VARIABLE VALUES IN A STRING.
student_name = "Aahana"
student_marks = 98
student_address  = "Mumbai"
strr3 = "The name of student is {s} and she got {r} marks . She lives in {f1}.".format(s = student_name , r = student_marks , f1 = student_address) 
print(strr3)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# ESCAPE CHARACTERS.....................................................................
# 1) \'    -  SINGLE QUOTE
# 2) \\    -  BACKSLASH
# 3) /n    -  NEW LINE
# 4) \r    -  CARRIAGE RETURN
# 5) \t    -  TAB 
# 6) \b    -  BACKSPACE
# 7) \f    -  FORM FEED 
# 8) \ooo  -  OCTAL VALUE
# 9) \xhh  -  HEX VALUE

# QUESTION : WRITE A PYTHON FUNCTION THAT CHECKS IF THE GIVEN STRING IS A PALINDROME OR NOT.
# INPUT : maam
# OUTPUT : True
def palindrome(string):
    if string[::-1] == string:
        return True 
    else:
        print("Given string", string ,"is not a palindrome." )
        return False
str = input("Enter a string : ")
str1 = str.replace(" ","")
str2 = str1.lower()
print(palindrome(str2))

# QUESTION : WRITE A PYTHON PROGRAM THAT PRINTS ALL WORDS THAT ARE OF EVEN LENGTH IN THE GIVEN STRING.
# INPUT : we love to code in the python
# OUTPUT : we love to code in python
list = []
string = input("Enter a string : ")
strq = string.split()
for i in strq:
    if len(i) % 2 == 0 :
        list.append(i)
print(" ".join(list))
