import os
import sys


print("git commit -a -m")
print("git log -p")

def check_reboot():
    """Return True if the computer has a pending reboot"""
    return os.path.exist("/run/reboot-required")

def main():
    if check_reboot():
        print("Pending Reboot.")
        sys.exit(1)
    print("Everything ok")
    sys.exit(0)
main()