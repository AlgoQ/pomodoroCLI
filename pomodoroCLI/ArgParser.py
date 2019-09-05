import sys
from pomodoroCLI import CONSTS

class ArgParse:
    def __init__(self, args):
        self.args = args
    
    def eventHandler(self):
        withoutEventArg = False
        if len(self.args) > 0:
            withoutEventArg = self.withoutEventArg

        event = self.event
        opts = self.opts

        # Get return dictonairy from "CONSTS.py" and change the event 
        returnDict = CONSTS.returnDict
        returnDict["event"] = event

        # Return help for specific event if needed (if there are opts)
        if len(opts) > 0:
            for item in ["help","-h"]:
                if item in self.opts:
                    returnDict["errorType"] = event
                    return returnDict

        # TODO: Check if there are specific settings about the time of the cycles
        if event == "r":
            if opts == []:
                return returnDict
            elif len(opts) == 1:
                returnDict["workCyc"] = opts[0]

                return returnDict
            elif len(opts) == 2:
                returnDict["workCyc"] = opts[0]
                returnDict["relCyc"] = opts[1]

                return returnDict
            elif len(opts) == 3:
                returnDict["workCyc"] = opts[0]
                returnDict["relCyc"] = opts[1]
                returnDict["bigRelCyc"] = opts[2]
                
                return returnDict
            else:
                returnDict["errorType"] = event

                return returnDict
            
        elif event == "st":
            pass
        elif event == "c":
            pass
        elif event == "se":
            pass
        elif event == "h":
            returnDict["errorType"] = "gen"
            
            return returnDict

    # Properties
    @property
    def event(self):
        try:
            if len(self.args) == 0 or self.withoutEventArg == True:
                event = "r"
            else:
                if self.args[0] in ["run","-r"]:
                    event = "r" 
                elif self.args[0] in ["stats","-st"]:
                    event = "st"
                elif self.args[0] in ["chart","-c"]:
                    event = "c"
                elif self.args[0] in ["settings","-se"]:
                    event = "se"
                elif self.args[0] in ["help","-h"]:
                    event = "h"
                
            return event
        except:
            pass
            # TODO: Add general help + full error message (use same library from "trading bot")
    
    @property
    def opts(self):
        if len(self.args) == 0:
            return []
        elif self.withoutEventArg == True:
            return self.args[0:]
        else:
            return self.args[1:]
    
    @property
    def withoutEventArg(self):
        if self.args[0].isdigit() == 1:
            return True
        else:
            return False
    
    # Functions
    # def loadSpecHelp(self, event):
    #     for item in ["help","-h"]:
    #         if item in self.opts:
    #             pass
    #             # TODO: Get specific event error from "errorMessages.json"
