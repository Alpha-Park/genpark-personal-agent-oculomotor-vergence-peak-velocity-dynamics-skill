"""
Oculomotor Binocular Vergence Dynamics & Convergence Fatigue Engine.
Provides deterministic, zero-dependency modeling of convergence/divergence peak velocities (deg/s),
convergence-to-divergence velocity ratio, vergence latency (ms), and digital asthenopia / convergence insufficiency (CI).
"""

from typing import Dict, Any, List, Optional


class OculomotorVergenceDynamicsClient:
    """
    Deterministic client for calculating Binocular Vergence Dynamics.
    Assesses midbrain supraoculomotor area (SOA) vergence burst neurons, medial rectus co-activation,
    binocular disparity motor fusion, and visual display terminal (VDT) eyestrain.
    """

    def __init__(self):
        pass

    def evaluate_vergence_dynamics(
        self,
        step_disparity_deg: float,
        peak_convergence_velocity_deg_s: float,
        peak_divergence_velocity_deg_s: float,
        vergence_latency_ms: float = 160.0,
        time_constant_ms: float = 220.0
    ) -> Dict[str, Any]:
        """
        Calculates vergence velocity ratio and binocular motor fusion fatigue score.
        Normative values (for 4 - 8 deg step disparity):
        - Peak Convergence Velocity: 18.0 - 42.0 deg/s
        - Peak Divergence Velocity: 12.0 - 26.0 deg/s
        - Conv / Div Ratio: 1.2 - 2.0
        - Vergence Latency: 140.0 - 190.0 ms
        - Time Constant: 180.0 - 280.0 ms
        """
        if step_disparity_deg <= 0 or peak_convergence_velocity_deg_s <= 0 or peak_divergence_velocity_deg_s <= 0:
            return {"error": "Step disparity and peak velocities must be strictly positive"}
        if vergence_latency_ms <= 0 or time_constant_ms <= 0:
            return {"error": "Latency and time constant must be strictly positive"}

        # 1. Convergence-to-Divergence Ratio
        conv_div_ratio = round(peak_convergence_velocity_deg_s / peak_divergence_velocity_deg_s, 2)

        # 2. Convergence Velocity per Degree of Disparity (s^-1)
        conv_gain_per_deg = round(peak_convergence_velocity_deg_s / step_disparity_deg, 2)

        # 3. Binocular Vergence Health & Asthenopia Score (0 - 100)
        score = 80.0
        if 20.0 <= peak_convergence_velocity_deg_s <= 42.0:
            score += 10.0
        elif 16.0 <= peak_convergence_velocity_deg_s < 20.0:
            score += 4.0
        elif peak_convergence_velocity_deg_s < 12.0:
            score -= 28.0  # Severe convergence insufficiency
        elif peak_convergence_velocity_deg_s < 16.0:
            score -= 15.0

        if 1.2 <= conv_div_ratio <= 1.9:
            score += 5.0
        elif conv_div_ratio < 0.9:
            score -= 15.0  # Paradoxical convergence slowness

        if 140.0 <= vergence_latency_ms <= 185.0:
            score += 5.0
        elif vergence_latency_ms > 230.0:
            score -= 15.0

        if time_constant_ms <= 260.0:
            score += 5.0
        elif time_constant_ms > 340.0:
            score -= 15.0

        vergence_score = round(min(100.0, max(5.0, score)), 1)

        if vergence_score >= 85.0 and peak_convergence_velocity_deg_s >= 18.0 and time_constant_ms <= 280.0:
            tier = "OPTIMAL_BINOCULAR_VERGENCE_DYNAMICS"
            interp = f"Crisp binocular vergence kinetics (Conv {peak_convergence_velocity_deg_s} deg/s, Div {peak_divergence_velocity_deg_s} deg/s, Ratio {conv_div_ratio}, Latency {vergence_latency_ms} ms); balanced midbrain supraoculomotor burst integration."
            guidance = "Superior motor fusion and binocular alignment. High resilience against digital reading fatigue and near-work asthenopia."
        elif peak_convergence_velocity_deg_s < 14.5 or time_constant_ms > 320.0:
            tier = "CONVERGENCE_INSUFFICIENCY_ASTHENOPIA"
            interp = f"Sluggish convergence velocity ({peak_convergence_velocity_deg_s} deg/s < 16 deg/s) or prolonged motor settlement time ({time_constant_ms} ms); hallmark of convergence insufficiency."
            guidance = "Convergence insufficiency detected. Implement the 20-20-20 rule, increase display working distance, and practice Brock string / pencil push-up vergence therapy."
        else:
            tier = "MODERATE_VERGENCE_MOTOR_FATIGUE"
            interp = f"Borderline vergence velocity (Conv {peak_convergence_velocity_deg_s} deg/s, Time constant {time_constant_ms} ms); mild neuromuscular ocular strain."
            guidance = "Incipient binocular fatigue. Take structured 2-minute horizon gazing breaks between intense code or text review."

        return {
            "step_disparity_deg": step_disparity_deg,
            "peak_convergence_velocity_deg_s": peak_convergence_velocity_deg_s,
            "peak_divergence_velocity_deg_s": peak_divergence_velocity_deg_s,
            "convergence_divergence_ratio": conv_div_ratio,
            "convergence_velocity_per_deg": conv_gain_per_deg,
            "vergence_latency_ms": vergence_latency_ms,
            "time_constant_ms": time_constant_ms,
            "vergence_health_score": vergence_score,
            "classification": tier,
            "physiological_interpretation": interp,
            "actionable_guidance": guidance
        }
