def parse_input(user_input):
    parts = user_input.strip().split()
    if not parts:
        return "", []
    cmd = parts[0].lower()
    args = parts[1:]
    return cmd, args


def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command. Usage: add [name] [phone]"
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command. Usage: change [name] [new_phone]"
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."


def show_phone(args, contacts):
    if len(args) != 1:
        return "Invalid command. Usage: phone [name]"
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."


def show_all(contacts):
    if not contacts:
        return "No contacts found."
    lines = [f"{name}: {phone}" for name, phone in contacts.items()]
    return "\n".join(lines)


def main():
    """
    Основний цикл взаємодії бота з користувачем.
    """
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        cmd, args = parse_input(user_input)

        if cmd in ("exit", "close"):
            print("Good bye!")
            break

        elif cmd == "hello":
            print("How can I help you?")

        elif cmd == "add":
            print(add_contact(args, contacts))

        elif cmd == "change":
            print(change_contact(args, contacts))

        elif cmd == "phone":
            print(show_phone(args, contacts))

        elif cmd == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()

