# Double Pendulum Simulation
---
## Alvin Li and Rishabh Das

This applet simulates the motion of a double pendulum, which is a common example of a chaotic system: one where the behavior of objects vary greatly with small shifts in initial conditions such as the ratio of the lengths of the rods or the initial angles.

The user is able to adjust the following with sliders:
- The lengths of the rods
- The ratio of the masses of bobs
- The intitial angle of either bob with respect to the vertical

Once these conditions are set, the motion of the pendulum is animated in a display window on the right side of the screen. Phase diagrams, or graphs plotting angle against angular velocity, are also drawn for both bobs and updated live as the simulation runs. The user can pause or play the simulation using a button on the top left corner. While the simulation is running, the sliders cannot be changed, but they can be once the user presses the reset button which is also on the top left of the screen. After the initial conditions are set the user can just press 'Play' to watch the simulation play.

This program uses Lagrangians and the Runge-Kutta method of simulating differential equations to predict the movement of the double pendulum. Graphics were rendered with the VPython library.

To run the program, double click the `go.exe` executable. This will only work on Windows.

**Note: To run the program, the user must have VPython installed.** To do so, just type `pip3 install vpython` in the shell.
