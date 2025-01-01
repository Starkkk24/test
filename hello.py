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
wrd="".join(wrd_l) 
print(wrd)
random.shuffle(wrd_l)
wrdd="".join(wrd_l)
print(wrdd)

