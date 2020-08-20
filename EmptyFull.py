def countList(full, empty): 
    return [sub[item] for item in range(len(empty)) 
                      for sub in [full,empty]] 
glass=list(map(str,input().split()))
full=[]
empty=[]
for i in range(0,len(glass)):
  if(glass[i]=='J'):
    full.append(glass[i])
  else:
    empty.append(glass[i])
print(*countList(full,empty))
