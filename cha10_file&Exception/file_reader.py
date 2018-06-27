file_path = 'test_files\pi_million_digits.txt'
with open(file_path) as file_object:
    # for line in file_object:
    #     print(line.rstrip())
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("yes")
else:
    print("No")
