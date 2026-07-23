import time

class Timer:
    '''Create a chronometer'''
    def __init__(self) :
        self.initial = 0
        self.current = 0
        self.time_passed = 0
        self.run_state = False

    def start(self):
        self.initial = time.time()
        self.run_state = True

    def stop(self):
        '''Stop the chronometer'''
        self.run_state = False
        self.initial = 0
        self.current = 0

    def update(self):
        if self.run_state :
            self.current = time.time()
            self.time_passed = round(self.current - self.initial)

