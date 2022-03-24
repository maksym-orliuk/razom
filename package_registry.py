from package import Package


class PackageRegistry:
    def __init__(self):
        self._packages = {}

    def install_package(self, package: Package):
        if package.dependencies:
            for dependency in package.dependencies:
                print(f'{package.name} package depends on: {package.dependencies}')
                print(f'Installing {package.name} package dependencies...')
                self.install_package(package.dependencies[dependency])
        self._packages[package.name] = package
        print(f'{package} successfully installed!')

    def remove_package(self, package):
        if package.name not in self._packages:
            print(f'{package} is not installed')
        elif package.depended_packages:
            print(f"Can't delete {package} because of depended packages: {package.depended_packages}")
        else:
            self._packages.pop(package.name)
            for dependency in package.dependencies.values():
                dependency.depended_packages.pop(package.name)
                if not dependency.depended_packages:
                    print(f'{dependency} will be also removed because its no longer needed by any package')
                    self.remove_package(dependency)
                print(f'{package} has been removed!')

    def list_packages(self):
        return self._packages.keys()
