# razom

This is a tool for emulating package managing.
With this tool you can install, remove packages, 
create dependencies between them and to list all installed 
packages.

## Usage
for usage this tool you need to run cli_reader.py as script.
Just type into the terminal the next:

*python main.py*

It will allows you to type some commands and afer that to execute it.


This tool supports the next commands:


**DEPEND** *PACKAGE1 PACKAGE2 [PACKAGE3 ...]*

Command for creating dependencies between packages

**EXAMPLE**

***DEPEND DNS TCPIP TELNET***

it will make package DNS depended on TCPIP and TELNET


**INSTALL** *PACKAGE1  [PACKAGE2 ...]*

Command for installing packages. It also installs dependecies for the package 

**EXAMPLE**

***INSTALL DNS***

it will install package DNS and it's dependencies TCPIP and TELNET

**REMOVE** *PACKAGE1  [PACKAGE2 ...]*

Command for uninstalling packages. It also removes dependecies for the package if this packages are not dependencies for other packages

**EXAMPLE**

***REMOVE DNS***

it will install package DNS and it's dependencies (if it's possible)

**LIST**

Command for listing all installed packages

**EXAMPLE**

***INSTALL DNS***

it will install package DNS and it's dependencies TCPIP and TELNET

**END**

Command executes all typed commands

**EXAMPLE**

***END***

it will start to run all your commands




#### NOTE: this tool has a little bit different output from provided, but functionality is working properly.