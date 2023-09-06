# Team: Akash Vidyadharan, Maya Dunlap, Sai Kishore Neppali and Venkata Nagendar Reddy

import math as m

# This is the first program
print("Hello World")

num_int = 10 # this is an integer

num_float = 0.5 # this number is a float

print(num_int * (num_int + num_float))

print(num_int % 3)

print(max(num_int, 9))

print(abs(-num_int))

print(pow(num_int, 2))

print(round(num_float))

from math import *
#import math as m is alternative

print(floor(num_float))

print(ceil(num_float))

print(sqrt(num_int))

print(exp(num_int))

#import math as m
print(exp(num_int))

print("There are " + str(num_int) + " arm robots in the factory, " + str(num_float) + " of them are broken.")

print("There are", num_int, "arm robots in the factory,", num_float, "of them are broken.")

factory_name = "ABC"
print("The factory’s name is " + factory_name)

print("The first character in the factory name is " + factory_name[0])
print("The third character in the factory name is " + factory_name[2])

print(factory_name.lower())
print(factory_name.islower())

print(factory_name.upper().isupper())
print(len(factory_name))
print(factory_name[0:len(factory_name)-1])

print(factory_name.index("A"))

print(factory_name.replace("ABC", "DEF"))


##################LISTS#####################

robot_brands = ["ABB", "KUKA", "FANUC", "Omron"]
print(robot_brands)

print(robot_brands[1])

print(robot_brands[:3])

robot_brands.append("UR")
print(robot_brands)

robot_brands.remove("UR")
print(robot_brands)

robot_brands.insert(1, "UR")
print(robot_brands)

robot_brands.sort()
print(robot_brands)

robot_brands.reverse()
print(robot_brands)

print(len(robot_brands))

robot_brands_1 = ["Yaskawa", "Staubli"]
robot_brands.extend(robot_brands_1)
print(robot_brands)

robot_brands.pop()
print(robot_brands)

print(robot_brands.index("ABB"))

print(robot_brands.count("ABB"))

robot_brands2 = robot_brands.copy()
print(robot_brands)
print(robot_brands2)


for robot_brand in robot_brands:
    print(robot_brand)


robot_brands.clear()
print(robot_brands)

###################2D Lists######################

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)

print(matrix[0][0])

print(matrix[1][2])



#################################################

######################Tuple######################

robotic_engineers = ("Hannah", "Jim", "Bella", "John")
print(robotic_engineers[1])

e1, e2, e3, e4 = robotic_engineers
print(e1, e2, e3, e4)

# Robotic_engineers[1] = "Bob"
# got an error when trying to change tuple

robotic_partners = [("Hannah", "John"), ("Jim","Bella")]
print(robotic_partners)
print(robotic_partners[0])

###################Dictionaries####################

objects_colors = {
    "ball": "red",
    "cube": "green",
    "flower": "pink",
    "pyramid": "blue"
}

print("the ball is " + objects_colors["ball"])
print("the cube is " + objects_colors["cube"])

print(objects_colors.get("floer", "no such object"))

# Testing 
object_color_mapping = {
    'apple': 'red',
    'banana': 'yellow',
    'grapes': 'purple',
    'lemon': 'yellow',
    'orange': 'orange',
    'blueberry': 'blue',
    'lettuce': 'green',
    'eggplant': 'purple'
}

print(object_color_mapping["lemon"])


# a dictionary that maps robot arm joints to their corresponding min, max, and default joint angles
import math as m

arm_dict = {
    "joint1": {
        "min" : -m.pi/2,
        "max" : m.pi/2,
        "default" : 0,
    },

        "joint2": {
        "min" : -m.pi,
        "max" : m.pi,
        "default" : 0,
    },

        "joint3": {
        "min" : -m.pi/2,
        "max" : m.pi/2,
        "default" : 0,
    },
}

joint_angles_1 = arm_dict["joint1"]
print(joint_angles_1)

print(arm_dict["joint2"]["max"])

print(arm_dict["joint3"]["min"])

###################################################

####################Functions######################

def add(a, b):
    return a + b

total = add(3, -1)
print(total)


