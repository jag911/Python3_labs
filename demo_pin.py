

master_pin = "0123"
pin = None
count = 0

while pin != master_pin and count < 3:
    pin = input("Enter PIN: ")
    count += 1
    if pin == master_pin:
        print("Valid PIN")
    else:
        print("Invalid PIN")
else:
    print("Too many attempts")
    
print("Done...")