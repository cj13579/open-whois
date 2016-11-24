# open-whois

An open and extensible python whois client that retreives the registration record for the domain name that you specify. It has in-built support for significantly more WHOIS formats than the Sysinternals whois client. It is intended to be a drop-in replacement for the [Windows Sysinternals whois client](https://technet.microsoft.com/en-us/sysinternals/whois.aspx).

# Requirements

None. Just follow the instructions below.

# Instructions

1. Drop whois.exe into `C:\Program Files\open-whois` or another location of your choosing.
2. Update your PATH environment variable with the new folder
3. Run from the command prompt:

```cmd
C:\> whois.exe google.com
```

# Build / Develop

open-whois is a compiled Python application using PyInstaller. It has been built and tested on Python 2.7.

```powershell
> cd open-whois
> pyinstaller.exe --clean -y --onefile whois.py
```

# License

Open-whois is available under the MIT license.

# Contributing

Feel free to fork and submit pull requests or submit issues.

# Sources

- Core library originally from [joepie91](https://github.com/joepie91/python-whois) but using a [forked version](https://github.com/cj13579/python-whois).
- Compiled using Pyinstaller - [https://github.com/pyinstaller/pyinstaller](https://github.com/pyinstaller/pyinstaller)