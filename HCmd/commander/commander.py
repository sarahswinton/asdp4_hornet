from cmd import Cmd
import logger

import rospy
from mavros_msgs.srv import CommandBool

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

    def do_arm(self,inp):
        rospy.wait_for_service("/mavros/cmd/arming")
        try:
            arming = rospy.ServiceProxy("mavros/cmd/arming", CommandBool)
            if inp.lower() == "true": 
                resp = arming(True)
                resp = "Success: " + str(resp.success)
            elif inp.lower() == "false":
                resp = arming(False)
                resp = "Success: " + str(resp.success)
            else:
                resp = "No value argument (true/false) given"
            print(resp)
        except rospt.ServiceException, e:
            print("Service arm call failed: %s"%e)

    ### WP Shell functionality ##
    def do_exit(self,inp):
        print()
        if input("Do you want to exit the waypoint creator? Y/[N] ").lower() == "y":
            log.info("Exiting the WP creator")
            return True
    do_EOF = do_exit
