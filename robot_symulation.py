import random
'''
Simple symulation of robots collecting items. Only the closest one is used to collect.
All steps are printed one after another and they are separated with line of *
'''
dimension = 10  #dimension of field
max_n = dimension * 2  #max distance
loop_w = 5  #number of loops

robot_1 = {"x":1, "y":1, "z":max_n, "name":1, "score":0, "step":0}
robot_2 = {"x":10, "y":7, "z":max_n, "name":2, "score":0, "step":0}
robot_3 = {"x":4, "y":5, "z":max_n, "name":3, "score":0, "step":0}


robots = (robot_1, robot_2, robot_3)
#diff_robot = max_n
diff_name = ""


crate_x = list(range(1,dimension + 1))  #possible x for wood
crate_y = list(range(1,dimension + 1))  #possible y for wood

def robot_pos(ix, iy):  #checker for robot position
    for variable_robot in robots:
        if ix == variable_robot["x"] and iy == variable_robot["y"]:
            return True
    return False

def wood_random():  #random wood generator
    wood_x = random.choice(crate_x)
    wood_y = random.choice(crate_y)
    while robot_pos(wood_x, wood_y) == True:
        wood_x = random.choice(crate_x)
        wood_y = random.choice(crate_y)

    wood_xy = {"x":wood_x, "y":wood_y}
    return wood_xy  #returning dictionary with wood coordinates (X and Y)


def closest_robot(wood, diff_robot=max_n):  #choosing closest robot
    for variable_robot in robots:
        for xory in variable_robot:
            if xory == "x":
                diff_x = variable_robot[xory] - wood_r["x"]
            if xory == "y":
                diff_y = variable_robot[xory] - wood_r["y"]
        variable_robot["z"] = abs(diff_x) + abs(diff_y)
    for variable_robot in robots:
        if variable_robot["z"] < diff_robot:
            diff_robot = variable_robot["z"]
            diff_name = variable_robot["name"] - 1
    return (robots[diff_name])  #returning robot_n dictionary {"name":?}


def printing():  #printing field with robots and wood
    for ix in range(1, dimension + 1):
        for iy in range(1, dimension + 1):
            if robot_pos(ix, iy) == True:
                if iy == dimension:
                    print(" r ")
                else:
                    print(" r ", end=" ")
            elif ix == wood_r["x"] and iy == wood_r["y"]:
                if iy == dimension:
                    print(" w ")
                else:
                    print(" w ", end=" ")
            else:
                if iy < dimension:
                    print(" . ", end=" ")
                else:
                    print(" . ")

def walking_step():  #walking step for robot - one step at a time. takes notes about score and step
    robots[closest_r["name"] - 1]["step"] += 1
    if closest_r["x"] > wood_r["x"]:
        robots[closest_r["name"] - 1]["x"] = robots[closest_r["name"] - 1]["x"] - 1
    elif closest_r["x"] < wood_r["x"]:
        robots[closest_r["name"] - 1]["x"] = robots[closest_r["name"] - 1]["x"] + 1
    elif closest_r["x"] == wood_r["x"]:
        if closest_r["y"] > wood_r["y"]:
            robots[closest_r["name"] - 1]["y"] = robots[closest_r["name"] - 1]["y"] - 1
        elif closest_r["y"] < wood_r["y"]:
            robots[closest_r["name"] - 1]["y"] = robots[closest_r["name"] - 1]["y"] + 1
    if closest_r["x"] == wood_r["x"] and closest_r["y"] == wood_r["y"]:
        robots[closest_r["name"] - 1]["score"] += 1


while loop_w > 0:  #final loop
    wood_r = wood_random()
    printing()
    closest_r = closest_robot(wood_r)
    while not robot_pos(wood_r["x"], wood_r["y"]):
        print("***************************************")
        walking_step()
        printing()
    loop_w -= 1
    print("#######################################")

for variable_robots in robots:  #printing score and step
    print("Robot nr {} zdobył {} pkt. I przebył {} pól.".format(variable_robots["name"], variable_robots["score"], variable_robots["step"]))