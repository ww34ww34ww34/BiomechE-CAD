#include "biomeche_q0/adapter.hpp"

#include <opensubdiv/far/topologyDescriptor.h>
#include <opensubdiv/far/topologyRefinerFactory.h>

#include <memory>

namespace biomeche::q0 {
namespace {

class OpenSubdivAdapter final : public Adapter {
public:
    SmokeResult smoke() noexcept override {
        namespace Far = OpenSubdiv::Far;

        const int verts_per_face[1] = {4};
        const Far::Index face_vertices[4] = {0, 1, 2, 3};

        Far::TopologyDescriptor desc;
        desc.numVertices = 4;
        desc.numFaces = 1;
        desc.numVertsPerFace = verts_per_face;
        desc.vertIndicesPerFace = face_vertices;

        Far::TopologyRefinerFactory<Far::TopologyDescriptor>::Options options;
        options.validateFullTopology = true;

        std::unique_ptr<Far::TopologyRefiner> refiner(
            Far::TopologyRefinerFactory<Far::TopologyDescriptor>::Create(desc, options));

        const bool ok = refiner != nullptr
            && refiner->GetLevel(0).GetNumVertices() == 4
            && refiner->GetLevel(0).GetNumFaces() == 1;

        return {
            "opensubdiv",
            "v3_7_0@9dab8a47bfbb1388ec8388fe61f5f916e6123f38",
            CapabilityCoreLinked | CapabilitySubdObjectOrTopology | CapabilityHeadless,
            ok
        };
    }
};

} // namespace

std::unique_ptr<Adapter> make_adapter() {
    return std::make_unique<OpenSubdivAdapter>();
}

} // namespace biomeche::q0