# this function will get the radius of the wheel and returns the area of the wheel
def calc_wheel_area(radius):
    area = m.pi * radius**2
    return area

# now we want to call this function
wheel_radius = 0.2 # 0.2 meters
wheel_area = calc_wheel_area(wheel_radius)
print("The area of this wheel is", wheel_area)

#################Conditional Statements#####################

joystick_in = "right"

if joystick_in == "right":
    print("moving 1st joint in positive direction")
elif joystick_in == "left":
    print("moving 1st joint in negative direction")
elif joystick_in == "up":
    print("moving the 2nd joint in positive direction")
elif joystick_in == "down":
    print("moving the 2nd joint in the negative direction")
else:
    print("the joystick is in the neutral position, no movement")


# Conditional for robot obstacle aboidance


sensor1_dist = 1.5 # distance read by sensor 1 in meters
sensor2_dist = 1.2 # distance read by sensor 2 in meters
threshold_dist = 1 # threshold distance for considering an obstacle in meters


if sensor1_dist < threshold_dist or sensor2_dist < threshold_dist:
    print("Warning: obstacle detected! Stopping!")
else:
    print("No obstacle, moving forward!")

# in this example we want to write a function that gives us the minimum number of three numbers that we pass to it

def min_num(a,b,c):
    if a < b and a < c:
        return "The smallest number is " + str(a)
    elif b < a and b < c:
        return "The smallest number is " + str(b)
    elif c < a and c < b:
        return "The smallest number is " + str(c)
    else:
        return "They are equal"
    
print(min_num(-2,-1,0))

#################While Loops#####################

# in this example we want to simulate a situation where a robot moves forward until it encounters an obstacle
import time
import random 

# the move_robot() function simulates the robot's movement

def move_robot(distance):
    print("Moving robot forward ...")
    # now we want to simulate the time it takes for the robot to move forward by giving some delay
    time.sleep(1)
    print(f"The robot has moved {distance} units.")
    # note that f"..." is used to create formatted string literals aka f-strings 
    # it is introduced in python 3.6 and allows you to embed expressions inside string literals


# now we should write a function for obstacle detection
def detect_obstacle():
    # simulating obstacle detection
    obstacle = random.choice([True, False])
    return obstacle 
# the random.choice() function is part of the random module in python
# it allows you to select a random element from a sequence such as a list, tuple or string 
# because we are simulating a situation here and we do not have real obstacles we randomly choose whenever an obstacle is present

# robot's initial position
position = 0

# we will keep moving the robot until an obstacle is detected
while not detect_obstacle():
    # now we should generate a random distance to move fw (because we are simulating and it's not a real scenario)
    distance = random.randint(1, 5)
    # here we call the move_robot() function to move the robot fw by the randomly generated distance 
    move_robot(distance)
    # now we will add this distance to the position of the robot
    # here we update the position of the robot
    position += distance

# here the while loop continues to execute as long as the detect_obstacle() function returns False meaning that there is no obstacle. 
# if it becomes True, then it means that there is an obstacle and the loop is exited and a message will print showing that there is an obstacle
# and the control system should take action accordingly and commands the actuators to stop the robot

print("Obstacle is detected! Stopping the robot.")
# we also print the final position of the robot
print(f"The final position of the robot is {position}")


######################FOR Loops#########################

for letter in "Robotics":
    print(letter)

robotics_engineers = ["Tim", "Hannah", "John", "Bella"]
for re in robotics_engineers:
    print(re)

for index in range(len(robotics_engineers)):
    print(index)
    print(robotics_engineers[index])

for number in range(3, 10):
    print(number)

####################Nested Loops#########################

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in matrix:
    for element in row:
        print(element)

##################Classes & Objects###################
#Importing from the file robotarm.py 

from RobotArm import RobotArm

#The first RobotArm refers to RobotArm.py and the second refers to the class name

arm1 = RobotArm("Armrob", 50, 10, "Black")
arm1.move(45)
arm1.display_info()

arm1.move(-15)
arm1.display_info()

######################EXCEPT#####################

def divide_numbers(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("Division by zero error")

print(divide_numbers(10, 0))
print(divide_numbers(10, 5))
