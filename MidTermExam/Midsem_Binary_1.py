def binary(m):
    x=m//2
    y=str(m%2)
    if x==0 and y=='1':
        return '1'
    else:
            return binary(x)+str(y)
        
print(binary(16))