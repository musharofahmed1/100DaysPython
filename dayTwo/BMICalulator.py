# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
convert_height = float(height)
convert_weight = float(weight)
BMI = convert_weight / convert_height**2
print(int(BMI))