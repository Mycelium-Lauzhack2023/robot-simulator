import numpy as np
from yacs import config as cfg_

from src.agent import controller as controller_
from src.agent import planner as planner_
from src.utils import types
from src.world import world as world_


class Agent:  # pylint: disable=too-many-instance-attributes

  def __init__(
      self,
      agent_cfg: cfg_.CfgNode,
      controller: controller_.Controller,
      planner: planner_.Planner,
  ):
    self._name: str = agent_cfg.NAME
    self._pose = agent_cfg.STARTING_POSE
    self._velocity = agent_cfg.STARTING_VELOCITY

    self._global_goal_pose = agent_cfg.GOAL_POSE
    self._local_goal_poses: list[types.Pose] = []

    self._controller = controller
    self._planner = planner

    self._replan = True

  def update(self, world: world_.World) -> None:
    if self._replan:
      self._plan(world.occupancy_grid)
      self._replan = False
    self._move_to_next_local_goal_pose()
    for i in range(2):
      new_pose_ = np.array(self._pose)
      new_pose_[i] = self._pose[i] + self._velocity[i] * 2
      if world.is_pose_occupied([new_pose_[0], new_pose_[1], 0]):
        self._velocity[i] = 0
    new_pose = [x + dx for x, dx in zip(self._pose, self._velocity)]
    if not world.is_pose_occupied(new_pose):
      self._pose = new_pose
    else:
      self._velocity = [0, 0, 0]
      self._replan = True
    if self._is_goal_reached():
      self._velocity = [0, 0, 0]
      self._replan = False

  def _plan(self, occupancy_grid: types.OccupancyGrid) -> None:
    self._planner.set_pose(self._pose)
    self._planner.set_global_goal_pose(self._global_goal_pose)
    self._planner.set_occupancy_grid(occupancy_grid)
    self._local_goal_poses = self._planner.calc_plan()

  def _move_to_next_local_goal_pose(self) -> None:
    if len(self._local_goal_poses) == 0:
      self._velocity = [0, 0, 0]
      self._replan = True
      return
    next_local_goal_pose = self._local_goal_poses[0]
    self._controller.set_pose(self._pose)
    self._controller.set_goal_pose(next_local_goal_pose)
    self._velocity = self._controller.calc_velocity()
    if self._controller.is_goal_reached():
      self._local_goal_poses.pop(0)

  def _is_goal_reached(self) -> bool:
    return all(abs(self._pose[i] - self._global_goal_pose[i] < 5) for i in range(2))

  @property
  def x(self) -> float:
    return self._pose[0]

  @property
  def y(self) -> float:
    return self._pose[1]

  @property
  def pose(self) -> types.Pose:
    return self._pose

  @property
  def global_goal_pose(self) -> types.Pose:
    return self._global_goal_pose
