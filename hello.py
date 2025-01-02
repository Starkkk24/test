import random

lst=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
wrd_l=[]
# i=0
# while i<5:
#     idx=random.randint(0,len(lst))
#     ltr=lst[idx]
#     wrd_l.append(ltr)
#     i += 1
for i in range(0,5):
    idx=random.randint(0,len(lst)-1)
    ltr=lst[idx]
    wrd_l.append(ltr)   
wrd_1="".join(wrd_l) 
print(wrd_1)
random.shuffle(wrd_l)
wrd_2="".join(wrd_l)
print(wrd_2)

# num_1=[]
# for l in wrd_1:
#     x=wrd_1.index(l)
#     num_1.append(x)
# print(num_1)

num_1={}
for l in wrd_1:
    num_1[l]=wrd_1.index(l)
# print(num_1)

num_2=[]
for n in wrd_2:
    num_2.append(num_1[n])
# print(num_2)

nm=[]
for c in num_2:
    d=str(c)
    nm.append(d)
# print(nm)
code="".join(nm)
code=int(code)
# print(code)


cde=int(input("Enter the code here:"))
if cde==code:
    print("verified")
else:
    print("invalid")