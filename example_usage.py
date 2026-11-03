"""
Example Usage: Oculomotor Binocular Vergence Dynamics & Convergence Fatigue.
Demonstrates zero-dependency calculation of convergence/divergence velocities, ratio, and digital asthenopia scoring.
"""

from client import OculomotorVergenceDynamicsClient


def main():
    client = OculomotorVergenceDynamicsClient()
    print("=== Oculomotor Binocular Vergence Dynamics Demo ===")

    # Test Case 1: Healthy vigorous binocular motor fusion (6 deg step)
    res1 = client.evaluate_vergence_dynamics(
        step_disparity_deg=6.0,
        peak_convergence_velocity_deg_s=29.5,
        peak_divergence_velocity_deg_s=18.2,
        vergence_latency_ms=155.0,
        time_constant_ms=210.0
    )
    print("\nTest Case 1: Optimal Binocular Vergence Dynamics")
    print(f"  Step Disparity: {res1['step_disparity_deg']} deg | Convergence Velocity: {res1['peak_convergence_velocity_deg_s']} deg/s")
    print(f"  Divergence Velocity: {res1['peak_divergence_velocity_deg_s']} deg/s | Conv/Div Ratio: {res1['convergence_divergence_ratio']}")
    print(f"  Latency: {res1['vergence_latency_ms']} ms | Time Constant: {res1['time_constant_ms']} ms")
    print(f"  Vergence Score: {res1['vergence_health_score']} / 100")
    print(f"  Classification: {res1['classification']}")
    print(f"  Physiological Interpretation: {res1['physiological_interpretation']}")
    print(f"  Actionable Guidance: {res1['actionable_guidance']}")

    # Test Case 2: Convergence Insufficiency / Digital Eyestrain pattern
    res2 = client.evaluate_vergence_dynamics(
        step_disparity_deg=6.0,
        peak_convergence_velocity_deg_s=13.0,
        peak_divergence_velocity_deg_s=15.5,
        vergence_latency_ms=215.0,
        time_constant_ms=360.0
    )
    print("\nTest Case 2: Convergence Insufficiency Pattern (Digital Eyestrain)")
    print(f"  Convergence Velocity: {res2['peak_convergence_velocity_deg_s']} deg/s | Conv/Div Ratio: {res2['convergence_divergence_ratio']}")
    print(f"  Time Constant: {res2['time_constant_ms']} ms")
    print(f"  Vergence Score: {res2['vergence_health_score']} / 100")
    print(f"  Classification: {res2['classification']}")
    print(f"  Actionable Guidance: {res2['actionable_guidance']}")


if __name__ == "__main__":
    main()
