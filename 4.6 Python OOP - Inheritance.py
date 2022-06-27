
class Animal():

    def __init__(self):
        
        self.tipe = "Mamalia"
        self.kecepatan = "lambat"

    def grow(self):
        print("Mamalia ini bertumbah...")

class Cat(Animal):

    def __init__(self, nama, tipe):
        
        super().__init__()

        self.nama = nama
        self.tipe = tipe

    def run(self):
        print(f"Kucing ini berlari...")

kinako = Cat(nama="Kinako", tipe="Persia")

print(kinako.kecepatan)
print(kinako.tipe)

kinako.run()
kinako.grow()