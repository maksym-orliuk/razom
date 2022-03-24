class Package:
    """
    Package entity.
    """
    def __init__(self, name):
        self.name = name
        self.dependencies = {}
        self.depended_packages = {}

    def add_dependency(self, package):
        self.dependencies[package.name] = package
        package.add_as_depended(self)

    def add_as_depended(self, package):
        self.depended_packages[package.name] = package

    def __str__(self):
        return self.name

    def __repr__(self):
        return \
            f' package: {self.name}\n \
        dependencies: {[dep.name for dep in self.dependencies.values()]}\n \
        depended: {[dep.name for dep in self.depended_packages.values()]}\n\n'

