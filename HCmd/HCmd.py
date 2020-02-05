from cmd import Cmd
import logger

import waypoints
import commander
from info import controller_info, drone_info


log = logger.get_logger(__name__)

banner = """


  _    _  ____  _____  _   _ ______ _______ 
 | |  | |/ __ \|  __ \| \ | |  ____|__   __|
 | |__| | |  | | |__) |  \| | |__     | |   
 |  __  | |  | |  _  /| . ` |  __|    | |   
 | |  | | |__| | | \ \| |\  | |____   | |   
 |_|  |_|\____/|_|  \_\_| \_|______|  |_|   
                                            
                                            

"""


class HCmd(Cmd):
  
#    intro = "Welcome to the Hornet Shell!\nUse ? or 'help' to see a list of available commands"
    
    def __init__(self):
        self.root = False
        self.prompt = "$ "

        self.intro = banner
        self.intro += "\nUse ? or 'help' to see a list of available commands"

        Cmd.__init__(self)
    
    ## Root ###
    def do_root(self, inp):
        log.info("Giving root access to user... TODO: Implement password?")
        self.root = True
        self.prompt = "# "
    def exit_root(self):
        self.root = False
        print("\r")
        log.info("Exiting root. Resuming normal user permissions")
        self.prompt = "$ "
    def help_root(self):
        print("Gives escelated priviliges to the user")
   
    
    ### Commander ###
    def do_commander(self, inp):
        # Do translate
        shell = commander.CommanderCmd()
        shell.cmdloop()

    ### Waypoints ###
    def do_waypoints(self, inp):
        shell = waypoints.WaypointsCmd()
        shell.cmdloop()
    def help_waypoints(self):
        print("A manual waypoint creator WIP")

    ### Info ###
    def do_info(self, inp):
        # Could have htop like terminal GUI
        if inp == "controller":
            controller_info()
        elif inp == "drone":
            drone_info()
        else:
            print("No correct argument given")
            self.help_info()
    def help_info(self):
        print("Prints either the controller or drones current inforation")
        print("\tARGUMENTS:\tcontroller\tdrone")

    ### Setup ###
    def do_setup(self, inp):
        print("TODO: Nested shell for setup? Might be superflous")
    
    ### Exit ###
    def do_exit(self, inp):
        if self.root:
            self.exit_root()
        else:
            print("Exiting HCmd...")
            return True
    def help_exit(self):
        print("Exit HCmd or root")

    ### Other Cmd setup to control shell behaviour ###
    def emptyline(self):
        pass
    do_EOF = do_exit
    help_EOF = help_exit

def run():
    HCmd().cmdloop()

if __name__ == "__main__":
    run()
