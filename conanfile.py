from conans import ConanFile, CMake, tools


class PdcursesConan(ConanFile):
    name = "pdcurses"
    version = "3.8"
    license = "Public Domain"
    author = "Jonathan Cooper me@jonathancooper.xyz"
    url = "https://github.com/DrowsySaturn/pdcurses-conan-recipe"
    description = "CLI library"
    topics = ("console", "CLI", "curses")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/wmcbrine/PDCurses.git")
        # This small hack might be useful to guarantee proper /MT /MD linkage
        # in MSVC if the packaged project doesn't have variables to set it
        # properly
        tools.save("PDCurses/CMakeLists.txt", '''
CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

PROJECT(HelloWorld)

INCLUDE_DIRECTORIES("common")

if (WIN32 OR MINGW)
    INCLUDE_DIRECTORIES("wincon")
    INCLUDE_DIRECTORIES(".")
endif()

file(GLOB curses_SRC "pdcurses/*.c")

if (WIN32 OR MINGW OR MSYS)
    file(GLOB wincurses_SRC "wincon/*.c")
    ADD_LIBRARY(curses ${curses_SRC} ${wincurses_SRC})
endif()
if (UNIX)
    file(GLOB xcurses_SRC "x11/*.c")
    ADD_LIBRARY(curses ${curses_SRC} ${xcurses_SRC})
endif()
''')
        tools.replace_in_file("PDCurses/CMakeLists.txt", "PROJECT(HelloWorld)",
                              '''PROJECT(HelloWorld)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()
''')

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="PDCurses/")
        cmake.build()

        # Explicit way:
        # self.run('cmake %s/hello %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("curses.h", dst="include", src="PDCurses")
        self.copy("*curses.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["curses"]

