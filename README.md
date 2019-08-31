# ooflang (C/C++)

Replaces the token in C/C++ projects with macros to decrease readibility.


## Usage

```bash
usage: ooflang [-h] [-o OUTPUT] [-q] [-d] Input File [Input File ...]

Obfuscates C/C++ code

positional arguments:
  Input File

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Directs the output to a name of your choice
  -q, --quiet           Do not output anything
  -d, --dry             Dumps results to standard out
```

### Example:

```bash
dan@dan-Lenovo-ideapad-FLEX-5-1470:~/Documents/cpp/myproject$ ooflang test.cpp
```

## Install

1. Download the source code by `git clone` or from the [Releases](https://github.com/danhab99/ooflang/releases).
2. `cd` into the folder and run `pip install -e .`