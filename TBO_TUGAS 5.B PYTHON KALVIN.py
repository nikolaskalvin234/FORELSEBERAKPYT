#.TUGAS 5.B - Kuliah TBO
#.DOSEN = Arnes Y.V, M.Kom
#. FOR...ELSE....BREAK
print("NAMA = NIKOLAS KALVIN");
print("NPM = 21421002");
#

listKota = [
    'Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo',
    'Jogjakarta', 'Semarang', 'Makassar'
]

kotaYangDicari = input('Ketik nama kota yang kamu cari: ')

for i, kota in enumerate(listKota):
    # kita ubah katanya ke lowercasw agar
    # menjadi case insensitive
    if kota.lower() == kotaYangDicari.lower():
      print('Kota yang anda cari berada pada indeks', i)
      break
else:
   print('Maaf, kota yang anda cari tidak ada, coba lagi ya')