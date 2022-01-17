a={}
sum=0
while True:
    option=print("A-Add Item\nE-Exit")
    task=input("Please Choose Your Option :".upper())
    if task=="A":
        Item=input("please enter item name :")
        price=float(input("Please enter item price :"))
        a[Item]=price
    elif task=="E":
        print("Thankyou for visiting")
        break
    else:
        print("Invalid Option Selected")
        pass
print("\t","Items List","\t\t","Price Of The Item")
print("\t""-----------------","\t","-----------------------")
for j in a:
    print("\t",j,"\t\t\t\t\t",a[j],"\t")
    sum =(sum+a[j])
print("Total Amount Of Items Is :",sum)
#this is my first project
# local and ec2 users are working here
