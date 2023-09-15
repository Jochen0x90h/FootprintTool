#include "generateVrml.hpp"
#include <fstream>


// generate a box as vrml as minimalistic 3D visualization
void generateVrml(const fs::path &path, const std::string &name, const Footprint &footprint) {
    // center of box
    double3 center = footprint.body.offset + double3(footprint.position.x, footprint.position.y, 0);
    center.y = -center.y;

    // size of box
    double3 size = footprint.body.size;

    // create output file
    std::ofstream s((path / (name + ".wrl")).string());

    // header
    s << R"vrml(#VRML V2.0 utf8
Shape {
    appearance Appearance {material DEF mat Material {
        ambientIntensity 0.293
        diffuseColor 0.148 0.145 0.145
        specularColor 0.18 0.168 0.16
        emissiveColor 0.0 0.0 0.0
        transparency 0.0
        shininess 0.35
        }
    }
}
Shape {
    geometry IndexedFaceSet {
        creaseAngle 0.50
        coordIndex [3,0,2,-1,3,1,0,-1,6,5,7,-1,6,4,5,-1,1,4,0,-1,1,5,4,-1,7,2,6,-1,7,3,2,-1,2,4,6,-1,2,0,4,-1,7,1,3,-1,7,5,1]
        coord Coordinate {point [)vrml";

    for (int i = 0; i < 8; ++i) {
        if (i != 0)
            s << ',';
        double3 p = (center + size * double3(i & 1 ? 0.5 : -0.5, i & 2 ? 0.5 : -0.5, i & 4 ? 1.0 : 0.0)) / 2.54;
        s << p;
    }

s << R"vrml(]}
    }
    appearance Appearance {material USE mat}
}
)vrml";

    s.close();
}
