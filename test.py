n=int(input())
contact={}

for i in range(n):
    a=input().split()
    contact.update({a[0]: a[1]})
   
for i in range(n):
    s = input()
    
    if s in contact:
        print(s + "=" +contact[s])
    else:
        print('Not found')