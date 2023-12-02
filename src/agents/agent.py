from src.utils import types


class Agent:

  def __init__(
      self,
      name: str,
      agent_type: types.AgentType,
      starting_pose: types.Pose,
      starting_velocity: types.Velocity,
  ):
    self._name = name
    self._agent_type = agent_type
    self._pose = starting_pose
    self._velocity = starting_velocity

  def set_velocity(self) -> None:
    pass

  def set_rotational_velocity(self) -> None:
    pass

  def set_forward_velocity(self) -> None:
    pass

  def update(self) -> None:
    self._pose = [x + dx for x, dx in zip(self._pose, self._velocity)]

  @property
  def x(self) -> float:
    return self._pose[0]

  @property
  def y(self) -> float:
    return self._pose[1]
