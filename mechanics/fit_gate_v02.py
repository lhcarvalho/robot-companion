#!/usr/bin/env python3
"""Preliminary dimensional gate, not a real collision or STEP assembly check.

X is head width, Y is vertical head height, Z is head depth (toward front).
All dimensions are in millimetres, and every unverified depth/position is tagged.
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class Head:
    width: float = 105.0  # proposed
    height: float = 85.0  # proposed
    depth: float = 60.0  # proposed
    wall: float = 2.4     # fabrication assumption
    corner_radius: float = 14.0  # proposal

@dataclass(frozen=True)
class Rect:
    x: float
    y: float
    w: float
    h: float
    def bounds(self):
        return (self.x-self.w/2, self.y-self.h/2,
                self.x+self.w/2, self.y+self.h/2)

def aabb_overlap(a: Rect, b: Rect):
    ax0, ay0, ax1, ay1 = a.bounds()
    bx0, by0, bx1, by1 = b.bounds()
    return (max(0.0, min(ax1, bx1)-max(ax0, bx0)),
            max(0.0, min(ay1, by1)-max(ay0, by0)))

def inspect():
    head = Head()
    lcd = Rect(0.0, -15.0, 70.5, 43.3) # manufacturer board nominal
    cam = Rect(0.0, 22.0, 32.0, 32.0) # manufacturer board nominal
    inner_x = head.width/2-head.wall
    inner_y = head.height/2-head.wall
    for name, part in [("LCD", lcd), ("CAMERA", cam)]:
        x0,y0,x1,y1 = part.bounds()
        assert min(x0+inner_x, inner_x-x1, y0+inner_y, inner_y-y1) >= 0, (
            f"{name}: fails axis-aligned inner cavity check")
    overlap_x, overlap_y = aabb_overlap(lcd,cam)
    camera_top_clearance = inner_y-(cam.y+cam.h/2)
    lcd_bottom_clearance = lcd.y-lcd.h/2+inner_y
    return {
        "head_inner_bbox_mm": (head.width-2*head.wall,
                               head.height-2*head.wall,
                               head.depth-2*head.wall),
        "camera_top_nominal_clearance_mm": round(camera_top_clearance, 2),
        "lcd_bottom_nominal_clearance_mm": round(lcd_bottom_clearance, 2),
        "front_projection_overlap_mm": (round(overlap_x,2),round(overlap_y,2)),
        "state": "2D bounding box feasibility only; depth, corners, connectors and cables UNKNOWN",
    }

if __name__ == "__main__":
    result = inspect()
    for k,v in result.items(): print(f"{k}: {v}")
    assert result["head_inner_bbox_mm"] == (100.2, 80.2, 55.2) or all(
        abs(a-b)<1e-8 for a,b in zip(result["head_inner_bbox_mm"],(100.2,80.2,55.2)))
    assert result["camera_top_nominal_clearance_mm"] == 2.1
    assert result["front_projection_overlap_mm"] == (32.0,0.65)
