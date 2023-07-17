# Kayla Willman
# Encoder for lab6


def pw_encoder(password):
    print("1. Encode the password \n2. Decode the password")
    user_choice = int(input("Encode or Decode (1 or 2): "))
    new_pass = ''
    pass_val = 0
    for num in password:
        if int(num) < 7:
            pass_val = int(num) + 3
            new_pass += str(pass_val)
        else:
            pass_val = int(num) - 7
            new_pass += str(pass_val)
    return new_pass


def pw_decoder(password):
    pass


def main():
    password = str(input("Please enter a string of 8 numbers: "))
    print("1. Encode the password \n2. Decode the password")
    user_choice = int(input("Encode or Decode (1 or 2): "))
    if user_choice == 1:
        print(pw_encoder(password))
    elif user_choice == 2:
        pass

if __name__ == '__main__':
    main()
