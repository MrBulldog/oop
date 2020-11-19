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

# Membuat objek pertama dari kelas Karyawan
employee1 = Employee("Mimi", 5000000)
# Membuat objek pertama dari kelas Karyawan
employee2 = Employee("Yousef", 10000000)

employee1.tampilkan_profile()
employee2.tampilkan_profile()
print("Total Karyawan: ", Employee.jumlah_karyawan)