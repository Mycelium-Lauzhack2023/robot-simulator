from yacs import config as cfg_

from src.utils import types
from src.world import world as world_


class Controller:

  def __init__(self, controller_cfg: cfg_.CfgNode) -> None:
    self._max_speed = controller_cfg.MAX_SPEED
    self._max_yaw_rate = controller_cfg.MAX_YAW_RATE
    self._goal_reached_threshold = controller_cfg.GOAL_REACHED_THRESHOLD

    self._pose: types.Pose = []
    self._goal_pose: types.Pose = []

  def set_pose(self, pose: types.Pose) -> None:
    self._pose = pose

  def set_goal_pose(self, goal_pose: types.Pose) -> None:
    self._goal_pose = goal_pose

  def calc_velocity(self, world: world_.World) -> types.Velocity:
    self._assert_is_initialized()
    velocity: list[float] = [0, 0, 0]
    for i in range(2):
      dx = self._goal_pose[i] - self._pose[i]
      dx_abs = abs(dx)
      dx_sign = 1 if dx > 0 else -1
      velocity[i] = min(dx_abs, self._max_speed)
      velocity[i] *= dx_sign
    d_theta = self._goal_pose[2] - self._pose[2]
    velocity[2] = self._max_yaw_rate if d_theta > 0 else -self._max_yaw_rate
    for i in range(2):
      new_pose = self._pose
      new_pose[i] = self._pose[i] + velocity[i]
      if world.is_pose_occupied(new_pose):
        velocity[i] = 0
    return velocity

  def is_goal_reached(self) -> bool:
    self._assert_is_initialized()
    return all(abs(self._pose[i] - self._goal_pose[i]) < self._goal_reached_threshold for i in range(2))

  def _assert_is_initialized(self) -> None:
    if not self._pose or not self._goal_pose:
      raise RuntimeError("Pose and goal pose must be set")
