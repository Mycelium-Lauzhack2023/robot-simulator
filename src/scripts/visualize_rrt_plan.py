import matplotlib.pyplot as plt

from src.agent import agent_factory
from src.agent import planner as planner_
from src.utils import config as cfg_
from src.world import world as world_


def main() -> None:
  cfg = cfg_.get_default_configs()
  world = world_.World(cfg)
  planner = planner_.Planner(cfg.AGENT.PLANNER)
  agents = agent_factory.create_agents(cfg.AGENT)

  plt.imshow(world.occupancy_grid, cmap='gray')

  for agent in agents:
    planner.set_pose(agent.pose)
    planner.set_global_goal_pose(agent.global_goal_pose)
    planner.set_occupancy_grid(world.occupancy_grid)
    plan = planner.calc_plan()
    path = planner.path

    for edge in path.edges:
      x = [path.nodes[edge[0]]["pt"][1], path.nodes[edge[1]]["pt"][1]]
      y = [path.nodes[edge[0]]["pt"][0], path.nodes[edge[1]]["pt"][0]]
      plt.plot(x, y, 'r-')

    x = [pose[0] for pose in plan]
    y = [pose[1] for pose in plan]
    plt.plot(x, y, 'b-')
    plt.scatter(agent.pose[1], agent.pose[0], c='g', marker='o')
    plt.scatter(agent.global_goal_pose[1], agent.global_goal_pose[0], c='r', marker='o')

  plt.axis('off')
  plt.show()


if __name__ == '__main__':
  main()
