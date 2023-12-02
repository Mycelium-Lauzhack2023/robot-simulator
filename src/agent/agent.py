from yacs import config as cfg_

from src.agent import controller as controller_
from src.utils import types
from src.world import world as world_


class Agent:

  def __init__(self, agent_cfg: cfg_.CfgNode, controller: controller_.Controller):
    self._pose = agent_cfg.STARTING_POSE
    self._velocity = agent_cfg.STARTING_VELOCITY

    self._goal_pose: types.Pose | None = None
    if "GOAL_POSE" in agent_cfg:
      self._goal_pose = agent_cfg.GOAL_POSE

    self._controller = controller

  def set_velocity(self) -> None:
    pass

  def set_rotational_velocity(self) -> None:
    pass

  def set_forward_velocity(self) -> None:
    pass

  def update(self, world: world_.World) -> None:
    # Controller
    if self._goal_pose is not None:
      self._controller.set_pose(self._pose)
      self._controller.set_goal_pose(self._goal_pose)
      self._velocity = self._controller.calc_velocity()
    # Update pose
    new_pose = [x + dx for x, dx in zip(self._pose, self._velocity)]
    # Collision checking
    if not world.is_pose_occupied(new_pose):
      self._pose = new_pose

  @property
  def x(self) -> float:
    return self._pose[0]

  @property
  def y(self) -> float:
    return self._pose[1]
