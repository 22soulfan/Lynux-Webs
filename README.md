# PyLinux
A basic Linux console made entirely with MicroPython
> Note: PyLinux is still in alpha. Some features are still in development

# What is PyLinux?

PyLinux is a basic and simulated Linux console based on MicroPython. It is a command-line interface console that can be used on any pc and graphical calculator with python installed.

# How to install:

To install PyLinux, you need:

- A graphical calculator or computer with Python linux installed (e.g. Casio FX-CG50)
- Enough storage to install PyLinux

Installing PyLinux is very easy. Download the py. file from the Releases page, then transfer the file to a graphical calculator. Afterwards, open Python there and select PYLINUX.py and voila! You have a Linux console in a calculator!

# FAQs about PyLinux

**Can you login any user in PyLinux?**

Yes of course. You can login lots of accounts. For example, if your name is John, and you type this name in PyLinux login:

```bash

Login: John

```

it will appear in the input:

``` bash
John@pylinux$
```

You can login any user (and even fictional characters.) Bear in mind that if you add a large name (say for example, Jonathan), the console will show this in a graphical calculator:
``` bash
Jonathan@pylinux~
```
Since graphical calculators sometimes have low resolutions, they might see that. To log out a user, simply type this:

``` bash
logoff
```
and it shows this:
``` bash
User guest logoff!
Login:
```

Note that if you log out, everything are erased, like a sandbox console.

**How to install packages?**

To install a package in PyLinux, use this format:

``` bash
bee install <package>
```

Bee is a package installer, which installs local pacakges not yet installed.

However, all packages are loaded automatically and will be enabled by doing this command. Some packages are preinstalled, such as Questa (virtual storage). To check for the package catalog to install, type this:
``` bash
bee catalog
```

You may see a few pacakges, depending on which version you have. Since PyLinux is in alpha, you might see 2 or more packages.

**Can you install a desktop environment?**

No, we don't support these. Since PyLinux is entirely made from MicroPython, you may receive an error message. For example, if you want to install xfce, and you type this:

``` bash
sudo bee install xfce4
```

you would receive this:
``` bash
sudo bee install xfce4: cmd not found
```
That's because desktop environments are made with C++ and other complex programming languages, which PyLinux can't do. If you want a graphical desktop interface, you need to install a real Linux distro instead of PyLinux.

**Is PyLinux like a real Linux console?**

No, it is just a basic console. You cannot try complex commands; they are hard to be coded.

**Is PyLinux open-source?**

Yes, PyLinux is open-source on the MIT License. You can fork it as long as you like or contribute.

**Can you build PyLinux?**

There is no build script to create PyLinux; but if you want to customize it, you can clone the repository. On Linux, type this: 
``` bash
git clone "https://github.com/hirohamada2014/PyLinux.git"
```

Afterwards, you can edit the source code as long as you like.

On Windows, download the source code zip file from the Releases page, then extract it. You can edit the source code if you like.





