import unittest
from package_manager.package_registry import PackageRegistry
from package_manager.package import Package


class TestPackage(unittest.TestCase):
    def test_adding_package(self):
        package_registry = PackageRegistry()
        p1 = Package('p1')
        p2 = Package('p2')
        p3 = Package('p3')

        p1.add_dependency(p2)
        p2.add_dependency(p3)

        package_registry.install_package(p1)

        self.assertIn(p1, package_registry._packages.values())
        self.assertIn(p2, package_registry._packages.values())
        self.assertIn(p3, package_registry._packages.values())

    def test_remove_package(self):
        package_registry = PackageRegistry()
        p1 = Package('p1')
        p2 = Package('p2')
        p3 = Package('p3')

        p1.add_dependency(p2)
        p2.add_dependency(p3)

        package_registry.install_package(p1)
        package_registry.remove_package(p1)
        self.assertNotIn(p1, package_registry._packages.values())
        self.assertNotIn(p2, package_registry._packages.values())
        self.assertNotIn(p3, package_registry._packages.values())

    def test_list_packages(self):
        package_registry = PackageRegistry()
        p1 = Package('p1')
        p2 = Package('p2')
        p3 = Package('p3')

        p1.add_dependency(p2)
        p2.add_dependency(p3)
        package_registry.install_package(p1)
        list_ = package_registry.list_packages()
        self.assertEqual(len(list_), 3)
