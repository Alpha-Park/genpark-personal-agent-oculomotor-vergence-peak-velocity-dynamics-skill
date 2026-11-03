# Oculomotor Binocular Vergence Dynamics Skill

[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/zero--dependencies-standard--lib-brightgreen.svg)](requirements.txt)
[![MCP Protocol Ready](https://img.shields.io/badge/mcp-protocol--ready-orange.svg)](mcp_server.py)
[![OpenClaw Certified](https://img.shields.io/badge/openclaw-certified-purple.svg)](SKILL.md)

Zero-dependency sovereign personal agent skill for non-invasive evaluation of Binocular Vergence Dynamics peak convergence/divergence velocity, latency, and convergence insufficiency asthenopia.

```mermaid
flowchart TD
    BinocularDisparity["Step Binocular Disparity Jump (4-8 deg)"] --> SOA["Midbrain Supraoculomotor Area (SOA) Burst Neurons"]
    SOA --> MedialRecti["Bilateral Medial Rectus Inward Co-Activation (Convergence)"]
    SOA --> LateralRecti["Bilateral Lateral Rectus Outward Relaxation (Divergence)"]
    MedialRecti & LateralRecti --> VelocityRatios["Peak Velocity Kinetics & Conv/Div Ratio"]
    VelocityRatios --> AsthenopiaEngine["Convergence Insufficiency (CI) & Digital Eyestrain Score"]
    AsthenopiaEngine --> Agent["OpenClaw / Hermes Personal Agent Screen Distance Prescriptions"]
```

## Features
- **Deterministic Math**: Pure Python standard library implementation with zero external dependencies.
- **Oculomotor Neurophysiology Standards**: Implements validated equations for step vergence velocities, main sequence ratios, and settling time constants.
- **Digital Eyestrain & Convergence Fatigue Shield**: Sensitive detection of binocular motor fusion breakdown during intense screen reading.
- **Model Context Protocol (MCP)**: Native JSON-RPC tool integration for LLMs and autonomous agents.

## Quickstart

```python
from client import OculomotorVergenceDynamicsClient

client = OculomotorVergenceDynamicsClient()
result = client.evaluate_vergence_dynamics(
    step_disparity_deg=6.0,
    peak_convergence_velocity_deg_s=29.5,
    peak_divergence_velocity_deg_s=18.2
)
print("Conv/Div Ratio:", result["convergence_divergence_ratio"])
print("Vergence Score:", result["vergence_health_score"])
print("Classification:", result["classification"])
```

## License
Apache-2.0
