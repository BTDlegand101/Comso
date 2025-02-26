import base64

filename = "save.txt"
registers = {}

commands = {
    "help": "Shows all commands",
    "list": "Lists all registers",
    "read": "Reads a register",
    "create": "Creates a register",
    "delete": "Deletes a register",
    "exit": "Exits the program"
}

def help():
    print("")
    print("Commands:")
    for command in commands:
        print(f"{command}: {commands[command]}")
    print("")

def save(filename):
    with open(filename, 'w') as file:
        for name, number in registers.items():
            encoded_line = base64.b64encode(f"{name}:{number}".encode()).decode()
            file.write(f"{encoded_line}\n")

def load(filename):
    global registers
    try:
        with open(filename, 'r') as file:
            registers = {}
            for line in file:
                decoded_line = base64.b64decode(line.strip()).decode()
                name, number = decoded_line.split(':')
                registers[name] = float(number)
    except FileNotFoundError:
        print(f"No saved numbers found in {filename}")

def list_registers():
    for name, number in registers.items():
        print(f"{name}: {number}")

def create():
    name = input("Enter register name: ")
    value = float(input("Enter register value: "))
    registers[name] = value

def read():
    name = input("Enter register name: ")
    if name in registers:
        print(f"{name}: {registers[name]}")
    else:
        print("Register not found")

def delete():
    name = input("Enter register name: ")
    if name in registers:
        del registers[name]
    else:
        print("Register not found")