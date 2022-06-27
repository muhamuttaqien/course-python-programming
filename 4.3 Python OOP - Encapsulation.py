class Mobil:

    def __init__(self, plat):

        self.__plat = plat
        self.__tipe = "Avanza"
        self.__bensin = 40 # liter

    def lihatMaksimumBensin(self):
        print(f"Maksimum bensin yaitu: {self.__bensin}")

    def aturMaksimumBensin(self, bensin):
        self.__bensin = bensin


avanza = Mobil("B 7185 XC")
# avanza.lihatMaksimumBensin()

avanza.aturMaksimumBensin(100)
avanza.lihatMaksimumBensin()