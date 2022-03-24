from package_manager import CLIReader


cli = CLIReader()
commands = []

## Uncomment this if you want to run commands from the input.txt file

# with open('input.txt') as f:
#     commands = f.readlines()
#
# cli.read_input_commands(commands)


# Comment the code bellow if you want to test the app with commands from file input.txt

if __name__ == '__main__':
    continue_input = True
    while continue_input:
        command = input('ENTER COMMAND: ')
        if command != 'END':
            commands.append(command)
        else:
            continue_input = False

    print('You entered the next commands:')
    for command in commands:
        print(command)
    cli.read_input_commands(commands)
