# f=open("people.txt")
# f=f.read()
# print(f)

# f=open("maggie.txt","r")
# a=f.read()
# s=1
# for i in a:
#     s=s+1
# print(s)



























# f=open("maggie.txt")
# a=f.read()
# s=0
# for i in a:
#     s=s+1
# print(s)

f=open("question4.txt","r")
for i in f:
    if "delhi" in  i :
        f=open("delhi.txt","a")
        f.write(i)
    elif "shimla" in i:
        f=open("shimla.txt","a")
        f.write(i)
    else:
        f=open("others.txt","a")
        f.write(i)        

# f=("maggie.txt","r")
# i=0
# while i<len(f):
#     if "delhi" in  i :
#         f=open("delhi1.txt","a")
#         f.write(i)
#     elif "shimla" in i:
#         f=open("shimla1.txt","a")
#         f.write(i)
#     else:
#         f=open("others1.txt","a")
#         f.write(i)    
#     i=i+1        



