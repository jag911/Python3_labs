import getpass

master_pin = '1234'

pin = None
count = 0

while pin != master_pin:
    if count < 3:
        pin = getpass.getpass("Please enter 4 digit PIN: ")
        count += 1
        if len(pin) == 4 and pin.isdecimal() and pin == master_pin:
            print("Vault Unlocked")
        else:
            print("Invalid PIN")
    else:
        print("Account LOCKED")
        break
    
print("Done...")