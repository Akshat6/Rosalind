import os
data=os.path.basename(__file__).split(".")[0]+".txt"
text=open(data,"r").read()
print(text)
nu,no=text.split("/n")[0],text.split("/n")[1]
for i in range(len(nu)):
    buff=str(nu[i])
    for j in range(no-1):
        buff+=str(nu[j])
    print(buff)

