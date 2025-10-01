l1=[4,3,3,5,6,7,7,7]
l2=[2,3,4,6,7,7,7,3,9,11,13]
l3=[7,9,11,2,3,4,5,7,6]

L=[]
S=[]
L.append(l1)
L.append(l2)
L.append(l3)
#print(L)

for i in L[0]:
    c=0
    for j in range(1,len(L)):
        if i in L[j]:
            L[j].remove(i)
            c+=1
    if (c==len(L)-1):
        S.append(i)
print(S)
    


#ins=[]
#for i in range(0,len(l1)):
#    c=l1[i]
#    if c not in l2 and c not in l3:
#        l3.remove(c)
#        l2.remove(c)
#    else:
#        ins.append(c)

#print(ins)