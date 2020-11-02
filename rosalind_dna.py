data=open("rosalind_dna.txt","r")
text=data.read()

a=g=c=t=0
for s in text:
	if(s=="A"):
		a+=1
	if(s=="G"):
		g+=1
	if(s=="C"):
		c+=1
	if(s=="T"):
		t+=1
print(a,c,g,t)	

