from ui import menu


def start_warung() -> None:
    while True:
        print("ini warung apps!")
        play_again = input("kembali ke menu utama? [y/n] ")

        if play_again == "y":
            menu.menu_program()

