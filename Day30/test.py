# try:
# 	# try to open the file and access the key in the dict
# 	file = open("file.txt", "r")
# 	a_dict = {"key": "value"}
# 	# print(a_dict["key_2"])
# except FileNotFoundError:
# 	file = open("file.txt", "w")
# 	file.write("Something")
# except KeyError as error_message:
# 	print(f"The key {error_message} does not exist")
# else:
# 	# if the try block happened with no errors then run this code
# 	content = file.read()
# 	print(content)
# finally:
# 	# run regardless of if any exceptions raised or not
# 	file.close()

height = float(input("Height in meters:"))
weight = int(input("Weight in pounds:"))

# get the users height and weight and if the height is over 3 meters then give an error
if height > 3:
	raise ValueError("Human Height does not exceed 3 meters")

bmi = weight / height ** 2
print(bmi)