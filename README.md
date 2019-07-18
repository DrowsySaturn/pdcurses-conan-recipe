# pdcurses-conan-recipe
A conan recipe for PDCurses. Uses https://github.com/wmcbrine/PDCurses

### Installation

You can download this repository and in the root of the repo run:
```
conan create . drowsysaturn/stable
```

Inside of your conanfile.txt, add under [requires]
```
PDCurses/3.8@drowsysaturn/stable
```

Your project should now be able to use PDCurses.

**This project has not yet been tested with any compiler except for Visual Studio 16 2019's 64 bit compiler. Any confirmations of this working on other platforms would be appreciated.**
