from typing import Dict, List, Tuple

from package_registry import PackageRegistry
from package import Package

PACKAGE_STORAGE = {}


class CLIReader:
    def __init__(self):
        self._package_registry = PackageRegistry()

        self._command_to_func_mapping = {
            'DEPEND': self.depend,
            'REMOVE': self.remove,
            'INSTALL': self.install,
            'LIST': self.list
        }

    def install(self, args):
        print(f'INSTALL: {args}')
        for package_name in args:
            package = Package(package_name)
            self._package_registry.install_package(package)

    def depend(self, args):
        print(f'DEPEND: {args}')
        target_package_name = args[0]
        if target_package_name not in PACKAGE_STORAGE:
            PACKAGE_STORAGE[target_package_name] = Package(target_package_name)

        for dependency in args[1:]:
            if dependency not in PACKAGE_STORAGE:
                PACKAGE_STORAGE[dependency] = Package(dependency)
            PACKAGE_STORAGE[target_package_name].add_dependency(PACKAGE_STORAGE[dependency])

    def remove(self, args):
        print(f'REMOVE: {args}')

        for package_name in args:
            self._package_registry.remove_package(PACKAGE_STORAGE[package_name])

    def list(self, args):
        print('LIST:')

        for package in self._package_registry.list_packages():
            print(package)

    @staticmethod
    def _parse_command(command: str):
        command_args = command.split()
        return command_args[0], command_args[1:]

    def read_input_commands(self, commands: List[str]):
        # parsed_commands = List[Tuple[str, List[str]]]
        parsed_commands = [self._parse_command(command) for command in commands]

        for command, args in parsed_commands:
            self._command_to_func_mapping[command](args)


cli = CLIReader()
with open('input.txt') as f:
    commands = f.readlines()

cli.read_input_commands(commands)
