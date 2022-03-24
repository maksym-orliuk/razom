import unittest
from package_manager.package import Package


class TestPackage(unittest.TestCase):
    def test_adding_dependency(self):
        p1 = Package('p1')
        p2 = Package('p2')
        p3 = Package('p3')

        p1.add_dependency(p2)
        p2.add_dependency(p3)

        self.assertIn(p2.name, p1.dependencies)
        self.assertIn(p3.name, p2.dependencies)

        self.assertIn(p1.name, p2.depended_packages)
        self.assertIn(p2.name, p3.depended_packages)
