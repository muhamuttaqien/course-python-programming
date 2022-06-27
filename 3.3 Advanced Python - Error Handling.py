# logical error

class ValueTooSmallError(Exception):
    pass

class ValueTooLargeError(Exception):
    pass

number = 10

while True:

    try:
        i_num = int(input('Masukan angka: '))

        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError

        break
        
    except ValueTooSmallError:  
        print("Angka yang kamu tebak terlalu kecil, coba lagi!")
    except ValueTooLargeError:
        print("Angka yang kamu tebak terlalu besar, coba lagi!")

print("Betul! Kamu berhasil menebak dengan tepat.")