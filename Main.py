import Math
import Registers

commands = {
    "help": "Shows all commands",
    "exit": "Exits the program",
    "math": "Enters Mathematical mode",
    "register": "Allows you to change register values"
}

def help():
    print("")
    print("Commands:")
    for command in commands:
        print(f"{command}: {commands[command]}")
    print("")

print("\nWelcome to Cosmo!")
print("Type 'help' for a list of commands\n")

while True:
    main = input("<Cosmo> ")
    if main == "help":
        help()
    elif main == "exit":
        break
    elif main == "math":
        print("Math mode activated")
        while True:
            action = input("Enter equation: ")
            if action == "exit":
                print("Math mode deactivated")
                break
            elif action == "list":
                Math.list_ops()
            else:
                Math.setup(action)
                Math.calculate()
    elif main == "register":
        print("Register mode activated")
        Registers.load(Registers.filename)
        while True:
            action = input("Enter register action: ")
            if action == "help":
                Registers.help()
            elif action == "list":
                Registers.list_registers()
            elif action == "read":
                Registers.read()
            elif action == "create":
                Registers.create()
            elif action == "delete":
                Registers.delete()
            elif action == "exit":
                Registers.save(Registers.filename)
                print("Registers saved")
                print("Register mode deactivated")
                break
    else:
        print("Invalid command")

print("Program exited")