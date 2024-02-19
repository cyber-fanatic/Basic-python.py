MULTIPLICATION TABLES:

a=int(input("Enter a Numer of table,that you want to learn: "))
for b in range(1,16):
    print(a,"x",b,"=",a*b)

CHECK NUMBER EVEN OR ODD:

num=float(input("Enter any number:>>>>"))
if num%2==0:
    print("Number",num,"is Even.")
else:
    print("Number",num,"is Odd.")

(DMAS) CALCULATOR:

print("\t\tDMAS CALCULATOR !")
op=input("which operation you want to perform ------>(/,*,+,-)=>")
if op=="/":
    print("\tYou choose Division:")
    num_1=float(input("enter a num1: "))
    num_2=float(input("enter a num2: "))
    print("\n\t\tThe result is ------>",float(num_1/num_2))
elif op=="*":
    print("\tYou choose Multiplication:")
    num_1=float(input("enter a num1: "))
    num_2=float(input("enter a num2: "))
    print("\n\t\tThe result is ------>",float(num_1*num_2))
elif op=="+":
    print("\tYou choose Addition:")
    num_1=float(input("enter a num1: "))
    num_2=float(input("enter a num2: "))
    print("\n\t\tThe result is ------>",float(num_1+num_2))
elif op=="-":
    print("\tYou choose subtraction:")
    num_1=float(input("enter a num1: "))
    num_2=float(input("enter a num2: "))
    print("\n\t\tThe result is ------>", float(num_1-num_2))
else:
    print("\t<<<<< Oops!!! invalid Choice >>>>>")
