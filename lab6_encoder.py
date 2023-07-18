# Kayla Willman
# Encoder for lab6


def encode(password):
    # print("1. Encode the password \n2. Decode the password")
    # user_choice = int(input("Encode or Decode (1 or 2): "))
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


def decode(new_pass):
    dec_password = ''

    for i in new_pass:
        if i == '0':
            i='7'
            dec_password = dec_password + i
        if i == '1':
            i='8'
            dec_password = dec_password + i
        if i == '2':
            i='9'
            dec_password = dec_password + i
        if i == '3':
            i='0'
            dec_password = dec_password + i
        if i == '4':
            i='1'
            dec_password = dec_password + i
        if i == '5':
            i='2'
            dec_password = dec_password + i
        if i == '6':
            i='3'
            dec_password = dec_password + i
        if i == '7':
            i='4'
            dec_password = dec_password + i
        if i == '8':
            i='5'
            dec_password = dec_password + i
        if i == '9':
            i='6'
            dec_password = dec_password + i
    return dec_password


def main():
    while True:
        print("Menu")
        print('-------------')
        print("1. Encode \n2. Decode \n3. Quit")
        print()
        user_choice = int(input("Please enter an option: "))
        if user_choice == 1:
            password = str(input("Please enter your password to encode: "))
            new_pass = encode(password)
            print('Your password has been encoded and stored!')
            print()
        elif user_choice == 2:
            orig_password = decode(new_pass)
            print('The encoded password is', new_pass, ', and the original pasword is', orig_password + '.')
        elif user_choice == 3:
            break

if __name__ == '__main__':
    main()
