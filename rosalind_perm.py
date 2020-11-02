data = open("rosalind_perm.txt","r")
no=int(data.read())
low=[]
str_low=""
str_high=""

for i in range(no):
    low.append(str(i+1))
    str_low+=str(i+1)

high=low.copy()
high.reverse()
for no in high:
	str_high+=no
poss=[]
for i in range(int(str_low),int(str_high)+1,1):
	flag=0
	str_i=str(i)
	list_i=[]
	for j in range(len(str_i)):
		list_i.append(str_i[j])
	for j in range(len(low)):
		try:
			index=list_i.index(low[j])
		except ValueError:
			flag=1
			break
		
		
			
	if(flag==0):
		poss.append(str_i)
print(len(poss))
string=""
for no in poss:
	string=""
	for j in range(len(no)):
		string+=no[j]
		string+=" "
	print(string)

