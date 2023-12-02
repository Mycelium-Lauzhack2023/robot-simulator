import numpy as np
from yacs import config as cfg_

from src.utils import types


class World:  # pylint: disable=too-few-public-methods

  def __init__(self, cfg: cfg_.CfgNode):
    self._width = cfg.SCENARIO.WIDTH
    self._height = cfg.SCENARIO.HEIGHT
    self._occupancy_grid_file = cfg.SCENARIO.OCCUPANCY_GRID_FILE
    self._occupancy_grid: types.OccupancyGrid = np.zeros((self._height, self._width), dtype=np.uint8)
    self._load_scenario()

  def is_pixel_occupied(self, x: int, y: int) -> bool:
    return self._occupancy_grid[y, x] == 1

  @property
  def occupancy_grid(self) -> types.OccupancyGrid:
    return self._occupancy_grid

  def _load_scenario(self) -> None:
    self._occupancy_grid = np.load(self._occupancy_grid_file).astype(np.uint8)
