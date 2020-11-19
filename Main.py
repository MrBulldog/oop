class Employee:
    ''' Dasar kelas untuk semua karyawan '''
    jumlah_karyawan = 0


    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji
        Employee.jumlah_karyawan += 1

    def tampilkan_jumlah(self):
        print("Total karyawan : ", Employee.jumlah_karyawan)


    def tampilkan_profile(self):
        print("Nama :", self.nama)
        print("Gaji :", self.gaji)
        print()
