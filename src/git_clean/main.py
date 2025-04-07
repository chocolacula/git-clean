from verbm.version_control.call import call
from git_clean.clap import parser

VERSION = "0.0.0"


def run():
    # parse command line arguments
    args = parser().parse_args()

    # only one command is supported
    # if args.component == "local":
    #     pass

    if args.version:
        print(VERSION)
        exit(0)

    call("git", "fetch", "--prune")

    current = call("git", "branch", "--show-current").rstrip()

    origin = (
        call(
            "git",
            "--no-pager",
            "branch",
            "--list",
            "--format=%(refname:short)",
            "--remote",
        )
        .rstrip()
        .split("\n")
    )

    locals = (
        call(
            "git",
            "--no-pager",
            "branch",
            "--list",
            "--format=%(refname:short)",
        )
        .rstrip()
        .split("\n")
    )

    for local in locals:
        if local == current:
            print("Skip current branch")
            continue
        if "origin/" + local not in origin:
            print(f"Remove branch {local}")
            call("git", "branch", "-D", local)
