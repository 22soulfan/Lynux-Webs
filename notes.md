# Notes on PyLinux

Since it is in alpha, you might expect some bugs and errors.

## Notes on graphical calculators

On some calculators (such as Casio FX-CG20), Python might not be pre-installed. It is not recommended by Casio to install the official Python add-in. And some other calculator brands might have no Python preinstalled. 

**If a graph calculator has Python, can you use PyLinux there?**

Yes, you can. Every graph calculator that has Python pre-installed can run PyLinux as long as it uses the official Python programming language or MicroPython. Just bear in mind that some modules may not work.

**Does PyLinux works on any device?**

Yes. If the device has Python installed, then yes, it is possible. However, if Python is not installed, you have to install it.

On Windows, Python may not be pre-installed. Download it from the official website and follow the on-screen instructions. You can use VSCode or Mu Editor as an alternative since they support Python. To run PyLinux, go to the start menu, search IDLE and click open. If IDLE is shown on your desktop, double-click it, click File > Open, and select PyLinux on the directory that has it.

On macOS, Python is pre-installed, but it may be an older version (if using macOS 10.15 and under.) Update Python by going to the official website, and installing the package. To run PyLinux, go to the Terminal, and type this command:
``` bash
idle
```
Then go to File > Open and select PyLinux on the directory that has it.

Note: Linux and macOS are Unix so the instructions are same.
