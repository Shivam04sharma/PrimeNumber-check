print("#"*60)
print("*"*60)
print(" "*20,"."*5,"WELCOME","."*5)
print("")
print(" "*12,"Prime Number And Composite Number")
while True:
    print("*"*60)
    print('''>>> Press:
> N or n for entering the range
> I or i for project information
> E or e for exiting the program''')
    print("-"*35)
    com=input("# Enter the command: ")
    if com in "Nn":
        print("-"*60)
        num1=int(input("> Enter the starting value of range: "))
        num2=int(input("> Enter the ending value of range: "))
        if num1>=0 and num2>0 and num2>num1:
            numcount=abs(num2-num1+1)
            n1=num1
            n2=num2
            print("-"*60)
            print("# Prime/Composite-range("+str(n1)+","+str(n2)+")")
            print("-"*35)
            prm=0
            prml=[]
            cmp=0
            cmpl=[]
            ncnp=0
            if num1==0:
                num1=2
                print("> 0 Neither composite nor prime number")
                print("> 1 Neither composite nor prime number")
                ncnp=2
            if num1==1:
                num1=2
                print("> 1 Neither composite nor prime number")
                ncnp=1
            for i in range(num1,num2+1):
                stat="Prime Number"
                for j in range(2,i):
                    if i%j==0:
                        stat="Composite Number"
                print(">",i,stat)
                if stat=="Prime Number":
                    prm=prm+1
                    prml.append(i)
                else:
                    cmp=cmp+1
                    cmpl.append(i)
            print("-"*60)
            print(" "*20,"."*5,"SUMMARY","."*5)
            print("")
            if num2<num1:
                num1,num2=num2,num1
            print("# Prime/Composite-range("+str(n1)+","+str(n2)+")")
            print("# Total Prime Number:",prm)
            print("# Total Composite Number:",cmp)
            print("# Neither composite nor prime:",ncnp)
            print("# Total Number Count:",numcount)
            print("")
            print("# Prime Number List:",prml)
            print("")
            print("# Composite Number List:",cmpl)
            print("")
            print("#"*60)
        else:
            print("-"*60)
            print(" "*20,"! Enter valid range")
    elif com in "Ii":
        print("-"*60)
        print(" "*15,"."*5,"Project Information","."*5)
        print()
        print("> Made by:  Ankit Maurya")
        print("> Section:  K22ER")
        print("> Reg. No.: 12205604")
        print("> Roll No.: A20")
        print("> Course:   Python(Int-108)")
        print("")
        print(">>> Project Description:")
        print('''> This project is programmed to take a range of number and
check for all the prime numbers and composite numbers within
that given range, also count the total number of prime numbers
and composite numbers and display their respective list.
-Prime Number: numbers which are divisible by 1 or itself only
-Composite Number: numbers which have atleast one factor other
than 1 and itself.''')
        print("")
        print("#"*60)
    elif com in "Ee":
        print("-"*60)
        print(" "*15,"."*3,"Thanks, Visit Again","."*3)
        print("#"*60)
        break
    else:
        print("-"*60)
        print(" "*15,"! Invalid Entry, Try Again...")