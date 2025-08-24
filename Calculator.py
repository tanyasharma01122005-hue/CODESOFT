# firstly we have to define a function  named calculator 
def calculator():
  print("A Simple Calculator")
# Now take input from the user
  number_1=float(input("Enter first number:-")
  number_2=float(input("Enter second number (in case of division not equals to zero):-")
  chooose_operation=input("choose from(+,-,/,*)")
  # Here if and elif and else statement is used 
  if choose_operation=='+':
    result = number_1 + number_2
  elif choose_operation=='-':
    result = number_1 - number_2
  elif choose_operation=='*':
    result = number_1 * number_2
  elif choose_operation=='/':
    result = number_1/number_2
  else:
    result="Invalid Operation!"
   print("Result of operation is:-",result)
# at last calling the function 
calculator()
  

                 
               
  
