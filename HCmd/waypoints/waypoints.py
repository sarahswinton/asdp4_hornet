from cmd import Cmd
import logger

log = logger.get_logger(__name__)

banner = """


 __          __ __     _______   ____ _____ _   _ _______ _____ 
 \ \        / /\\ \   / /  __ \ / __ \_   _| \ | |__   __/ ____|
  \ \  /\  / /  \\ \_/ /| |__) | |  | || | |  \| |  | | | (___  
   \ \/  \/ / /\ \\   / |  ___/| |  | || | | . ` |  | |  \___ \ 
    \  /\  / ____ \| |  | |    | |__| || |_| |\  |  | |  ____) |
     \/  \/_/    \_\_|  |_|     \____/_____|_| \_|  |_| |_____/ 
                                                                
                                                                
"""

def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(arg.split())


class WaypointsCmd(Cmd):
    intro = banner +"\nType ? to see a list of available commands"
    prompt = "WP Editor > "

    ### Add waypoint ... ###
    def do_add(self,inp):
        pass
    def help_add(self):
        print("Add a waypoint")

    ### Import waypoints from file ###
    def do_import(self,inp):
        try:
            import_file = parse(inp)
            with open(import_file[0], 'r') as file_:
                pass    
        except IndexError as e:
            log.error("No file path given")
        except FileNotFoundError as e:
            log.error("This file path doesn't exist '{}'".format(import_file[0]))
    def help_import(self):
        print("Import a CSV waypoint file\n\tUsage: import FILEPATH")

    ### Upload to PX4 ###
    def do_upload(self,inp):
        pass
    def help_upload(self):
        pass

    ### WP Shell functionality ##
    def do_exit(self,inp):
        print()
        if input("Do you want to exit the waypoint creator? Y/[N] ").lower() == "y":
            log.info("Exiting the WP creator")
            return True
    do_EOF = do_exit
