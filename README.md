# ooflang (C/C++)

![GitHub stars](https://img.shields.io/github/stars/danhab99/ooflang-c-cpp)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/danhab99/ooflang-c-cpp)
![PyPI](https://img.shields.io/pypi/v/ooflang)

Replaces the token in C/C++ projects with macros to decrease readibility.

- [ooflang (C/C++)](#ooflang-cc)
  - [Usage](#usage)
    - [Example:](#example)
    - [Demo](#demo)
  - [Install](#install)
  - [Warnings](#warnings)

## Usage

```bash
usage: ooflang.py [-h] [-o OUTPUT] [-q] [-d] [-p] Input File [Input File ...]

Obfuscates C/C++ code

positional arguments:
  Input File

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Directs the output to a name of your choice
  -q, --quiet           Do not output anything
  -d, --dry             Dumps results to standard out
  -p, --nopretest       Do not run pretest to make sure obfuscated code will
                        compile            Dumps results to standard out
```

### Example:

```bash
dan@dan-Lenovo-ideapad-FLEX-5-1470:~/Documents/cpp/myproject$ ooflang test.cpp
```

### Demo

Inital code

```cpp
#include <iostream>

using namespace std;

int main(int argc, char ** argv) {
  // Adds two numbers
  int a,b;
  cout << "Input a: ";
  cin >> a;
  cout << "Input b: ";
  cin >> b;

  cout << (a + b);
  return 0;
}
```

Oofed code

```cpp
#include <iostream>

#define oof cout
#define off >>
#define ooO int
#define oFo <<
#define ooF char
#define oOf )
#define oOoF (
#define oOfF +
#define oFof namespace
#define ooof ,
#define oofff 0
#define ooffO "Input b: "
#define oOfFF ;
#define ofOFF main
#define oooOF std
#define oooOf return
#define ooofO argv
#define ofoFf **
#define oofoF using
#define oOffO argc
#define ooOOF a
#define ooOfF b
#define ooooF cin
#define ooOFF "Input a: "
#define ooFOF {
#define oOOoFF }

oofoF oFof oooOF oOfFF ooO ofOFF oOoF ooO oOffO ooof ooF ofoFf ooofO oOf ooFOF ooO ooOOF ooof ooOfF oOfFF oof oFo ooOFF oOfFF ooooF off ooOOF oOfFF oof oFo ooffO oOfFF ooooF off ooOfF oOfFF oof oFo oOoF ooOOF oOfF ooOfF oOf oOfFF oooOf oofff oOfFF oOOoFF
```

## Install

Requires GNU c++ compiler `g++`.

1. Download the source code by `git clone` or from the [Releases](https://github.com/danhab99/ooflang/releases).
2. `cd` into the folder and run `pip install -e .`

## Warnings

ooflang will remove all code formatting and string the all the code onto one line, therefore the program should beable to compile in one line

* ooflang cannot handle single lined code blocks without curly braces. 