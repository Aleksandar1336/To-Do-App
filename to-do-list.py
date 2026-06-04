import database

database.show_all()

while True:
    print("\nCommands:")
    print("create <note>")
    print("delete <id>")
    print("delete all")
    print("quit")
    command = input("\n> ")

    if command.startswith("create "):
        note = command[7:]
        database.add_one(note)
        database.show_all()

    elif command.startswith("delete all"):
        database.delete_all()
        database.show_all()

    elif command.startswith("delete "):
        note_id = int(command[7:])
        database.delete_one(note_id)
        database.show_all()

    elif command == "quit":
        break

    else:
        print("Commands:")
        print("create <note>")
        print("delete <id>")
        print("delete all")
        print("quit")
