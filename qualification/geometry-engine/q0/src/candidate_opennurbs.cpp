#include "biomeche_q0/adapter.hpp"

#include <opennurbs_public.h>

#include <memory>

namespace biomeche::q0 {
namespace {

class OpenNurbsAdapter final : public Adapter {
public:
    SmokeResult smoke() noexcept override {
        // Q0 deliberately performs only a link/type-containment smoke.
        // Geometry semantics remain product-owned and richer ON_SubD tests begin in Q1/Q2.
        const unsigned int version = ON::Version();
        ON_SubD subd;
        (void)subd;

        const bool ok = version != 0u;
        return {
            "opennurbs",
            "8.x@00bdd2ce8f3e4cd3d4921343909bbe123b2e9d58",
            CapabilityCoreLinked | CapabilitySubdObjectOrTopology | CapabilityHeadless,
            ok
        };
    }
};

} // namespace

std::unique_ptr<Adapter> make_adapter() {
    return std::make_unique<OpenNurbsAdapter>();
}

} // namespace biomeche::q0
