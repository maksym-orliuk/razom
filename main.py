from package import Package
from package_registry import PackageRegistry


p_r = PackageRegistry()
p1 = Package('p1')
p2 = Package('p2')
p3 = Package('p3')
p4 = Package('p4')
p5 = Package('p5')
p6 = Package('p6')

p1.add_dependency(p2)
p2.add_dependency(p3)

p2.add_dependency(p4)
p3.add_dependency(p4)

p4.add_dependency(p5)
p6.add_dependency(p3)

p_r.install_package(p1)
# p_r.install_package(p6)
print(p_r._packages)

p_r.remove_package(p1)
p_r.remove_package(p6)
print(p_r._packages)