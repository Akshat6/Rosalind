data = open("rosalind_fibd.txt","r")
text=data.read()
gen=7#int(text.split(" ")[0])
life_span=3#int(text.split(" ")[1])


pres=[]

pres.append(1)
prev=0
prev_=0

for i in range(1,gen):
	if(i-2>=0):
		prev=pres[i-2]
	if(i-3>=0):
		prev_=pres[i-3]
	pres.append(pres[i-1]+prev-prev_)
	

	
print(pres)