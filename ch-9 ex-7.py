rec=dict()
num=int(input("Enter number of students :"))
i=1
while i<=num:
    name=input("Enter name of students :")
    per=input ("Enter marks% of students :")
    rec[name]=per
    i=i+1
    ls=rec.keys()
print("Name of students","\t","marks%")
for i in sorted(ls,key=rec.get) :
    print("\t",i,"\t\t",rec[i])
    
          
