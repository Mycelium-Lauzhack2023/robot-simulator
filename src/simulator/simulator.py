from src.agents import agent as agent_
from src.world import world as world_


class Simulator:  # pylint: disable=too-few-public-methods

  def __init__(
      self,
      world: world_.World,
      agents: list[agent_.Agent],
  ):
    self._world = world
    self._agents = agents

  def step(self) -> None:
    for agent in self._agents:
      agent.update()
