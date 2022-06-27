class Employee():
    '''
    Ini adalah class untuk memanipulasi data employee
    Melalui kelas ini kita bisa memanipulasi data yang ada seperti baca, hapus dan tambah
    '''

    def __init__(self, lokasi_file):
        
        self.data_employee = open(f'{lokasi_file}', mode='r', encoding='utf-8')
        self.data_per_sesi = 10

    def baca_data(self):
        pass

    def hapus_data(self):
        pass

    def tambah_data(self):
        pass

it = Employee(lokasi_file='./karyawan_IT.xls')
marketing = Employee(lokasi_file='./karyawan_marketing.xls')
product = Employee(lokasi_file='./karyawan_product.xls')

class RandomForest():
    pass