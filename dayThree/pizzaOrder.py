print("Thank you for choosing Python Pizza Deliveries!")
print("What Size Do You Want? S,M,L available")
size = input() # What size pizza do you want? S, M, or L
print("Do you want to add pepperoni? Y for YES N for NOT")
add_pepperoni = input() # Do you want pepperoni? Y or N
print("Do you need extra chesee? Y for YES N for NOT")
extra_cheese = input() # Do you want extra cheese? Y or N
# ? Don't change the code above ?
# Write your code below this line ?
 
bill = 0
if size == "S":
  bill +=15
elif size == "M":
  bill +=20
else:
  bill +=25
if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else :
    bill += 3
if extra_cheese == "Y":
  bill +=1
 
print(f"Your final bill is: ${bill}.")