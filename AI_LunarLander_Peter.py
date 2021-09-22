# Lunar Lander: AI-controlled play

# Instructions:
#   Land the rocket on the platform within a distance of plus/minus 20, 
#   with a horizontal and vertical speed less than 20
#
# Controlling the rocket:
#    arrows  : Turn booster rockets on and off
#    r       : Restart game
#    q / ESC : Quit

from LunarLander import *
import time

def calculate_std(score_list, mean):
    sum_of_deviations = 0.0
    for s in score_list:
        sum_of_deviations += (s - mean)**2
    
    std = (sum_of_deviations/len(score_list))**0.5
    return std

start_time=time.time() # For the LOLs

scores = []

env = LunarLander()
env.reset()
exit_program = False

while not exit_program:
    env.render()
    (x, y, xspeed, yspeed), reward, done = env.step((boost, left, right)) 

    # Process game events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_program = True
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_ESCAPE, pygame.K_q]:
                exit_program = True
            if event.key == pygame.K_UP:
                boost = True
            if event.key == pygame.K_DOWN:
                boost = False
            if event.key == pygame.K_RIGHT:
                left = False if right else True
                right = False
            if event.key == pygame.K_LEFT:
                right = False if left else True
                left = False
            if event.key == pygame.K_r:
                boost = False        
                left = False
                right = False
                env.reset()

    # INSERT YOUR CODE HERE
    #
    # Implement a Lunar Lander AI 
    # Control the rocket by writing a list of if-statements that control the 
    # three rockets on the lander 
    #
    # The information you have available are x, y, xspeed, and yspeed
    # 
    # You control the rockets by setting the variables boost, left, and right
    # to either True or false
    #
    # Example, to get you started. If the rocket is close to the ground, turn
    # on the main booster

    ########################
    # Center rocket
    ########################
    if x < 0:
        left = True
    else:
        left = False

    if x > 0:
        right = True
    else:
        right = False
    
    ########################
    # Control horizontal speed
    ########################
    if xspeed > 18:
        left = False
    if xspeed < -18:
        right = False
    
    ########################
    # Control booster to center rocket
    ########################
    if (yspeed > 18 and abs(x) < 100) or y < 175:
        boost = True
    if (yspeed < 18 and y < 175 and abs(x) < 100) or y > 175:
        boost = False
    
    ########################
    # Disable left & right boosters if over platform
    ########################
    if abs(x) < 14 and abs(xspeed) <= 1:
        left = right = False
    
    ########################
    # Boost if the rocket is about to land on the ground instead of the platform
    ########################
    if abs(x) > 30 and y < 20:
        boost = True
    
    # Modify and add more if-statements to make the rocket land safely
    # END OF YOUR CODE

    if done:
        scores.append(reward)
        if reward == 0:
            print("Crash!");
        
        if len(scores) == 1537:
            print("_______________Scores_____________________")
            average = sum(scores)/len(scores)
            std = calculate_std(scores, average)
            print("Average: ", average)
            print("Standard deviation: ", std)
            # print(scores)
            exit_program = True
        else:
            env.reset()

end_time=time.time()-start_time
print("Time elapsed: ", end_time)
env.close()