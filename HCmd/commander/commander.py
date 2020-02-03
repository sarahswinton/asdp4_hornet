"""
This commander shell will be a implementation of the PX4 'commander' CLI (https://docs.px4.io/v1.9.0/en/flight_modes/).

Here you can switch modes on the go. Will require root access for safety reasons.
"""



from cmd import Cmd
import logger

banner = """


   _____ ____  __  __ __  __          _   _ _____  ______ _____  
  / ____/ __ \|  \/  |  \/  |   /\   | \ | |  __ \|  ____|  __ \ 
 | |   | |  | | \  / | \  / |  /  \  |  \| | |  | | |__  | |__) |
 | |   | |  | | |\/| | |\/| | / /\ \ | . ` | |  | |  __| |  _  / 
 | |___| |__| | |  | | |  | |/ ____ \| |\  | |__| | |____| | \ \ 
  \_____\____/|_|  |_|_|  |_/_/    \_\_| \_|_____/|______|_|  \_\
                                                                 
                                                                 

"""

log = logger.get_logger(__name__)

def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(arg.split())


class CommanderCmd(Cmd):
    intro = banner+ "\nType ? to see a list of available commands"
    prompt = "Commander > "
    
    #Takeoff    Auto    [Position fix required (e.g. GPS)]      Vehicle initiates the takeoff sequence using either catapult/hand-launch mode or runway takeoff mode (in the current direction).
    def do_takeoff(self, inp):
        pass
    def help_takeoff(self):
        pass

    #Land       Auto    [Position fix required (e.g. GPS)]      Vehicle initiates the fixed-wing landing sequence.
    def do_land(self,inp):
        pass
    def help_land(self):
        pass

    #Hold       Auto    [Position fix required (e.g. GPS)]      Vehicle circles around the GPS hold position at the current altitude.
    def do_hold(self,inp):
        pass
    def help_hold(self):
        pass

    #Return     Auto    [Position fix required (e.g. GPS)]      Vehicle ascends to a safe height and then returns to its home position and circles.
    def do_return(self, inp):
        pass
    def help_return(self):
        pass

    #Mission    Auto    [Position fix required (e.g. GPS)]      Vehicle executes a predefined mission/flight plan that has been uploaded to the flight controller.  
    def do_mission(self, inp):
        pass
    def help_mission(self):
        pass


    ### Commander Shell functionality ##
    def do_exit(self,inp):
        print()
        if input("Do you want to exit commander? Y/[N] ").lower() == "y":
            log.info("Exiting the commander")
            return True
    def help_exit(self):
        pass

    help_EOF = help_exit
    do_EOF = do_exit

    def emptyline(self):
        pass
