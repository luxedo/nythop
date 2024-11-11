# SPDX-FileCopyrightText: 2024-present Luiz Eduardo Amaral <luizamaral306@gmail.com>
#
# SPDX-License-Identifier: GPL-3.0-or-later
import code
import subprocess
import sys
import tempfile
from pathlib import Path

from nythop.__about__ import __version__


def nythop_convert(string: str) -> str:
    return "\n".join(line[::-1] for line in string.split("\n"))


def cli():
    """
    Command-line interface for the Nyhtop esolang interpreter.

    Parses command-line arguments to determine the action to take: running a file,
    executing a command, or starting the REPL.

    Args:
        None

    Command-line arguments:
        - file: Path to a Nyhtop script file.
        - -c: Execute a Nyhtop program passed as a string.
        - No arguments: Starts an interactive REPL session.
    """
    import argparse

    parser = argparse.ArgumentParser(
        description=(
            "Nyhtop is an esolang that takes Python and gives it a good shake, "
            "letting you write code in reverse for a coding experience like no other!"
        )
    )
    parser.add_argument("file", nargs="?", help="Nythop script file", type=argparse.FileType("r"))
    parser.add_argument("-c", dest="cmd", metavar="cmd", help="Program passed in as string", type=str)
    args = parser.parse_args()

    match args:
        case argparse.Namespace(file=None, cmd=None):
            run_repl()
        case argparse.Namespace(file=None, cmd=command) if command is not None:
            run_command(command)
        case argparse.Namespace(file=file, cmd=None) if file is not None and file.name == "<stdin>":
            run_command(sys.stdin.read())
        case argparse.Namespace(file=file, cmd=None) if file is not None:
            run_file(Path(file.name))
        case _:
            sys.stderr.write("Something went wrong!\n")
            sys.exit(2)


def run_file(filepath: Path):
    """
    Executes a Nyhtop script from a file.

    Args:
        filepath (Path): Path to the Nyhtop script file.
    """
    code = nythop_convert(filepath.read_text())
    with tempfile.NamedTemporaryFile(mode="w", suffix=".py") as tmpfile:
        tmpfile.write(code)
        tmpfile.flush()
        tmpfile_path = tmpfile.name

        with subprocess.Popen([sys.executable, tmpfile_path], stdout=sys.stdout, stderr=subprocess.PIPE) as proc:
            _, stderr_output_bytes = proc.communicate()
            if proc.returncode != 0:
                stderr_output = stderr_output_bytes.decode()
                stderr_output = stderr_output.replace(tmpfile_path, str(filepath.resolve()))
                sys.stderr.write(stderr_output)
            sys.exit(proc.returncode)


def run_repl():
    """
    Starts an interactive Nyhtop REPL (Read-Eval-Print Loop) session.

    Provides a REPL environment for executing Nyhtop commands interactively.
    """

    class NythopREPL(code.InteractiveConsole):
        cprt = 'Type "pleh", "thgirypoc", "stiderc" or "esnecil" for more information or ")(tixe" to exit.'
        banner = f"Nythop {__version__} on Python {sys.version} on {sys.platform}\n{cprt}"

        def raw_input(self, prompt="Nythop>"):
            command = input(prompt)
            return nythop_convert(command)

    c = NythopREPL()
    c.interact(banner=c.banner, exitmsg="")


def run_command(command: str):
    """
    Executes a Nyhtop command passed as a string.

    Args:
        command (str): The Nyhtop code to execute, passed as a single string.
    """
    code = nythop_convert(command)
    with subprocess.Popen([sys.executable, "-c", code], stdout=sys.stdout, stderr=sys.stderr) as proc:
        proc.communicate()
        sys.exit(proc.returncode)
