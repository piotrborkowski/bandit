sc=open("d:/!!TO CHECK/sc.txt","w")
for i in range(1000):
 #print("{:0>4}".format(i))
 sc.write(str("{:0>4}".format(i)))
 sc.write("\n")
sc.close()

