def min_digit(list):
    for i in range (0,len(list)):
        for j in range (i,len(list)):
            if (list[i]>list[j]):
               list[j],list[i]=list[i],list[j]

    return list

s=[]
k=1
def m_d(List):
    global s
    global k
    for i in range (k, len(List)):
        if(List[k-1],List[i]):
            List[k-1],List[i]=List[i],List[k-1]
    
    s.append(List[k-1])
    k=k+1
    if (k<len(List)):
        return m_d(List)
    else:
        return List





    #l = len(list)
    #for i in range(l):
     #   for j in range(l-i-1):
      #      if list[j]>list[j+1]:
       #         list[j],list[j+1]=list[j+1],list[j]
    #return list

print(m_d([3,5,6,2,1]))

