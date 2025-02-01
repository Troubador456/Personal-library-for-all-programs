import time

# Variables
common_passwords = ["123456", "abcdef", "password"]
min_length = 6

# Get user to enter password
password = input("What is your Password: ")
print("Calculating...")
time.sleep(2)

errors_found = []
# Check for common passwords
if password in common_passwords:
    print("This is a really common password please change")
    errors_found.append("CommonPasswordTest FAILED")
# Check minimum password length
if len(password) < min_length:
    print("Password is Too short")
    errors_found.append("LengthTest FAILED")
# Check If password has special character
if password.isalnum():
    print("Please add a special character for hard to guess password")
    errors_found.append("SpecialCharacterTest FAILED")
if errors_found:
    print(errors_found)
else:
    print("Strong Password")