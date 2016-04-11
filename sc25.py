sc=open("d:/!!TO CHECK/sc.txt","w")
for i in range(1000):
 #print("{:0>4}".format(i))
 sc.write(str("{:0>4}".format(i))) #4 digits ex. 0002
 sc.write("\n")
sc.close()

