"""
MCP Server for Oculomotor Vergence Dynamics Skill.
Exposes JSON-RPC Model Context Protocol tools for evaluating convergence/divergence peak velocities, latency, and asthenopia scores.
"""

import sys
import json
from typing import Dict, Any
from client import OculomotorVergenceDynamicsClient


def get_tools_manifest() -> Dict[str, Any]:
    return {
        "tools": [
            {
                "name": "evaluate_vergence_dynamics",
                "description": "Calculates Binocular Vergence Dynamics peak convergence/divergence velocity (deg/s), latency (ms), time constant, and asthenopia score.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "step_disparity_deg": {
                            "type": "number",
                            "description": "Step binocular disparity jump in degrees (e.g. 6.0 deg, normative 4-8 deg)."
                        },
                        "peak_convergence_velocity_deg_s": {
                            "type": "number",
                            "description": "Peak angular velocity during inward convergence in deg/s (e.g. 28.5 deg/s)."
                        },
                        "peak_divergence_velocity_deg_s": {
                            "type": "number",
                            "description": "Peak angular velocity during outward divergence in deg/s (e.g. 18.0 deg/s)."
                        },
                        "vergence_latency_ms": {
                            "type": "number",
                            "description": "Vergence motor initiation latency in milliseconds (default: 160.0 ms, normative 140-190 ms).",
                            "default": 160.0
                        },
                        "time_constant_ms": {
                            "type": "number",
                            "description": "Exponential settling time constant in milliseconds (default: 220.0 ms).",
                            "default": 220.0
                        }
                    },
                    "required": ["step_disparity_deg", "peak_convergence_velocity_deg_s", "peak_divergence_velocity_deg_s"]
                }
            }
        ]
    }


def handle_request(client: OculomotorVergenceDynamicsClient, req: Dict[str, Any]) -> Dict[str, Any]:
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": get_tools_manifest()
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})

        if name == "evaluate_vergence_dynamics":
            res = client.evaluate_vergence_dynamics(
                step_disparity_deg=float(args.get("step_disparity_deg", 6.0)),
                peak_convergence_velocity_deg_s=float(args.get("peak_convergence_velocity_deg_s", 28.0)),
                peak_divergence_velocity_deg_s=float(args.get("peak_divergence_velocity_deg_s", 18.0)),
                vergence_latency_ms=float(args.get("vergence_latency_ms", 160.0)),
                time_constant_ms=float(args.get("time_constant_ms", 220.0))
            )
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(res, indent=2)
                        }
                    ]
                }
            }
        else:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {
                    "code": -32601,
                    "message": f"Method not found: {name}"
                }
            }
    else:
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "error": {
                "code": -32600,
                "message": f"Invalid Request: Unsupported method {method}"
            }
        }


def main():
    client = OculomotorVergenceDynamicsClient()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_request(client, req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err_resp = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {
                    "code": -32700,
                    "message": f"Parse error or exception: {str(e)}"
                }
            }
            sys.stdout.write(json.dumps(err_resp) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
