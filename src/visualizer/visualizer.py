import matplotlib
import matplotlib.pyplot as plt

from src.world import world as world_

matplotlib.rcParams["toolbar"] = "None"


class Visualizer:

  def __init__(self, world: world_.World):
    self._world = world

    self._fig, self._ax = plt.subplots()
    self._img = self._ax.imshow(self._world.occupancy_grid, cmap='gray', interpolation='none')
    self.update()

  def update(self) -> None:
    occupancy_grid = self._world.occupancy_grid
    occupancy_grid = 1 - occupancy_grid  # Invert colors
    self._img.set_array(occupancy_grid)

  def show(self) -> None:
    self._ax.plot([0, 1], [1, 0])
    self._fig.canvas.draw()
