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
TBD

## Usage
1. Enter folder `cd antlr4_calculator`
2. Run antlr tool
``` bash
antlr -Dlanguage=Python3 -visitor Expr.g4  
```
3. Execute `Driver.py` script
```bash 
python3 Driver.py --file input.txt --worker visitor
```
