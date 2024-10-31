import copy
import random

class Hat:
    def __init__(self, **balls):
        # Initialize contents with the specified number of each color ball
        self.contents = []
        for color, count in balls.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        # If the number of balls to draw exceeds the available balls, return all balls
        if num_balls >= len(self.contents):
            drawn_balls = self.contents[:]
            self.contents = []
        else:
            # Randomly draw the specified number of balls
            drawn_balls = random.sample(self.contents, num_balls)
            # Remove the drawn balls from the hat
            for ball in drawn_balls:
                self.contents.remove(ball)
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0

    for _ in range(num_experiments):
        # Create a copy of the hat to reset for each experiment
        temp_hat = copy.deepcopy(hat)
        
        # Perform the draw
        drawn_balls = temp_hat.draw(num_balls_drawn)
        
        # Count the drawn balls
        drawn_counts = {color: drawn_balls.count(color) for color in set(drawn_balls)}
        
        # Check if the drawn balls meet the expected criteria
        success = True
        for color, count in expected_balls.items():
            if drawn_counts.get(color, 0) < count:
                success = False
                break
        
        if success:
            successful_experiments += 1

    return successful_experiments / num_experiments

# Example usage
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                        expected_balls={'red': 2, 'green': 1},
                        num_balls_drawn=5,
                        num_experiments=2000)
print(probability)