import time

import matplotlib.pyplot as plt

from src.agents import agent_factory
from src.simulator import simulator as sim_
from src.utils import config as cfg_
from src.visualizer import visualizer
from src.world import world as world_


def main() -> None:
  cfg = cfg_.get_default_configs()

  world = world_.World(cfg)
  agents = agent_factory.create_agents(cfg.AGENT)
  simulator = sim_.Simulator(world, agents)
  vis = visualizer.Visualizer(world, agents)

  vis.show()

  for _ in range(100):
    simulator.step()
    vis.update()

    plt.pause(0.01)  # Pause for 0.01 seconds
    time.sleep(0.1)


if __name__ == '__main__':
  main()
