# SETS.......................................................................................
# SETS SRE CONTAINERS FOR STORING MULTIPLE VALUES IN A VARIABLE .
# SETS ARE UNORDERED , IMMUTABLE(cannot update existing values but can add or remove elements) , UNINDEXED , DUPLICATES ARE NOT ALLOWED , ANY DATATYOE CAN BE STORED , MIX OF DATATYPES CAN ALSO BE STORED.

# CREATING A SET..............................................................................
names = {"Sia","Mia","Kia","Jia","Ria"}
print(names) # ORDER MAY CHANGE EVERYTIME WE PRINT SETS.
print(type(names))

# LENGTH OF SET..............................................................................
print(len(names))

# ACCESSING ITEMS OF SET.....................................................................
for i in names:
    print(i)

# USE OF MEMEBERSHIP OPERATOR................................................................
if "Kia" in names:
    print("Kia is present in names.")    

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# ADDING ITEMS IN SET.......................................................................
names.add("Tia") # Tia WILL BE ADDED ANYWHERE IN THE SET AS SET IS ALWAYS UNORDERED.       
print(names)
names.add("Sia")
print(names) # Sia IS PRESENT ONLY ONE TIME AS DUPLICATES ARE NOT ALLOWED.

# UPDATE(ADDING ANOTHER SEQUENCE IN THE SET)................................................
names_list = ["Pia","Nia"]
names.update(names_list)
print(names)

# REMOVING ITEMS FROM SET...................................................................
# 1) remove() 
names.remove("Jia")
print(names)
'''names.remove("aahana") # Gives error as aahana is not present 
print(names)'''
# 2) discard()
names.discard("Pia")
print(names)
names.discard("aahana")
print(names) # Doesnot throw error( as in case of remove() ) even if aahana is not present in names. 

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# JOINING TWO SETS.........................................................................
s1 = {"a","b","c","d","e","f"}
s2 = {"f","g","h","i","j"}
print(s1,s2)
s3 = s1.union(s2) # VARIABLE s3 IS USED AS WE ARE NOT ADDING OR CHANGING ELEMENTS IN s1. JUST ADDING s1 AND s2.
print(s3) 
# ------------------------------------------------
s1.update(s2) # HERE UPDATION(operation) IS DONE IN s1 . SO NO NEED OF NEW VARIABLE. REFER LINE 27 FOR update().
print(s1)
# ------------------------------------------------
# KEEPING ONLY DUPLICATES WHILE JOINING-----------
print(s1)
print(s2)
print(s3)
s1.intersection_update(s2) 
print(s1) # PRINTS DUPLICATES(same) VALUES OF s1 AND s2 AND UPDATES SET s1.
l1 = {9,46,2,83,9}
l2 = {8,37,2,46,9,87,40}
l3 = l1.intersection(l2)
print(l3) # HERE WE HAVE USED A NEW VARIABLE l3 FOR STORING DUPLICATE VALUES OF l1 AND l2.
# ------------------------------------------------
# KEEPING ALL VALUES EXCEPT DUPLICATES WHILE JOINING-----------
s4 = {1,2,8,5,3,9}
s5 = {3,4,8,1,7,0}
s4.symmetric_difference_update(s5) # UPDATES SET s4.
print(s4)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# QUESTION IS : GIVEN THREE ARRAYS , WE HAVE TO FIND COMMON ELEMENTS IN THREE SORTED LISTS USING SETS. 
# EXAMPLES : ar1 = [1,5,5] , ar2 = [3,4,5,5,10] ,ar3 = [5,5,10,20]
# Output : [5]
ar1 = [1,5,10,20,40,80]
ar2= [6,7,20,80,100]
ar3 = [3,4,15,20,30,70,80,120]
ar4 = set(ar1)
ar5 = set(ar2)
ar6 = set(ar3)
print("Original arrays are :\n" , ar1 ,"\n", ar2 ,"\n" , ar3)
ar4.intersection_update(ar5)
ar4.intersection_update(ar6)
print("Common arary of all these three array is :\n" , list(ar4))
