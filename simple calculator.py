#progarm of simple calculator.
#USN:1RVU25BCA0008
#Name:Agney hs
#section A


a = int(input("Enter the a value"))
b = int(input("enter the b value"))

operator = input("enter the operator")

match operator:
    case "+":
        print("result is",a + b)
    case "-":
        print("result is",a - b)
    case "*":
        print("result is",a * b)
    case "/":
        print("result is",a / b)
    case "%":
        print("result is",a % b)
    case _:
        print("error")
         
