class Employee:
    ''' Dasar kelas untuk semua karyawan '''
    jumlah_karyawan = 0


    def __init__(self, nama, gaji, telepon):
        self.nama = nama
        self.gaji = gaji
        self.telepon = telepon
        Employee.jumlah_karyawan += 1

    def tampilkan_jumlah(self):
        print("Total karyawan : ", Employee.jumlah_karyawan)


    def tampilkan_profile(self):
        print("Nama :", self.nama)
        print("Gaji :", self.gaji)
        print("Telepon :", self.telepon)
        print()

# Membuat objek pertama dari kelas Karyawan
employee1 = Employee("Mimi", 5000000, "085691119221")
# Membuat objek pertama dari kelas Karyawan
employee2 = Employee("Yousef", 1000000, "082141411345")


#employee1.tampilkan_profile()
#employee2.tampilkan_profile()
print("Total Karyawan: ", Employee.jumlah_karyawan)
print("Karyawan.__doc__: ", Employee.__doc__)
print("Karyawan.__dic: ", Employee.__dict__)
print("Karyawan.__bases__:", Employee.__bases__)

print(100*"=")