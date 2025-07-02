# LIST..................................................................................
# THEY ARE MUTABLE , ORDERED , HAVE INDEX STARTING FROM ZERO , DUPLICATES VALUES ALLOWED , ANY DATATYPE CAN BE STORED , MIX OF DATA TYPES CAN ALSO BE STORED.

fruits = ['Apple','Banana','Kiwi','Pineapple','Guava'] # CREATING A LIST
print(fruits) # PRINTING OF A LIST
print("If mango is not present in fruits : ", "mango"  not in fruits)
print("If Kiwi is present in fruits : ", "Kiwi" in fruits)


list = [1,2,3,5,7,2,5,3,5,2,5,2] # INDEXING IN LIST----------------------------------------------------
# LIST INDEX STARTS FROM ZERO , SO list[0] = 1 , list[1] = 2 . LISTS ALSO HAVE NEGATIVE INDEX - list[-1] =2 , list[-2]= 5 .
list1 = print(list[3:9]) # PRINTING SUBPART OF LIST STARTING FROM 3 TO 8. 
list2 = print(list[-9:-3]) # -3 : -9 SHOW EMPTY LIST
print(list1 == list2)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# ADDING ELEMENTS TO A LIST-----------------------------------------------------------------------------
# 1) append() # ADDS ITEM TO THE END OF THE LIST.
fruits.append("Litchi")
print(fruits)

# 2) insert() # USED TO INSERT AN ELEMENT AT A PARTICULAR INDEX. ALWAYS TAKES 2 PARAMETERS.
fruits.insert(2,"Mango")
print(fruits)

# 3) extend() # USED TO APPEND ANOTHER LIST AT THE END OR USED TO ADD ANOTHER DATA TYPE LIST AT END.
list2 = ["Anna","Amma","Appa","Mummy", "Papa", "Me"]
list4 = [10,40,20]
list.extend(list4)
print(list)
list.extend(list2)
print(list)
list3 = list.extend(list4) # SHOWS None AS list3 IS EMPTY AND CHANGE IS APPLIED TO list.
print(list3)

# INSTEAD OF USING extend(),WE CAN CONCATE TWO LISTS.
arr1 = ["bhai","maa","appa","family"]
arr1 = list2 + arr1 # aar1 + list2 adds elements of list2 at end.
print(arr1)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# REMOVING ELEMENTS FROM A LIST---------------------------------------------------------------------------
# 1) remove() # REMOVES SPECIFIED ITEMS
list_1 = [10,37,83,76,47,30,24,13]
list_1.remove(76)
print(list_1)

# 2) pop() # REMOVES ITEMS AT GIVEN INDEX OTHERWISE REMOVES LAST 
list_1.pop(3)
print(list_1)
list_1.pop()
print(list_1)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# CHANGING ITEM IN A LIST SINCE IT IS MUTABLE-------------------------------------------------------------
# 1) at an index -- changes(updates) a value in a list
list_2 =[10,20,30,40,50,60]
list_2[4] = 70
print(list_2)

# 2) in a range -- changes a part of list or changes a sublist 
list_2[1:4] = [12,14,16]
print(list_2)
list_2[1:4] = [11,22] # imp -- if len(list) given is less than the range then it removes extra index element of original list.
print(list_2)
list_2[1:4] = [12,14,16,18,22] # imp -- if len(list) given is more than the range then it adds extra index element of original list.
print(list_2)

print(fruits)
fruits[1:3] = ["Grapes","papaya"]
print(fruits)
fruits[1:3] = "Orange" # imp -- if in place of list , string is given then then it considers each character of a list as a list.
print(fruits)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# SORTING A LIST..........................................................................
fruits.sort() # SORTS LIST IN ASCENDIND ORDER BY DEFAULT,IN CASE OF STRING SORTS LIST IN ALPHABETICAL ORDER BY DEFAULT.
print(fruits)
# FOR DESCENDING WAY - USE sort(reverse=True)
fruits.sort(reverse=True)
print(fruits)

print(list_2)
list_2.sort()
list_2.sort(reverse = True)
print(list_2)

# FOR REVERSING THE LIST - USE reverse() . IT REVERSE THE LIST IF IN ASCENDING , FUNCTION SORTS IT IN DESCENDING ORDER AND IF IN DESCENDING , IT REVERSES IT IN ASCENDING ORDER.
fruits.reverse()
print(fruits)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# TRAVERSING THE LIST USING FOR LOOP...................................................... 
lst = [10,30,50,20,40]
newlist = []
for i in lst:
    if i > 25 :
        newlist.append(i)
print(newlist)


# LIST COMPREHENSION......................................................................
# USED WHEN WE WANT TO MAKE A NEW LIST FROM ITEMS OF AN EXISTING LIST.
newlist1 = [i for i in lst if i > 25]
print(newlist1)

newfruits = [i for i in fruits if "a" in i]
print(newfruits)


# COPYING A LIST.........................................................................
new_list2 = list2.copy()
print(new_list2)


# NESTED LIST...............................................................
listt = [10,20,[30,40,50],60,32,[11,45],22]
print(listt[2]) 
print(listt[5]) 
print(listt[2][1])

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# QUESTIONS......................................................................
# 1) GIVEN A LIST IN PYTHON AND PROVIDED THE ELEMENTS IN THE INDEX OF THE ELEMENTS. WRITE A PROGRAM TO SWAP THE TWO ELEMENTS IN THE LIST.
# EXAMPLE - INPUT: LIST = [23,65,19,90] , idx1 = 0 , idx2 = 2 
# OUTPUT : [19,65,23,90]
LIST = []
size = int(input("Enter the size of the list : "))
for i in range(size):
    num =int(input("Enter element of list : "))
    LIST.append(num)
print("Original list is : " , LIST)    
# for swapping idx1 and idx2
idx1 = int(input("Enter index 1 :"))       
idx2 = int(input("Enter index 2 :"))    
temp = LIST[idx2] 
LIST[idx2] = LIST[idx1]
LIST[idx1] = temp
print("Swapped list is : ", LIST)