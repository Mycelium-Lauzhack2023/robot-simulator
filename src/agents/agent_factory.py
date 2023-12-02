import yaml
from yacs import config as cfg_

from src.agents import agent as agent_
from src.utils import types


def create_agents(agents_cfg: cfg_.CfgNode) -> list[agent_.Agent]:

  agents_cfg_file = agents_cfg.AGENTS_CONFIG_FILE
  with open(agents_cfg_file, encoding="utf-8") as f:
    agents_cfg_ = yaml.safe_load(f)

  agents = []

  for agent_cfg in agents_cfg_["AGENTS"]:
    agent_type = _str_to_agent_type(agent_cfg["TYPE"])
    agent = agent_.Agent(
        name=agent_cfg["NAME"],
        agent_type=agent_type,
        starting_pose=agent_cfg["STARTING_POSE"],
        starting_velocity=agent_cfg["STARTING_VELOCITY"],
    )
    agents.append(agent)

  return agents


def _str_to_agent_type(type_str: str) -> types.AgentType:
  if type_str.lower() == "holonomic":
    return types.AgentType.HOLONOMIC
  if type_str.lower() == "dubins":
    return types.AgentType.DUBINS
  raise ValueError(f"Unknown agent type: {type_str}")
