from argparse import ArgumentParser


def parser() -> ArgumentParser:
    p = ArgumentParser(description="git repo cleaning tool")

    # fmt: off
    p.add_argument(
        "-v", "--version",
        help="print git-clean version",
        action="store_true",
        default=False
    )

    commands = ["local"]

    p.add_argument(
        "command",
        help="command to run",
        type=str,
        choices=commands,
    )
    # fmt: on

    return p
