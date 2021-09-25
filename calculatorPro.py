import math

print("\t\t\t\tImportant notice\n\nThis is a mini-calculator designed by Khalid Hajilacag\nThe calculator uses its operators as their real symbols except the following:\nUse 'sqrt'for square root, 'power' for power and 'factorial' for factorial numbers")
print("\n\nAuthor information\n-----------------------------------------------")
print("Name: Khalid Mohamed Abdi\nNationality: Somali\nResidence: Bangladesh\nEmail: Khalidhajilacag@gmail.com\nFacebook: Khalid Mohamed Abdi Hajilacag")



try:
     base=int(input("\nEnter a number:"))

except ValueError:
     print("It should be a number.")

op=input("Enter the operator:")


if op=="power":
  pow=int(input("Enter power number:"))
  def exponentMath(base,pow):
     result=1
     for index in range(pow):
        result=result*base
     return result
  print("\n----------------------------")
  print("Result: ",exponentMath(base,pow))

elif op=="+":
   n=int(input("enter second number:"))
   print("\n----------------------------")
   print("Result: ",base + n)
elif op=="-":
   n=int(input("enter second number:"))
   print("\n----------------------------")
   print("Result: ",base - n)
elif op=="*":
   n=int(input("enter second number:"))
   print("\nResult: ",base * n)
elif op=="/":
   n=int(input("enter second number:"))
   print("\n----------------------------")
   print("Result: ",base / n)

#square root part

elif op=="sqrt":
    print("\n----------------------------")
    print("Result: ",math.sqrt(base))

#checking prime number part
elif op=="prime":
    def check(base):
        if base == 1:
            return False

            # from 1 to sqrt(n)
        for x in range(2, (int)(math.sqrt(base)) + 1):
            if n % x == 0:
                return False
        return True

    n=base
    if check(n):
        print("\n----------------------------")
        print("Result: prime")
    else:
        print("\n----------------------------")
        print("Result: not prime")

elif op=="factorial":
    n = base
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i
    print("\n----------------------------")
    print("The factorial is : ", end="")
    print(fact)

elif op=="modulus" or op=="%":
    n = int(input("enter modulus number:"))
    print("\n----------------------------")
    print("Result: ", base % n)

elif op=="log":
    BASE=int(input("enter base number: "))
    print("\n----------------------------")
    print("Result: ",math.log(base,BASE))

else:
    print("invalid")

