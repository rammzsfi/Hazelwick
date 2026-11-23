PIN= input("Enter the pin:")
attempts=1
while PIN != "1234" and attempts < 3:
    attempts=attempts+1
    PIN= input("Enter the pin:")

if attempts >= 3:
    print("Locked out!")
if PIN == "1234":
    print("Access Granted!")
