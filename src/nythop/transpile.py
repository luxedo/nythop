# SPDX-FileCopyrightText: 2024-present Luiz Eduardo Amaral <luizamaral306@gmail.com>
#
# SPDX-License-Identifier: GPL-3.0-or-later

import argparse
import sys
import traceback
from pathlib import Path

from nythop.nythop import nythop_convert


def transpile():
    parser = argparse.ArgumentParser(description="Transpiles python code into nythop")

    parser.add_argument("file", nargs="?", help="Python script file", type=argparse.FileType("r"))
    parser.add_argument("-c", dest="cmd", metavar="cmd", help="program passed in as string", type=str)
    parser.add_argument(
        "-o", dest="output", metavar="output", nargs="?", help="output file", type=argparse.FileType("w")
    )
    args = parser.parse_args()

    code: str
    match args:
        case argparse.Namespace(file=None, cmd=command) if command is not None:
            code = command
        case argparse.Namespace(file=file, cmd=None) if file is not None and file.name == "<stdin>":
            code = sys.stdin.read()
        case argparse.Namespace(file=file, cmd=None) if file is not None:
            code = Path(file.name).read_text()
        case _:
            sys.stdout.write("Please provide an input as a file, via stdin or as a command with -c\n")
            sys.exit(1)
    validate_source(code)

    if args.output is not None:
        args.output.write(nythop_convert(code))
    else:
        sys.stdout.write(nythop_convert(code))
    sys.exit(0)


def validate_source(code: str):
    try:
        compile(f"{code}\n", "<string>", "exec")
    except Exception as e:
        tb_lines = traceback.format_exception(type(e), e, e.__traceback__)
        tb_lines.pop(1)  # This line references nythop library. Don't want to show users
        sys.stdout.write("Nythop Transpiler Error. Could not transpile because of the following:\n\n")
        sys.stdout.write("".join(tb_lines))
        sys.exit(1)
