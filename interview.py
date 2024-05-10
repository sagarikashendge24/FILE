def a():
    b=[1,2,3,4,5,6,7,8,9]
    i=0
    k=b[i]
    l=[]
    while i<len(b):
        d=k+1-k
        l.append(d)
        i=i+1
    print(l)    
a()        
      


# pat=[1,3,2,1,2,3,1,0,1,3]
# for p in pat:
#     pass
#     if (p==0):
#         current=p
#         break
#     elif (p%2==0):
#         continue
#     print(p)
# print(current)    

def sq(num):
    words=str(num) 
    for word in words:
        print(int(word)**2,end="") 
a=int(input("enter"))
sq(a)            

# a=[1,1,2,2,3,3,4,5,2]
# i=0
# while i<len(a):
#     j=0
#     k=0
#     while j<len(a):
#         if a[i]==a[j]==2:
#             k=k+1
#         j=j+1
#     i=i+1
# print(k)            