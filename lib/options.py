"""
Parse flag args

Author: Christian M. Fulton
Date: 12.Nov.2021
"""
import configparser
import os


# TODO: Move APP_LOCATION from both app.py and options.py into config.ini
APP_LOCATION = os.path.abspath("logstuff")


def flags(args) -> None:
    """
    When the program is executed, any flags will be pushed into here.

    List all of the options and usage:
        Usage:
            python logstuff <OPTION> [args]
        Options:
            [-c], [--config]    :: Choose directory to write to.
            [-a], [--append]    :: Append an existing file.
    """
    # locate the '--' | '-' -> slice and parse

    if len(args) > 1:
        if "-c" in args[:1] or "--config" in args[:1]:
            config(args[1:2])
    else:
        err = "Usage: python logstuff <OPTION> [arg]"
        print(err)


def config(args):
    """
    This function will create config.ini
    """
    config = configparser.ConfigParser()

    this_arg = args.pop()

    print("Writing to config...")
    config["WORKING_DIR"] = {"Directory": this_arg}
    with open(APP_LOCATION + "/" + "config.ini", "w") as cfile:
        config.write(cfile)
    print(f"Target directory changed to {this_arg}.")


def check_config() -> None:
    """
    Checks directory for config. If config not in dir -> assign default
    Default will be: foobar
    """
    if "config.ini" not in os.listdir(APP_LOCATION):
        default = ["foobar"]
        config(default)
        # default pops before even printed
        # probably should be checking get_dir() for config.ini existence
        print(f"Default directory {default} created... Use --config to change default.")


def set_location() -> None:
    """
    Set the app location in the config
    """
    APP_LOCATION = os.path.abspath("iLog")


def get_location():
    """
    Get the app location from the config
    """
    config = configparser.ConfigParser()
