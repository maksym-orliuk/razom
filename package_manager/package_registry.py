from package import Package


class PackageRegistry:
    """
    It's a package manager allows you to install, remove and list packages.
    """
    def __init__(self):
        self._packages = {}

    def install_package(self, package: Package):
        if package.dependencies:
            print(f'{package.name} depends on {package.dependencies}')
            print(f'Installing {package.name} package dependencies...')

            for dependency in package.dependencies:
                self.install_package(package.dependencies[dependency])

        self._packages[package.name] = package
        print(f'{package} successfully installed!')

    def remove_package(self, package):
        if package.name not in self._packages:
            print(f'{package} is not installed')
        elif package.depended_packages:
            print(f"Can't delete {package} because of depended packages: {list(package.depended_packages.keys())}")
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
