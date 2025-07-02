# TUPLES.....................................................................................
# USED TO STORE MULTIPLE ITEMS OR VALUES IN A VARIABLE.
# THEY ARE ORDERED , IMMUTABLE(OPERATIONS LIKE APPEND , SORT , REMOVE ARE NOT APPLICABLE) , DUPLICATES ALLOWED , CAN STORE ANY DATATYPES AND MIX DATA TYPES CAN ALSO BE STORED.


fav_colours = ("Blue","White","Purple","Lavendar","Dark blue","Black") # CREATING A TUPLE
fruits = tuple("kiwi") # (TYPECASTING) THIS IS USED ONLY FOR 1 ELEMENT TUPLE (TAKES ONE ARGUMENT) 
colours = ("Magenta",) # CREATING A TUPLE WITH 1 ITEM (ALWAYS ADD A COMMA AT LAST IN CASE OF SINGLE ELEMENT). WITHOUT COMMA IT WILL ACT AS STRING.


print(type(fav_colours))
print(type(fruits))
print(len(fav_colours)) # LENGTH OF TUPLE


# ACCESSING ELEMENTS OF TUPLES...............................................................
print(colours[0]) # POSITIVE INDEX STARTS FROM ZERO
print(fav_colours[4]) # POSITIVE INDEXING
print(fav_colours[-3]) # NEGATIVE INDEXING
print(fav_colours[2:6]) # RANGE INDEXING
print(fav_colours[-4 :-1]) # -1:-4 SHOWS EMPTY TUPLE


# CHECKING IF AN EXISTS IN TUPLE............................................................
if "green" not in fav_colours:
    print("Green is not present in tuple.")


# TRAVERSING A TUPLE.........................................................................
for i in fav_colours:
    print(i)


# CONCATENATING TWO TUPLES...................................................................
more_colours = ("red","yellow","green","orange")
colors = fav_colours + more_colours
print(colors)
    

# UNPACKING A TUPLE.........................................................................
colour1 , colour2 , colour3 , colour4 = more_colours
print(colour1 , colour2 , colour3 , colour4)


# WHY WE USE TUPLE INSTEAD OF LIST EVEN THOUGH TUPLES ARE INMUTABLE AND LISTS ARE MUTABLE?
# ANSWER IS : ITERATING THROUGH TUPLE IS FASTER THAN LIST .


# QUESTION : REVERSING A TUPLE.
# FOR THIS QUESTION WE ARE USING reversed() WHICH ITERATES THE ELEMENTS IN REVERSE ORDER.
list = []
size = int(input("Enter the no. of items in tuple: "))
for i in range(size):
    num = int(input("Enter the items of the tuple : \n"))
    list.append(num)
tpl1 = tuple(list)  
list1 = []
print("Original tuple is : " , tpl1)  
for j in reversed(tpl1):
    list1.append(j)
tpl2 = tuple(list1)
print("Reversed tuple is : " , tpl2)    



