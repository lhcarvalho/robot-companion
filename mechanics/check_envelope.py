#!/usr/bin/env python3
"""Numerical checks for known/proposed component envelopes; NOT 3D collision checking."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Box:
    width: float
    height: float
    depth: float

HEAD = Box(105.0, 85.0, 60.0)   # proposed; not frozen
WALL = 2.4                        # assumed wall
DISPLAY = Box(70.5, 43.3, 0.0)    # PCB depth UNVERIFIED
CAMERA = Box(32.0, 32.0, 0.0)     # PCB depth UNVERIFIED

def cavity(outer: Box, wall: float) -> Box:
    assert wall > 0
    result = Box(outer.width - 2*wall, outer.height - 2*wall, outer.depth - 2*wall)
    if min(result.width, result.height, result.depth) <= 0:
        raise ValueError("Negative cavity dimension")
    return result

def preliminary_report() -> dict:
    inner = cavity(HEAD, WALL)
    return {
        "cavity_mm": (inner.width, inner.height, inner.depth),
        "nominal_stack_margin_height_mm": HEAD.height-DISPLAY.height-CAMERA.height,
        "display_width_fits_bbox": DISPLAY.width < inner.width,
        "camera_width_fits_bbox": CAMERA.width < inner.width,
        "conclusion": "bbox tests only; mechanical fit NOT PROVEN",
    }

if __name__ == "__main__":
    report = preliminary_report()
    for key,value in report.items(): print(f"{key}: {value}")
    assert round(report["nominal_stack_margin_height_mm"], 2) == 9.7
    assert tuple(round(x, 1) for x in report["cavity_mm"]) == (100.2, 80.2, 55.2)
