import socket
from games import cuypy
from tools import warung
from time import sleep

PC_NAME = socket.gethostname()


def welcome_message() -> None:
    style = "*" * (len(PC_NAME) + 6)

    print(style)
    print(f"** {PC_NAME} **")
    print(style)


def exit_program() -> None:
    print("program akan dihentikan")
    sleep(1)
    print("3...")
    sleep(1)
    print("2...")
    sleep(1)
    print("1...")
    sleep(1)
    print("program berhasil dihentikan")


def menu_program() -> None:
    user_option = int(
        input(
            f"menu program:\n1. Games CUYPY\n2. Warung Mini\n3. keluar program\n\nsilahkan pilih: "
        )
    )

    if user_option == 1:
        cuypy.start()
    elif user_option == 2:
        warung.start_warung()
    elif user_option == 3:
        exit_program()
        exit(1)
    else:
        print("hanya boleh pilih yang tersedia di menu!")
