# Calls "vcpkg install" for all presets in vpresets.txt
# Also creates a CMakeUserPresets.json which is supported by IDEs such as VSCode
#
# usage:
# 1: Copy vpresets.txt containing a list of presets from support/vcpkg/[operating system] to project root (next to this file)
# 2: Optional: Open vpresets.txt in an editor and adjust to own needs
# 3: $ python vinstall.py
#

import os
import json
from pathlib import Path
import shlex
import subprocess


# configuration
installPrefix = str(Path.home() / ".local")
vcpkg = Path(os.environ['VCPKG_ROOT'])


# read presets from presets.txt
file = open('vpresets.txt', 'r')
presets = file.readlines()
file.close()


# structure for cmake presets
cmakePresets = {
    "version": 3,
    "configurePresets": [],
    "buildPresets": [],
    "testPresets": []
}

# add a preset to the cmake presets
def addPreset(type, name):
    cmakePresets[type].append(
        {
            "name": name,
            "configurePreset": name
        }
    )

# add a preset with config (Debug/Release) for multi-generators (e.g. Visual Studio)
def addPresetWithConfig(type, name, config):
    cmakePresets[type].append(
        {
            "name": name,
            "configurePreset": name,
            "configuration": config
        }
    )

# iterate over presets
triplets = set()
for preset in presets:
    p = shlex.split(preset)
    if not preset.startswith('#') and len(p) == 3:
        triplet = p[0] # vcpkg triplet
        config = p[1] # Debug/Release
        generator = p[2]
        if config == 'Release':
            name = triplet
        else:
            name = f"{triplet}-{config}"

        # install dependencies using conan
        if triplet not in triplets:
            print(f"*** Installing dependencies for {triplet} ***")
            subprocess.run(f"vcpkg install --triplet {triplet} --x-install-root vcpkg/{triplet}", shell=True)
            triplets.add(triplet)

        # create cmake presets
        cmakePresets["configurePresets"].append(
            {
                "name": name,
                "description": f"({generator})",
                "generator": generator,
                "cacheVariables": {
                    "VCPKG_INSTALLED_DIR": f"vcpkg/{triplet}",
                    "X_VCPKG_APPLOCAL_DEPS_INSTALL": "ON",
                    "CMAKE_BUILD_TYPE": config,
                    "CMAKE_INSTALL_PREFIX": installPrefix
                },
                "toolchainFile": str(vcpkg / "scripts/buildsystems/vcpkg.cmake"),
                "binaryDir": f"build/{name}"
            }
        )
        if "Visual Studio" in generator:
            addPresetWithConfig("buildPresets", name, config)
            addPresetWithConfig("testPresets", name, config)
        else:
            addPreset("buildPresets", name)
            addPreset("testPresets", name)

# save cmake presets to CMakeUserPresets.json
file = open("CMakeUserPresets.json", "w")
file.write(json.dumps(cmakePresets, indent=4))
file.close()
