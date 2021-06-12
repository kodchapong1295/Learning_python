# #FileNotFound
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["sddsf"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as err_msg:
#     print(f"The key {err_msg} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise KeyError

height = float(input("Height: "))
weight = float(input("Weight: "))

if height>3:
    raise ValueError("Human Height should not over 3 meters.")

bmi = weight/height ** 2
print(bmi)