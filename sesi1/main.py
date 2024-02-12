import random

welcome_message = "WELCOME TO CUYPY GAMES!"
cuypy_position = random.randint(1, 4)

print("*****************************")
print(f"** {welcome_message} **")
print("*****************************")

nama_user = input("masukan nama kamu: ")

print(f'''
Halo {nama_user}! Coba perhatikan goa dibawah ini  
|_| |_| |_| |_|
''')

pilihan_user = int(input("Menurut kamu di goa nomor berapa CUYPY berada? [1 / 2 / 3 / 4]: "))

if pilihan_user == cuypy_position:
    print("Selamat Kamu Menang!")
else:
    print("Maaf kamu kalah!")