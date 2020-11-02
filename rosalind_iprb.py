data = open("rosalind_iprb.txt","r")
text = data.read()
x=int(text.split(" ")[0]) #AA
y=int(text.split(" ")[1]) #Aa
z=int(text.split(" ")[2]) #aa
total=x+y+z
geno_find=["AA","Aa"]

x_buff=x
y_buff=y
z_buff=z
total_buff=total
prop1_z=z/total
z_buff-=1
total_buff-=1
prop_zx=(x_buff/total_buff)*prop1_z
prop_zy=(y_buff/total_buff)*prop1_z
prop_zz=(z_buff/total_buff)*prop1_z


x_buff=x
y_buff=y
z_buff=z
total_buff=total
prop1_x=x/total
x_buff-=1
total_buff-=1
prop_xx=(x_buff/total_buff)*prop1_x
prop_xy=(y_buff/total_buff)*prop1_x
prop_xz=(z_buff/total_buff)*prop1_x

x_buff=x
y_buff=y
z_buff=z
total_buff=total
prop1_y=y/total
y_buff-=1
total_buff-=1
prop_yx=(x_buff/total_buff)*prop1_y
prop_yy=(y_buff/total_buff)*prop1_y
prop_yz=(z_buff/total_buff)*prop1_y

#prop_xx
#prop_yy
#prop_zz
prop_xy+=prop_yx
prop_xz+=prop_zx
prop_yz+=prop_zy


geno_xx=["AA"]
geno_yy=["AA","Aa","Aa","aa"]
geno_zz=["aa"]
geno_xy=["AA","Aa"]
geno_xz=["Aa"]
geno_yz=["Aa","aa"]
t=0
for i in range(len(geno_find)):
	
	t+=(geno_xx.count(geno_find[i])/len(geno_xx))*prop_xx
	t+=(geno_yy.count(geno_find[i])/len(geno_yy))*prop_yy
	t+=(geno_zz.count(geno_find[i])/len(geno_zz))*prop_zz
	t+=(geno_xy.count(geno_find[i])/len(geno_xy))*prop_xy
	t+=(geno_xz.count(geno_find[i])/len(geno_xz))*prop_xz
	t+=(geno_yz.count(geno_find[i])/len(geno_yz))*prop_yz

print (t)
		