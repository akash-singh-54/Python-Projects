a = eval(input("Input number: "))
b = input("Enter operator: +, - , *, /\n%, //, ^\nC, CE:- \n")


while (b != "CE"):
    c = eval(input("Input number: "))
    if(b == "+"):
        a = a +c
        b = input("Enter operator: +, - , *, /\n%, //, ^\nC, CE:- \n")
    elif(b == "-"):
        a = a -c
        b = input("Enter operator: +, - , *, /\n%, //, ^\nC, CE:- \n")
    elif(b == "*"):
        a = a *c
        b = input("Enter operator: +, - , *, /\n%, //, ^\nC, CE:- \n")
    elif(b == "/"):
        a = a /c
        b = input("Enter operator: +, - , *, /\n%, //, ^\nC, CE:- \n")
    elif(b == "%"):
        a = a %c
        b = input("Enter operator: +, - , *, /\n%, //, ^\nC, CE:- \n")
    elif(b == "//"):
        a = a //c
        b = input("Enter operator: +, - , *, /\n%, //, ^\nC, CE:- \n")
    elif(b == "^"):
        a = a **c
        b = input("Enter operator: +, - , *, /\n%, //, ^\nC, CE:- \n")
    elif(b == "C"):
        a = 0
        a = eval(input("Input number: "))
        b = input("Enter operator: +, - , *, /\n%, //, ^\nC, CE:- \n")
    else:
        break

print(a)
