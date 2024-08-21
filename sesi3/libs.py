def welcome_message(title: str) -> None:
    style = "*" * (len(title) + 6)

    print(style)
    print(f"** {title} **")
    print(style)

