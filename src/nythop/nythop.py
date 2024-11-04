# SPDX-FileCopyrightText: 2024-present Luiz Eduardo Amaral <luizamaral306@gmail.com>
#
# SPDX-License-Identifier: MIT


def cli():
    import argparse

    parser = argparse.ArgumentParser(
        description="Nyhtop is an esolang that takes Python and gives it a good shake, letting you write code in reverse for a coding experience like no other!"
    )
    parser.add_argument("script", help="Nothyp script file", type=argparse.FileType("r"))
    args = parser.parse_args()
    script = args.script.read()
    run(script)


def run(script: str):
    rev_script = "\n".join(line[::-1] for line in script.split("\n"))
    exec(rev_script)  # noqa: S102
