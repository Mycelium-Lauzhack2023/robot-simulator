from yacs import config as cfg


def get_default_configs() -> cfg.CfgNode:
  default_configs = cfg.CfgNode()

  default_configs.SCENARIO = cfg.CfgNode()
  default_configs.SCENARIO.WIDTH = 1000
  default_configs.SCENARIO.HEIGHT = 1000
  default_configs.SCENARIO.OCCUPANCY_GRID_FILE = "scenario/demo.npy"

  default_configs.AGENT = cfg.CfgNode()
  default_configs.AGENT.AGENTS_CONFIG_FILE = "configs/default_agents_cfg.yaml"

  default_configs.AGENT.CONTROLLER = cfg.CfgNode()
  default_configs.AGENT.CONTROLLER.MAX_SPEED = 4.0
  default_configs.AGENT.CONTROLLER.MAX_YAW_RATE = 1.0
  default_configs.AGENT.CONTROLLER.GOAL_REACHED_THRESHOLD = 5.0

  default_configs.AGENT.PLANNER = cfg.CfgNode()
  default_configs.AGENT.PLANNER.NUM_SAMPLES = 7000
  default_configs.AGENT.PLANNER.REWIRE_RADIUS = 25.0
  default_configs.AGENT.PLANNER.OCCUPANCY_GRID_WIDTH = 1000
  default_configs.AGENT.PLANNER.OCCUPANCY_GRID_HEIGHT = 1000

  return default_configs
