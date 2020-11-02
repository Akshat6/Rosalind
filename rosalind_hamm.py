data = open("rosalind_hamm.txt","r")
text=data.read()
print(text)
line1=text.split("\n")[0]
line2=text.split("\n")[1]

c=0
for i in range(len(line1)):
	if(line1[i]!=line2[i]):
		c+=1
print (c)