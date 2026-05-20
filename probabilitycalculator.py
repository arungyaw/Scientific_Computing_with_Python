import copy
import random

class Hat:
    def __init__(self, **balls):
        #Creates an empty list to store each ball as a color string
        self.contents = []
        #Loop through each color and its quantity
        for color,count in balls.items():
            #Adds the color into contents as many times as its count
            for _ in range(count):
                self.contents.append(color)

    def draw(self, num_balls):
        #Creates an empty list to store the balls that are drawn
        drawn_balls = []
        
        #If asked to draw more balls than available, return all balls
        if num_balls >= len(self.contents):
            drawn_balls = self.contents.copy()
            self.contents.clear()
            return drawn_balls
        
        #Draw one ball at a time
        for _ in range(num_balls):
            #Picks a random index from the contents list
            random_index= random.randrange(len(self.contents))
            
            #Removes the ball from contents and add it to drawn_balls
            drawn_balls.append(self.contents.pop(random_index))
            
        #Returns the list of randomly drawn balls
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    #Counts how many experiments successfully match expected balls
    successful_experiments = 0
    #Runs the experiment many times
    for _ in range(num_experiments):
        #Makes a fresh copy of the hat for this experiment
        hat_copy = copy.deepcopy(hat)
        
        #Draws balls from the copied hat
        drawn_balls = hat_copy.draw(num_balls_drawn)
        
        #Creates a dictionary to count the balls that were draen
        drawn_balls_count = {}
        
        #Count each color in the drawn balls list
        for ball in drawn_balls:
            if ball in drawn_balls_count:
                drawn_balls_count[ball] +=1
            else:
                drawn_balls_count[ball] = 1
        #Let's assume the experiment is successful at first
        success = True
        
        #Checks if each expected color appears enough times
        for color, count in expected_balls.items():
            if drawn_balls_count.get(color, 0) < count:
                success = False 
                break
        #If all expected balls requirements were met, count this experiment
        if success:
            successful_experiments +=1
    #Returns the estimated probability
    return successful_experiments / num_experiments
            

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={'black':2,'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)
print(probability)

    
