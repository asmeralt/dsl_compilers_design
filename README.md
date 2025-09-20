# Description
A baseline project for "Design Compilers for DSL" [course](https://github.com/gzholtkevych/Design-Compilers-for-DSL)

Python example for ANTLR can be found [here](https://github.com/antlr/antlr4/blob/master/doc/python-target.md)
## Requirements
### MacOSX
1. Install [__brew__](https://brew.sh/) `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
2. Install __antlr4__ tool `brew install antlr`
3. Create python virtual environment
4. Install __antlr4__ python interface `pip install -r requirements.txt`

### Windows
1. Install [__WSL__](https://learn.microsoft.com/en-us/windows/wsl/install) and __Ubuntu__ distro
    1. How to turn on Hyper Visor [video](https://www.youtube.com/watch?v=KEjr6mQ8rqg)
    2. Move __WSL__ installation to non-system drive `wsl --manage distro --move new-location` where `distro = Ubuntu` and `new-location = D:\wsl\`
    3. How to [reset user password](https://superuser.com/questions/1829481/how-to-reset-my-wsl-ubuntu-password)
        1. Start __Ubuntu__ terminal in as root user `wsl -d Ubuntu -u root`
        2. Reset password for your user `passwd {username}`
        3. Enter new password and confirm it. Note: in Unix like systems passwords typed in terminal are not visible
2. Install [__VS Code__](https://code.visualstudio.com/) and recommended for this project extentions
    1. Install [__WSL__](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl) extention for __VS Code__
    2. In bottom left corner select _Open a Remote Window_ button and restart __VS Code__ in __WSL__ mode
3. Run __Ubuntu__ terminal from start menu or in VS Code
4. Update system packages `sudo apt update && sudo apt upgrade -y`
5. Install __python3__ `sudo apt install python3 python3-pip python3-venv`
6. Install __antlr4__ `sudo apt install antlr4`

### Windows (simplified)
1. Install __python3__ from [official website](https://www.python.org/downloads/) without Admin Privileges and/or adding to Path
2. Install [__VS Code__](https://code.visualstudio.com/) and recommended for this project extentions
3. In __VS Code__ open any file with _.py_ extention and in bottom right corner select correct python interpreter installed on previous step
4. Run file with __Run__ button in right top corner
5. If needed specify default Terminal application by pressing __F1__, typing _Terminal: Select Default Profile_ and choosing _Command Prompt_ (cmd.exe)
6. Install __ANTLR4__
    1. Install __ANTLR4__ with `pip install antlr4-tools`
    2. (Alternatively) Get Java for Windows and add java executables & __ANTLR4__ [jar](https://www.antlr.org/download/antlr-4.13.2-complete.jar) in _PATH_ variable
    

## Usage

### ANTLR Calculator Example
1. Enter folder `cd antlr4_calculator`
2. Run antlr tool
``` bash
antlr -Dlanguage=Python3 -visitor Expr.g4  
```
3. Execute `Driver.py` script 
    1. CLI command
    ```bash 
    python3 Driver.py --file input.txt --worker visitor
    ```
    2. VS Code _Run & Debug_ config `ANTLR Calculator Example`

### Labs
Run unit tests from VS Code _Testing_ tab
#### Substrings
1. Run on config form VS Code _Run & Debug_ tab
    1. `Naive Substring`
    2. `KMP Substring`
