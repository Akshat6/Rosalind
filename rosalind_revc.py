data=open("rosalind_revc.txt","r")
s=data.read()
s1=""
for i in range(len(s)):
	if(s[i]=="A"):
		s1+="T"
	if(s[i]=="T"):
		s1+="A"
	if(s[i]=="G"):
		s1+="C"
	if(s[i]=="C"):
		s1+="G"
s2=""
for i in range(len(s1)-1,-1,-1):
	s2+=s1[i]

print (s2)

	