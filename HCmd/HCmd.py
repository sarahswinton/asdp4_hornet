from cmd import Cmd
import logger

import Waypoints

log = logger.get_logger(__name__)

class GCmd(Cmd):
    intro = "Welcome to the Hornet Shell!\nUse ? or 'help' to see a list of available commands"
    
    def __init__(self):
        self.root = False
        self.prompt = "$ "
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

    ### Waypoints ###
    def do_waypoints(self, inp):
        shell = Waypoints.WaypointsCmd()
        shell.cmdloop()
    def help_waypoints(self):
        print("A manual waypoint creator WIP")

    ### Info ###
    def do_info(self, inp):
        print("TODO: Print current drone info")
    def help_info(self):
        print("Prints current drones information")

    ### Setup ###
    def do_setup(self, inp):
        print("TODO: Nested shell for setup? Might be superflous")
    
    ### Exit ###
    def do_exit(self, inp):
        if self.root:
            self.exit_root()
        else:
            print("Exiting GCmd...")
            return True
    def help_exit(self):
        print("Exit GCmd or root")

    ### Other Cmd setup to control shell behaviour ###
    def emptyline(self):
        pass
    do_EOF = do_exit
    help_EOF = help_exit

def run():
    GCmd().cmdloop()

if __name__ == "__main__":
    run()
