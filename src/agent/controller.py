from yacs import config as cfg_

from src.utils import types


class Controller:

  def __init__(self, agent_cfg: cfg_.CfgNode) -> None:
    self._max_velocity = agent_cfg.MAX_VELOCITY

    self._pose: types.Pose | None = None
    self._goal_pose: types.Pose | None = None

  def set_pose(self, pose: types.Pose) -> None:
    self._pose = pose

  def set_goal_pose(self, goal_pose: types.Pose) -> None:
    self._goal_pose = goal_pose

  def calc_velocity(self) -> types.Velocity:
    if self._pose is None or self._goal_pose is None:
      raise ValueError("Pose and goal pose must be set before calculating velocity")
    velocity: list[float] = [0, 0, 0]
    for i in range(3):
      dx = self._goal_pose[i] - self._pose[i]
      velocity[i] = min(dx, self._max_velocity[i])
    return velocity
