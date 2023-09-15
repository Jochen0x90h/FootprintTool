#pragma once

#include "Footprint.hpp"
#include <filesystem>
#include <string>


namespace fs = std::filesystem;


// generate a box as vrml as minimalistic 3D visualization
void generateVrml(const fs::path &path, const std::string &name, const Footprint &footprint);
