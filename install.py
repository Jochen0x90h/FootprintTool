# Install the project to ~/.local/bin (CMAKE_INSTALL_PREFIX defined in cinstall.py/vinstall.py)
#
# Usage:
# 1a: When using conan, call $ python cinstall.py
# 1b: When using vcpkg, call $ python vinstall.py
# 2: $ python install.py
#

import subprocess


# configure
subprocess.run(f"cmake --preset native", shell=True)

# build and install to ~/.local/bin
subprocess.run(f"cmake --build --preset native --target install", shell=True)
