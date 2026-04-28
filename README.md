# Lynux Webs
A basic Linux console based on PyLinux.
> Note: I'm adding feature to PyLinux with this fork so that it can act like an interactive CLI distro.

# What is Lynux Webs?

Lynux Webs is a basic and simulated Linux console based on MicroPython. It is a command-line interface console that can be used on any pc and graphical calculator with python installed.

# How to install:

To install Lynux Webs, you need:

- A graphical calculator or computer with Python linux installed (e.g. Casio FX-CG50)
- Enough storage to install PyLinux

Installing Lynux Webs is very easy. Download the py. file from the Releases page, then transfer the file to a graphical calculator. Afterwards, open Python there and select PYLINUX.py and voila! You have a Linux console in a calculator!

# FAQs about Lynux Webs

**Does Lynux Webs works on a Casio FX-CG100?**

If that calculator model has a Python addin pre-installed, then that's allowed to run PyLinux.

**Can you login any user in Lynux Webs?**

Yes of course. You can login lots of accounts. For example, if your name is John, and you type this name in Lynux Webs login:

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
Since graphical calculators sometimes have low resolutions, they might see that. 

If you did not type anything if you see the login screen, it will log in as guest like this:
``` bash
guest@pylinux$
```
To log out a user (any user and also guest), simply type this:

``` bash
logoff
```
and it shows this:
``` bash
User guest logoff!
Login:
```

Note that if you log out, everything are erased, like a sandbox console.

**What are the list of Linux commands that can be type in Lynux Webs?**

Here are the commands (arranged from A-Z):
- about
- bee [command]
- cd [directory]/
- ls [directory]/
- logoff
- nano [filename]
- pwd
- pyfetch
- questa

**How to create a text file in Lynux Webs**

On the Lynux Webs console, type this command (replace filename with custom name):
``` bash
nano [filename]
```
On the nano shell, you can create a text file. To save, just click enter.

**Is there an artificial intelligence engine in Lynux Webs?**

Not yet, but there will be a basic chat bot preinstalled in Lynux Webs which you can type here:
``` bash
pyai
```

**How to install packages?**

To install a package in Lynux Webs, use this format:

``` bash
bee install <package>
```

Bee is a package installer, which installs local pacakges not yet installed.

However, all packages are loaded automatically and will be enabled by doing this command. Some packages are preinstalled, such as Questa (virtual storage). To check for the package catalog to install, type this:
``` bash
bee catalog
```

You may see a few pacakges, depending on which version you have. Since PyLinux is in alpha, you might see 2 or more packages.

**What are the commands of bee in Lynux Webs?**

Here are the commands for bee:

- catalog
- install
- purge
  
**Can you install a desktop environment?**

No, we don't support these. Since Lynux Webs is entirely made from MicroPython, you may receive an error message. For example, if you want to install xfce, and you type this:

``` bash
sudo bee install xfce4
```

you would receive this:
``` bash
sudo bee install xfce4: cmd not found
```
That's because desktop environments are made with C++ and other complex programming languages, which Lynux Webs can't do. If you want a graphical desktop interface, you need to install a real Linux distro instead of Lynux Webs.

**Is Lynux Webs like a real Linux console?**

No, it is just a basic console. You cannot try complex commands; they are hard to be coded.

**Is Lynux Webs open-source?**

Yes, Lynux Webs is open-source on the MIT License. It's a fork of PyLinux.

**Can you run Neofetch on Lynux Webs?**

No, you cannot do that. However, Lynux Webs includes PyFetch which is inspired by Neofetch. To access it, type this:
``` bash
pyfetch
```
**Can you build Lynux Webs?**

There is no build script to create Lynux Webs; but if you want to customize it, you can clone the repository. On Linux, type this: 
``` bash
git clone "https://github.com/hirohamada2014/PyLinux.git"
```

Afterwards, you can edit the source code as long as you like.

On Windows, download the source code zip file from the Releases page, then extract it. You can edit the source code if you like.





