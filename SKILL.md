---
name: genpark-personal-agent-oculomotor-vergence-peak-velocity-dynamics-skill
version: 1.0.0
description: Zero-dependency sovereign personal agent skill for calculating Binocular Vergence Dynamics peak convergence/divergence velocities, latency, and convergence insufficiency asthenopia.
author: AlphaPark Inc.
license: Apache-2.0
tags:
  - personal-agent
  - ai-agent
  - openclaw
  - genpark
  - mcp
  - mcp-server
  - model-context-protocol
  - python
  - zero-dependency
  - wellness
  - productivity
  - production-ready
metadata:
  openclaw_compatible: true
  hermes_compatible: true
  zero_dependency: true
---

# Oculomotor Binocular Vergence Dynamics Skill

A sovereign personal agent capability for evaluating disjunctive eye movements, midbrain supraoculomotor area (SOA) burst neuron firing, peak convergence and divergence velocities, and convergence insufficiency (CI) / digital display asthenopia.

## Core Capabilities
- **Convergence / Divergence Velocity Dynamics**: Quantifies inward ($V_{conv}$, $18.0 - 45.0^\circ/\text{s}$) and outward ($V_{div}$, $12.0 - 28.0^\circ/\text{s}$) disjunctive motor tracking.
- **Convergence-to-Divergence Ratio**: Formulates the physiological velocity advantage ($V_{conv} / V_{div}$, normative: $1.2 - 2.0$).
- **Convergence Insufficiency (CI) Detection**: Identifies sluggish motor fusion ($< 15.0^\circ/\text{s}$) and prolonged settling times ($> 320\text{ ms}$) linked to reading headaches.
- **Vision Ergonomics & Accommodation Relief**: Recommends monitor distance adjustments, ambient glare reduction, and Brock string vergence therapy.

## Fast Invocation
```python
from client import OculomotorVergenceDynamicsClient

client = OculomotorVergenceDynamicsClient()
res = client.evaluate_vergence_dynamics(
    step_disparity_deg=6.0,
    peak_convergence_velocity_deg_s=29.5,
    peak_divergence_velocity_deg_s=18.2
)
print("Conv/Div Ratio:", res["convergence_divergence_ratio"])
print("Vergence Score:", res["vergence_health_score"], "/ 100")
```
