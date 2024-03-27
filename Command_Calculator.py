class calc :
    def Add (self,a,b) :
        print("The summation of this Number is : " + str(a+b))
    def Sub (self,a,b) :
        print("The Subtraction of this Number is : " + str(a-b))
    def Multiply (self,a,b) :
        print("The Multiplication of this Number is : " + str(a*b))
    def Div (self,a,b) :
        print("The Division of this Number is : " + str(a/b))
j = calc()
Command = input("Enter Your Command : ")     
if Command == "Add" :
    a =int (input("Please, Enter First Number : "))
    b =int (input("Please, Enter Second Number : "))
    j.Add(a,b)
elif Command == "Sub" :
    a =int (input("Please, Enter First Number : "))
    b =int (input("Please, Enter Second Number : "))
    j.Sub(a,b)
elif Command == "Multiply" :
    a =int (input("Please, Enter First Number : "))
    b =int (input("Please, Enter Second Number : "))
    j.Multiply(a,b)
elif Command == "Div" :
    a =int (input("Please, Enter First Number : "))
    b =int (input("Please, Enter Second Number : "))
    j.Div(a,b)
else :
    print("Please Try Again")