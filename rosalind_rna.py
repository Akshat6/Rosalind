
def transcribe():
	data=open("rosalind_rna.txt","r")
	s=data.read()
	return(s.replace('T','U'))

print(transcribe())