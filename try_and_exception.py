print("<<<<< PROGRAM PEMBAGIAN >>>>>")

while True:
    try:
        penyebut = int(input("Masukkan penyebut: "))
        pembilang = int(input("Masukkan pembilang: "))
        hasil = penyebut/pembilang
        break
    except ValueError:
        print("Yang anda masukkan bukan merupakan angka!")
    except ZeroDivisionError:
        print("Maaf, pembilang tidak boleh sama dengan 0")
    # except Exception as error:
    #    print(error) # <-- Exception as error menunjukkan jenis error

print("Hasil pembagian adalah",hasil)

"""
   Type of exception errors:
   1. I0Error
   2. ImportError (mengimport modul yang belum di-install)
   3. ValueError
   4. ZeroDivisionError
   5. KeyboardInterupted
   6. E0FError
"""
