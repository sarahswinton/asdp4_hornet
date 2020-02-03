from cmd import Cmd
import logger

log = logger.get_logger(__name__)

class WaypointsCmd(Cmd):
    info = "HCmd waypoint creator! Type ? to see a list of available commands"
    prompt = "WP> "
    def do_add(self,inp):
        pass
    def help_add(self):
        print("Add a waypoint")

    def do_exit(self,inp):
        print()
        if input("Do you want to exit the waypoint creator? Y/[N] ").lower() == "y":
            log.info("Exiting the WP creator")
            return True

    do_EOF = do_exit
