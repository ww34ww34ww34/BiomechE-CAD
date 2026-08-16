#pragma once

#include <cstdint>
#include <memory>

namespace biomeche::q0 {

enum Capability : std::uint32_t {
    CapabilityNone = 0u,
    CapabilityCoreLinked = 1u << 0,
    CapabilitySubdObjectOrTopology = 1u << 1,
    CapabilityHeadless = 1u << 2
};

struct SmokeResult {
    const char* candidate_id;
    const char* candidate_version;
    std::uint32_t capability_mask;
    bool ok;
};

class Adapter {
public:
    virtual ~Adapter() = default;
    virtual SmokeResult smoke() noexcept = 0;
};

std::unique_ptr<Adapter> make_adapter();

} // namespace biomeche::q0
