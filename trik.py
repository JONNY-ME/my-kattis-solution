t=input()
k=1
for i in t:
    if(i=='A'):
        if(k==1):
            k=2
        elif(k==2):
            k=1
    elif(i=='B'):
        if(k==2):
            k=3
        elif(k==3):
            k=2
    elif(i=='C'):
        if(k==3):
            k=1
        elif(k==1):
            k=3
print(k)
