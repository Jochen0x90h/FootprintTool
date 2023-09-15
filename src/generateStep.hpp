#pragma once

#include "Footprint.hpp"
#include <filesystem>
#include <string>


namespace fs = std::filesystem;


// generate a box as step as minimalistic 3D visualization
bool generateStep(const fs::path &path, const std::string &name, const Footprint &footprint);
