# Turtle Figure Eights and Xacro Arm
## About This Package
#### Creator
Cody Nichoson

#### Overview 
This package carries out two unrelated processes. The first process involves having a Turtlebot traverse a figure eight trajectory in turtlesim, rviz, and ultimately in the real world. The second process involves visualizing a simple two link mechanical arm in rviz and experimenting with several available features in the software to manipulate the system.

## Video Demonstration Links
#### Turtlesim Figure Eight
https://youtu.be/26ZRERuD0xw
#### Turtlebot in rviz Figure Eight
https://youtu.be/OWYyptBH-iE
#### Turtlebot3 Figure Eight
https://youtu.be/TIIPveBU0p4
#### Xacro Arm Without Markers
https://youtu.be/caACK5UqpRQ (No GUI)

https://youtu.be/tpZbc0XvRJs (with GUI)
#### Xacro Arm With Markers
https://youtu.be/r6dQEYMVCs8 (No GUI)

https://youtu.be/VD39wRVtp6o (with GUI)

## Usage Instructions
### Part 1A - Turtlesim/rviz Figure Eight
1. Run the figure eight launchfile in simulation mode using the command `roslaunch homework-2-codynichoson figure_eight.launch`.
2. You should notice that both `turtlesim` and `rviz` open to display a cartoon turtle and turtlebot3, respectively. The two turtles will be stationary.
3. Begin the figure eight trajectory by opening a new terminal window and running the command `rosservice call /resume`.
4. If you want to pause the figure eight trajectory, run the command `rosservice call /pause`.
5. Watch as both the `turtlesim` and `rviz` turtles respond to the service calls.

### Part 1B - Turtlebot3 Figure Eight
#### Note: These procedures require the use of a Turtlebot3 Burger robot.
1. If you have not already done so, clone the `turtlebot3` and `turtlebot3_msgs` repositories so that they are on the same directory level as this package.
```
git clone git@github.com:ROBOTIS-GIT/turtlebot3.git
```
```
git clone git@github.com:ROBOTIS-GIT/turtlebot3_msgs.git
```
2. Turn on the Turtlebot and take note of its name or IP address (e.g. Donatello)
3. Activate the `turtle` network using the the command `nmcli con up turtle`
4. Log in to the turtlebot using the command `ssh msr@donatello`. If not logged in automatically, use the command `ssh-add ~/.ssh/id_turtle`.
5. Confirm that the `ROS_MASTER_URI` on the Turtlebot matches that of your own computer using the command `echo $ROS_MASTER_URI`. If not, run the command `export ROS_MASTER_URI:http://<hostname>:11311` where `<hostname>` is the name of your computer. **You should confirm that the `ROS_MASTER_URI` matches in this manner for every new terminal window you open.**
6. In a new terminal window, run `roscore`. (This should be from your computer, not the Turtlebot)
7. In the original terminal window in which you connected to the Turtlebot, run `roslaunch turtlebot3_bringup turtlebot3_robot.launch`.
8. In a new terminal window, run the figure eight launchfile in "real" mode using `roslaunch homework-2-codynichoson figure_eight.launch mode:=real`.
9. In a new terminal window, run `rosservice call /resume` to start moving the Turtlebot in the figure eight trajectory.
10. If you wish to pause the Turtlebot's trajectory, run `rosservice call /pause`. Run `rosservice call /resume` to start the Turtlebot once more.

#### Configuration Changes
The dimensional properties of the figure eight and time period of the pattern can be adjusted in the `trajectory.yaml` file found in `homework-2-codynichoson/config/trajectory.yaml`.
  
### Part 2 - Xacro Arm
#### Without End-Effector Markers
1. To run the xacro arm visualization with a moving trajectory pattern, run `roslaunch homework-2-codynichoson arm_basics.launch`.
2. To run the xacro arm visualization without a moving trajectory but with an interactive joint GUI, run `roslaunch homework-2-codynichoson arm_basics.launch use_jsp:=true`.
#### With End-Effector Markers
1. To run the xacro arm visualization with a moving trajectory pattern and end-effector markers, run `roslaunch homework-2-codynichoson arm_mark.launch`.
2. To run the xacro arm visualization without a moving trajectory but with an interactive joint GUI and end-effector markers, run `roslaunch homework-2-codynichoson arm_mark.launch use_jsp:=true`.

#### Configuration Changes
The dimensional properties of the arm links and time period of the pattern can be adjusted in the `arm.yaml` file found in `homework-2-codynichoson/config/arm.yaml`.