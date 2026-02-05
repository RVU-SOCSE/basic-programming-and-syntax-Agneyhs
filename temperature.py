#program to find temperature in fahrenheit or celcius
#1RVU25BCA0008
#Agney hs
#section A


print("i.celcius to fahrenheit conversation")
print("i.fahrenheit to celcius conversation")

choice = int(input("enter your choice"))
temp = float(input("enter the temperature"))

match choice:
    case 1:
        fahrenheit = (temp * 9/5)+32
        print("the fahrenheit temperature is ",fahrenheit)
    case 2:
        celcius = (temp - 32)*5/9
        print("the celcius temperature is ",celcius)
    case _:
        print("invalid")
            

    
            
