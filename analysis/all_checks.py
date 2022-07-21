import os
import sys


def check_reboot():
    """ Return True if the computer has pending reboot."""
    return os.path.exist("/run/reboot-required")

def main():

    if check_reboot():
        print('Pending Reboot')
        sys.exit(1)
    print('Everything ok.')
    sys.exit(0)
main();

