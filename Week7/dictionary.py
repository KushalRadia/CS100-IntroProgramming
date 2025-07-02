# DICTIONARY .....................................................................
# WE STORE KEY  VALUES PAIRS.
# THEY ARE ORDERED , CHANGEABLE , UNINDEXED , DUPLICATE KEYS ARE NOT ALLOWED , ANY DATATYPE CAN BE STORED . VALUES CAN BE LIST , FLOAT , BOOLEAN ,ETC.

# CREATING A DICTIONARY...........................................................
rank = {"John": 24 , "Janvi":22 , "Jack":12 , "Jerry": 14} # HERE John , Janvi , Jack ,  Jerry ARE KEYS AND 24 ,22 , 12 , 14 ARE VALUES.
print(rank)
print(type(rank))
print(len(rank)) # rank DICTIONARY HAS FOUR KEY-VALUES PAIRS.

# ACCESSING ITEMS OF DICTIONARY...................................................
print(rank["Jerry"]) # VALUE IS REPRESENTED BY dictionary_name[key]
print(rank.get("Janvi")) # get() IS ALSO USE TO GET VALUES WHEN KEY IS PASSED.
print(rank.keys()) # keys() IS USED TO GET ALL THE KEYS OF THE DICTIONARY. OUTPUT WILL BE :  dict_keys(['John', 'Janvi', 'Jack', 'Jerry'])
print(rank.values()) # values() IS USED TO GET ALL THE VALUES OF THE DICTIONARY .

# UPDATE VALUE IN DICTIONARY......................................................
rank["John"] = 20
print(rank)

# ADDING ELEMENTS IN DICTIONARY...................................................
rank["Samar"] = 28
print(rank)

# ADDING ANOTHER DICTIONARY.......................................................
more_rank = {"Purvi":11,"Archana":12,"Siya":10}
rank.update(more_rank)
print(rank)

# REMOVE ELEMENTS FROM A DICTIONARY...............................................
# 1) pop() - atleast have one argument.
rank.pop("John")
print(rank)
# 2) popitem() - removes the last added item , takes no argument.
rank.popitem()
print(rank)

# TO EMPTY THE DICTIONARY........................................................
more_rank.clear()
print(more_rank)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# PRINTING KEYS OF THE DICTIONARY................................................
for i in rank:
    print(i)

# PRINTING VALUES OF THE DICTIONARY..............................................
for i in rank:
    print(rank[i])

# PRINTING BOTH KEYS AND VALUES OF THE DICTIONARY - dictinoary_name.items()    
for i in rank.items(): # prints key value as a pair .
    print(i)    
for i,j in rank.items(): # prints key value but not as a pair.
    print(i,j)    

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# NESTED DICTIONARIES...........................................................
phones = {
    "Area1" : {
        "x":1,
        "y":2,
        "z":3
    },
    "Area2" : {
        "a":4,
        "b":5,
        "c":6
    },"Area3" : {
        "d":7,
        "e":8,
        "f":9
    }
}    
print(phones["Area2"]["b"])

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# QUESTION : GIVEN A DICTIONARY , WRITE A PROGRAM TO FIND THE SUM OF ALL ITEMS IN A DICTIONARY.
# INPUT : {"a": 100, "b":200, "c":300}
# OUTPUT : 600
dict1 = {"x":25,"y":18,"z":45}
dict2 = {"a": 100, "b":200, "c":300}
print(dict1.values())
# using sum() adding the values.
print(sum(dict1.values()))
print(sum(dict2.values()))
# we can use for loop also.
for i in dict1.values():
    sum += i
print("The sum is : " , sum)    
# GIVEN A STRING AND NUMBER N , WE NEED TO MIRROR THE CHARACTERS FROM THE N-th POSITION UP TO THE LENGTH OF TE STRING IN ALPHABETICAL ORDER .IN MIRROR OPERATION , WE CHANGE "a" TO "z" , "b" TO "y" , AND SO ON .
# Input : N = 3 , paradox 
# Output : paizwlc
alphabets = "abcdefghijklmnopqrstuvwxyz"
word = input("Enter a string : ")
N = int(input("Enter the value of N : "))
reverse_alphabets = alphabets[::-1] #  slicing - [start : stop : step]
dict1 = dict(zip(alphabets,reverse_alphabets)) # zip() joins elements in pair . 
s1 = word[0 : N-1]
s2 = word[N-1 : ]
mirror = ""
for i in range(len(s2)) :
    mirror = mirror + dict1[s2[i]]
Final_string = s1 + mirror    
print(Final_string)    

