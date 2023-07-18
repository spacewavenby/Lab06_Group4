# Kayla Willman
# Encoder for lab6


def encode(password):
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


def decode(enc_password):
    pass


def main():
    while True:
        print("Menu")
        print('-------------')
        print("1. Encode \n2. Decode \n3. Quit")
        print()
        user_choice = int(input("Please enter an option: "))
        if user_choice == 1:
            password = str(input("Please enter your password to encode: "))
            enc_password = encode(password)
            print('Your password has been encoded and stored!')
            print()
        elif user_choice == 2:
            pass
        elif user_choice == 3:
            break

if __name__ == '__main__':
    main()
