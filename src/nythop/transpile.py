# SPDX-FileCopyrightText: 2024-present Luiz Eduardo Amaral <luizamaral306@gmail.com>
#
# SPDX-License-Identifier: GPL-3.0-or-later

import argparse
import sys
import traceback
from pathlib import Path

from nythop.nythop import nythop_convert


def transpile():
    """
    Transpiles Python code into Nythop syntax.

    This function parses command-line arguments, which can either be a Python script file,
    a command passed as a string, or input from stdin. It converts the input code into Nythop
    syntax using the `nythop_convert` function and writes the result to a specified output file
    or prints it to stdout. If no valid input is provided, it displays an error message and exits.

    Command-line arguments:
        - `file`: The Python script file to transpile.
        - `-c`: A Python program passed as a string to be transpiled.
        - `-o`: The file to write the transpiled Nythop code to. If not provided, output is printed to stdout.
    """
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
    """
    Validates the Python code to ensure it can be compiled.

    This function attempts to compile the provided code string to ensure it is valid Python code.
    If the code is invalid, it catches the exception, formats the traceback, and prints an error
    message to stderr before exiting.

    Args:
        code (str): The Python code to be validated.

    Raises:
        SystemExit: If the code cannot be compiled, the function exits with an error message.
    """
    try:
        compile(f"{code}\n", "<string>", "exec")
    except Exception as e:
        tb_lines = traceback.format_exception(type(e), e, e.__traceback__)
        tb_lines.pop(1)  # This line references nythop library. Don't want to show users
        sys.stdout.write("Nythop Transpiler Error. Could not transpile because of the following:\n\n")
        sys.stdout.write("".join(tb_lines))
        sys.exit(1)
