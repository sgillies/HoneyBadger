
import time

class HoneyBadger:
    
    is_hungry = True
    is_gross = True
    has_fear = False
    gives_a_shit = False
    bee_stings = 0

    def eatSnake(self, snake):
        return 1

    def fightSnake(self, snake):
        return 1

    def runInSlowMotion(self):
        return 1

    def sleepOffVenomDose(self):
        time.sleep(5)
        return 1
    
    def eatLarvae(self):
        for i in range(1000):
            self.bee_stings += 1
        return 1
