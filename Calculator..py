print("welcome to calculator made by Aarush")
# print ("Select an operation (1/2/3/4/5/)")
#show menu 
print("1. +")
print("2. -")
print("3. /")
print("4. *")
choice = input("Enter choice (1/2/3/4/5): ")
# working of operations
if choice in ('1', '2', '3', '4',):
            try:
                First  = float(input("Enter first number: "))
                second = float(input("Enter second number: "))  
            except ValueError:
                print("Invalid input! Please enter numbers.")
                print('please Retry')

# working of fuction
if choice ==  "1":
    print("The value of your no. in Addition")          
    print( int(First) + int(second) )
elif choice == "2":
    print("The value of your no. in Subtraction")
    print( int(First) - int(second) )
elif choice == "3":
    print("The value of your no. in Division")
    print( int(First) / int(second) )
elif choice == "4":
    print("The value of your no. in Percentage")
    print( int(First) * int(second) )
else:
    print()
