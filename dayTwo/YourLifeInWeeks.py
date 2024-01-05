age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
week_gone = int(age)*52
week_total = 90*52
week_left = int(week_total) - int(week_gone)
print("You have "+ str(week_left) +" weeks left.")