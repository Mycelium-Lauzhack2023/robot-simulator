import jaxtyping
import networkx as nx
import numpy as np
from rrtplanner import rrt
from yacs import config as cfg_

from src.utils import types

Position = jaxtyping.UInt8[np.ndarray, "2"]


class Planner:  # pylint: disable=too-many-instance-attributes

  def __init__(self, planner_cfg: cfg_.CfgNode):
    self._pose: types.Pose = []
    self._global_goal_pose: types.Pose = []

    self._num_samples = planner_cfg.NUM_SAMPLES
    self._rewire_radius = planner_cfg.REWIRE_RADIUS
    self._occupancy_grid: types.OccupancyGrid = np.zeros(
        (planner_cfg.OCCUPANCY_GRID_HEIGHT, planner_cfg.OCCUPANCY_GRID_WIDTH),
        dtype=np.uint8,
    )

    self._rrt = rrt.RRTStar(self._occupancy_grid, self._num_samples, self._rewire_radius, pbar=False)
    self._path: nx.Graph | None = None

  def set_pose(self, pose: types.Pose) -> None:
    self._pose = pose

  def set_global_goal_pose(self, global_goal_pose: types.Pose) -> None:
    self._global_goal_pose = global_goal_pose

  def set_occupancy_grid(self, occupancy_grid: types.OccupancyGrid) -> None:
    self._occupancy_grid = occupancy_grid
    self._rrt.set_og(self._occupancy_grid)

  def calc_plan(self) -> list[types.Pose]:
    self._assert_initialized()
    self._path, goal_node_idx = self._rrt.plan(*self._get_start_and_goal())
    shortest_path = self._rrt.route2gv(self._path, goal_node_idx)
    plan = []
    for node_idx in shortest_path:
      node_position = self._path.nodes[node_idx]["pt"]
      plan.append([node_position[1], node_position[0], 0])
    return plan

  def _assert_initialized(self) -> None:
    if not self._pose or not self._global_goal_pose:
      raise RuntimeError("Planner pose and goal pose must be initialized")

  def _get_start_and_goal(self) -> tuple[Position, Position]:
    return np.array(self._pose[:2]).astype(np.uint32), np.array(self._global_goal_pose[:2]).astype(np.uint32)

  @property
  def path(self) -> nx.Graph:
    self._assert_initialized()
    return self._path
