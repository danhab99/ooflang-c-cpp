# ooflang (C/C++)

Replaces the token in C/C++ projects with macros to decrease readibility.


## Usage

```bash
dan@dan-Lenovo-ideapad-FLEX-5-1470:~$ ooflang -h
usage: ooflang [-h] --file FILE --out OUT

Replaces the tokens in your C/C++ project with oofs that decrease readability

optional arguments:
  -h, --help   show this help message and exit
  --file FILE  File to process
  --out OUT    Where to store results
```

### Example:

```bash
dan@dan-Lenovo-ideapad-FLEX-5-1470:~/Documents/cpp/myproject$ ooflang --file ./main.cpp --out ./oof.cpp
```

## Install

1. Download the source code by `git clone` or from the [Releases](https://github.com/danhab99/ooflang/releases).
2. `cd` into the folder and run `pip install -e .`