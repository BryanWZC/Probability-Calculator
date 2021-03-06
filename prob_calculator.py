import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.dict = kwargs
        self._get_contents()
    
    # Get key from dict into contents
    def _get_contents(self):
        self.contents = []
        for k, v in self.dict.items():
            for i in range(0, v):
                self.contents.append(k)
    
    # draw balls from hat
    def draw(self, num):
        self._get_contents()
        
        if num > len(self.contents):
            return self.contents
        
        draw = []

        while(num > 0):
            rand_index = random.randrange(0, len(self.contents))
            rand_content = self.contents.pop(rand_index)
            draw.append(rand_content)
            num -= 1
        
        return draw

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected_balls_copy = copy.deepcopy(expected_balls)
    success = 0

    for i in range(0, num_experiments):
        drawn_balls = hat.draw(num_balls_drawn)
        test_success = True

        # For each drawn ball, check if it meets expected and subtract from quantity
        for i in drawn_balls:
            if i in expected_balls_copy and expected_balls_copy[i]:
                expected_balls_copy[i] -= 1
        
        # Check each quantity for expected balls and if greater than 0, experiment fails
        for key, val in expected_balls_copy.items():
            if(val):
                test_success = False

        # If experiment is successful, increase success counter by 1
        if(test_success):
            success += 1

        # set new copy of expected balls for nexxt experiment
        expected_balls_copy = copy.deepcopy(expected_balls)

    return float(success) / num_experiments
        
