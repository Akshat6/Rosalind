data = open("rosalind_fib.txt","r")
text=data.read()
t=text.split(' ')
print (t)
rabits_prev=0
rabits_pres=1
gen=int(t[0])
rate=int(t[1])
for i in range(gen-1):
	buff=rabits_prev
	rabits_prev=rabits_pres
	rabits_pres+=rate*buff
print(rabits_pres)