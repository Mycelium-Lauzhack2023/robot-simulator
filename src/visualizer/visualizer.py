import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from src.agents import agent as agent_
from src.utils import types
from src.world import world as world_

matplotlib.rcParams["toolbar"] = "None"


class Visualizer:

  def __init__(self, world: world_.World, agents: list[agent_.Agent]):
    self._world = world
    self._agents = agents

    self._fig, self._ax = plt.subplots()
    self._img = self._ax.imshow(self._world.occupancy_grid, cmap='gray', interpolation='none')
    self.update()

  def update(self) -> None:
    image = self._world.occupancy_grid
    image = 1 - image  # Invert colors
    image = np.stack((image,) * 3, axis=-1)
    image = image * 255

    # Draw agents
    for agent in self._agents:
      image = self._draw_agent(image, agent)

    self._img.set_array(image)

  def show(self) -> None:
    self._ax.plot([0, 1], [1, 0])
    self._fig.canvas.draw()

  def _draw_agent(self, image: types.Image, agent: agent_.Agent) -> types.Image:
    height, width = image.shape[:2]
    x, y = agent.x, agent.y
    tl_x, tl_y, br_x, br_y = int(x - 10), int(y - 10), int(x + 10), int(y + 10)
    tl_x = max(0, tl_x)
    tl_y = max(0, tl_y)
    br_x = min(width, br_x)
    br_y = min(height, br_y)
    # Agents are blue
    image[tl_y:br_y, tl_x:br_x, 0] = 0
    image[tl_y:br_y, tl_x:br_x, 1] = 0
    return image
