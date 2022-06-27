
# read
data = open('./data.txt', mode='r', encoding='utf-8')
print(data.read())

# append
data = open('./data.txt', mode='a')
data.write('\nYuk belajar bahasa pemrograman Python!') # \n break new line \t tab
data.write('\nAgar jago harus sering berlatih!')
data.close()

# write
data = open('./data.txt', mode='w')
data.write('\nYuk belajar bahasa pemrograman Python!') # \n break new line \t tab
data.write('\nAgar jago harus sering berlatih!')
data.close()

# better practice
try:
    f = open('./data.txt', mode='w', encoding='utf-8')
finally:
    f.close()
    print('File handling telah berhasil.')

# best practice
with open('./data.txt', mode='w', encoding='utf-8') as f:
    # isi instruksi write()
    pass