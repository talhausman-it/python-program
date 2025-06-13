# Simple login system
correct_password = "OpenAI123"

# Ask user to input password
entered_password = input("Enter your password: ")

# Check if the password is correct
if entered_password == correct_password:
    print("✅ Access granted. Welcome!")
else:
    print("❌ Access denied. Incorrect password.")
