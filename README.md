# Project Mycelium: robot-simulator

Project Mycelium addresses the problem of logistic bottleneck by introducing a fleet of autonomous robots capable of dynamically navigating diverse environments.
This fleet of autonomous robots have applications in multiple sectors, such as healthcare, retail, manufacturing and entertainment.

In this repository, a bespoke robot simulator is implemented to simulate a fleet of autonomous robots.
It also contains a bespoke navigation stack to enable these robots to navigate to any predifined target position.

## Demo

The 3 agents (blue) in the GIF below are navigating to their goal position autonomously.
There is no pre-programmed path.

![Fleet of autonomous agents](https://github.com/Lauzhack2023/robot-simulator/blob/main/autonomous_multi_agent_navigation.gif)

For this demo, the RRT* Algorithm is used as the planner in the navigation stack.

![RRT visualization](https://github.com/Lauzhack2023/robot-simulator/blob/main/RRT.gif)

This project is developed as part of the LauzHack 2023 event.
Team members: Dominic Wong, Muhammad Aman
