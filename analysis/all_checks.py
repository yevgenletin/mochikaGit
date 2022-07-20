import os


def check_reboot():
    """ Return True if the computer has pending reboot."""
    return os.path.exist("/run/reboot-required")

def main():
    pass;

main();