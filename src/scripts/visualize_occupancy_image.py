import matplotlib.pyplot as plt

from src.utils import config as cfg_
from src.visualizer import visualizer
from src.world import world as world_


def main() -> None:
  cfg = cfg_.get_default_configs()

  world = world_.World(cfg)
  vis = visualizer.Visualizer(world)

  plt.show()  # Keep plt window alive
  vis.show()


if __name__ == '__main__':
  main()
