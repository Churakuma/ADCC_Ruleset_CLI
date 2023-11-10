""" This module provides the ruleset CLI."""

try:
    import argparse
    from . import __version__
    from .ADCC_Ruleset import Ruleset
except (ImportError):
    print("Failed to import necessary packages.")

def main():
    ars = parse_cmd_line_arguments()
    ruleset = Ruleset()
    ruleset.determine_ruleset()

def parse_cmd_line_arguments():
    parser = argparse.ArgumentParser(
        prog = "ruleset",
        description= "ADCC Ruleset, generates appropriate rules that apply to the given competitor based on input.",
        epilog= "Thanks for using the ADCC Ruleset Generator!"
    )
    parser.version = f"ADCC Ruleset Generator v{__version__}"
    parser.add_argument("-v", "--version", action="version")

    return parser.parse_args()