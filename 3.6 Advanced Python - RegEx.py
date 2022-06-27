import re

teks = "regex"
x = re.match("^r...x$", teks)
print(x)

teks = "saya senang belajar regex"
x = re.split("\s", teks)
print(x)

teks = """
        Ada 3 tipe loop atau perulangan di bahasa pemrograman Python yaitu while loop, 
        for loop dan nested loop 2022
       """

x = re.sub("\d+", "", teks)
print(x)

teks = "Hujan deras di kawasan depok"
result = re.search("^Hujan.*depok$", teks)
if result:
    print("YES! We have a match.")
else:
    print("No match.")

teks = "23 oct 2019 23 oct,2019 23 october,2019 oct 26,2020"
x = re.findall("\d{2} [a-z]{3} \d{4}", teks)
print(x)

teks = "Harga 1 mobil antik tersebut yaitu $1000"
x = re.sub("\$\d+", "_", teks)
print(x)

teks = "Akan dialihkan ke http://medium.com"
x = re.sub("http[s]?\://\S+", "_", teks)
print(x)

teks = "Luar biasa! Banyak anak-anak muda traveling tahun ini, begini tanggapan lesti #travel #_lesti #viral #gadget"
x = re.findall("#[_]*[a-z]+", teks)
print(x)
