import random
from libs import welcome_message

cuypy_position = random.randint(1, 4)

welcome_message("SELAMAT DATANG DI CUYPY")

nama_user = input("masukan nama kamu: ")

while nama_user == "":
    nama_user = input("isi dulu nama anda: ")

bentuk_goa = "|_|"
goa_kosong = [bentuk_goa] * 4 # INI TETEP HARUS KOSONG

goa = goa_kosong.copy() # INI ADALAH TEMPAT BARU UNTUK SI CUYPY
goa[cuypy_position - 1] = "|0_0|"

goa_kosong = ' '.join(goa_kosong)
goa = ' '.join(goa)


while True:
    print(f'''
    Halo {nama_user}! Coba perhatikan goa dibawah ini  
    {goa_kosong}
    ''')

    pilihan_user = int(input("Menurut kamu di goa nomor berapa CUYPY berada? [1 / 2 / 3 / 4]: "))

    confirm_answer = input(f"apakah kamu yakin jawabannya adalah {pilihan_user}? [y/n]: ")

    if confirm_answer == "n":
        print("program dihentikan!")
        exit()
    elif confirm_answer == "y":
        if pilihan_user == cuypy_position:
            print(f"\n{goa}\n\nSelamat Kamu Menang 🏆")
        else:
            print(f"\n{goa}\n\nUncchhh kamu kalah 🙊")
    else:
        print("Silahkan ulangi programnya!")
        exit()
        
    play_again = input("\n\napakah ingin melanjutkan gamenya lagi? [y/n]")
    if play_again == "n":
        break
    
print("program selesai!")