#BMI calculator 

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#convert input to float
f_height = float(height)
f_weight = float(weight)

#caluculate BMI
BMI = f_weight / f_height ** 2
print(int(BMI))
