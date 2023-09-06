from WheeledRobot import WheeledRobot
from FlyingRobot import FlyingRobot 

robot1 = WheeledRobot("Rover", 3, 4)
robot1.introduce() # this is the introduce function that we created in the Robot class and WheeledRobot class inherited from it
robot1.move() # this will provide its own definition of the move function and also the inherited move function from the Robot class


robot2 = FlyingRobot("DroneX", 6, 100)
robot2.introduce()
robot2.move()