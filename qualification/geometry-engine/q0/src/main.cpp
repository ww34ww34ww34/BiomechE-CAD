#include "biomeche_q0/adapter.hpp"

#include <iostream>
#include <memory>

int main() {
    std::unique_ptr<biomeche::q0::Adapter> adapter = biomeche::q0::make_adapter();
    if (!adapter) {
        std::cerr << "{\"ok\":false,\"error\":\"adapter_factory_returned_null\"}\n";
        return 2;
    }

    const biomeche::q0::SmokeResult result = adapter->smoke();
    std::cout
        << "{\"candidateId\":\"" << result.candidate_id
        << "\",\"candidateVersion\":\"" << result.candidate_version
        << "\",\"capabilityMask\":" << result.capability_mask
        << ",\"ok\":" << (result.ok ? "true" : "false")
        << "}\n";

    return result.ok ? 0 : 1;
}
