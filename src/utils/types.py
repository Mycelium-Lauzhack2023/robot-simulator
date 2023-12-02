import enum

import jaxtyping
import numpy as np

OccupancyGrid = jaxtyping.UInt8[np.ndarray, "height width"]

Image = jaxtyping.UInt8[np.ndarray, "height width channels"]

Pose = list[float]  # x, y, theta
Velocity = list[float]  # vx, vy, v_theta


class AgentType(enum.Enum):
  HOLONOMIC = enum.auto()
  DUBINS = enum.auto()
