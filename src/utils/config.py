from yacs import config as cfg


def get_default_configs() -> cfg.CfgNode:
  default_configs = cfg.CfgNode()

  default_configs.SCENARIO = cfg.CfgNode()
  default_configs.SCENARIO.WIDTH = 1024
  default_configs.SCENARIO.HEIGHT = 1024
  default_configs.SCENARIO.OCCUPANCY_GRID_FILE = "scenario/default.npy"

  return default_configs
