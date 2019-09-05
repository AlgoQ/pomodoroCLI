from pomodoroCLI import CONSTS
import time

class CycMan: # CycleManager
    def __init__(self, workCyc, relCyc, bigRelCyc):
        self.workCyc = workCyc
        self.relCyc = relCyc
        self.bigRelCyc = bigRelCyc
        self.i = 1
    
    def cycle(self):
        if self.i == 1:
            self.workCycle()
        else:
            pass
            enter = input("Press enter to start a new cycle")
            if enter == "":
                self.workCycle()
            

        if self.i < 4:
            self.relaxCycle()
        else:
            self.bigRelaxCycle()
    
    def restart(self):
        print("Congratulations you've completed a hole set!")
        enter = input("Press enter to start new set (4 cycles)")
        if enter == "":
            self.workCycle()

    def workCycle(self):
        print("\a")
        print("A work cycle of %i minutes is been started, let's work!" % self.workCyc)
        time.sleep(self.workCyc * 60)
        self.relaxCycle()
    
    def relaxCycle(self):
        print("\a")
        self.i += 1
        print("Good job! Enjoy your relax cycle of %i minutes" % self.relCyc)
        time.sleep(self.relCyc * 60)
        self.cycle()
    
    def bigRelaxCycle(self):
        print("\a")
        self.i = 1
        print("Enjoy your big relax cycle of %i minutes." % self.bigRelCyc)
        time.sleep(self.bigRelCyc * 60)
        self.cycle()