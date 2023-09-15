# Conan

If you use conan for the first time, run

```console
$ conan profile detect
```

It creates a default profile in ~/.conan2/profiles

## Windows
The default profile should contain these lines:

```
compiler=msvc
compiler.cppstd=20
```

If not, Install Visual Studio Community Edition (in addition to VSCode!)
with C++ for desktop option and/or change cppstd to 20.

## Debug Profile

Create debug profile ~/.conan2/profiles/debug by copying the default profile and set

```
build_type=Debug
```

# Presets

Copy cpresets.txt from the subdirectory for your platform into the root of the project.

Then run

```console
$ python cinstall.py
```

It generates CMakeUserPresets.json which can be used by IDEs such as VSCode
