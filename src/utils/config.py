from yacs import config as cfg


def get_default_configs() -> cfg.CfgNode:
  default_configs = cfg.CfgNode()

  default_configs.SCENARIO = cfg.CfgNode()
  default_configs.SCENARIO.WIDTH = 1024
  default_configs.SCENARIO.HEIGHT = 1024
  default_configs.SCENARIO.OCCUPANCY_GRID_FILE = "scenario/default.npy"

  default_configs.AGENT = cfg.CfgNode()
  default_configs.AGENT.AGENTS_CONFIG_FILE = "configs/default_agents_cfg.yaml"

  return default_configs
