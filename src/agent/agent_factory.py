import yaml
from yacs import config as cfg_

from src.agent import agent as agent_
from src.agent import controller as controller_
from src.agent import planner as planner_
from src.utils import types


def create_agents(agents_cfg: cfg_.CfgNode) -> list[agent_.Agent]:

  agents_cfg_file = agents_cfg.AGENTS_CONFIG_FILE
  with open(agents_cfg_file, encoding="utf-8") as f:
    agents_cfg_ = yaml.safe_load(f)

  agents = []

  for agent_cfg in agents_cfg_["AGENTS"]:
    agent_type = _str_to_agent_type(agent_cfg["TYPE"])
    agent_cfg_node = cfg_.CfgNode(agent_cfg)
    if agent_type == types.AgentType.HOLONOMIC:
      planner = planner_.Planner(agents_cfg.PLANNER)
      controller = controller_.Controller(agents_cfg.CONTROLLER)
      agent = agent_.Agent(agent_cfg_node, controller, planner)
    elif agent_type == types.AgentType.DUBINS:
      raise NotImplementedError("Dubins agent not implemented")
    else:
      raise ValueError(f"Unknown agent type: {agent_type}")
    agents.append(agent)

  return agents


def _str_to_agent_type(type_str: str) -> types.AgentType:
  if type_str.lower() == "holonomic":
    return types.AgentType.HOLONOMIC
  if type_str.lower() == "dubins":
    return types.AgentType.DUBINS
  raise ValueError(f"Unknown agent type: {type_str}")
