# SPDX-FileCopyrightText: 2024-present Luiz Eduardo Amaral <luizamaral306@gmail.com>
#
# SPDX-License-Identifier: MIT
import code
import subprocess
import sys
import tempfile
import traceback
from pathlib import Path

from nythop.__about__ import __version__


def cli():
    import argparse

    parser = argparse.ArgumentParser(
        description=(
            "Nyhtop is an esolang that takes Python and gives it a good shake, "
            "letting you write code in reverse for a coding experience like no other!"
        )
    )
    parser.add_argument("file", nargs="?", help="Nythop script file", type=argparse.FileType("r"))
    parser.add_argument("-c", help="Program passed in as string", type=str)
    args = parser.parse_args()
    match args:
        case argparse.Namespace(file=None, c=None):
            run_repl()
        case argparse.Namespace(file=None, c=command):
            run_command(command)
        case argparse.Namespace(file=file, c=None) if file.name == "<stdin>":
            run_command(sys.stdin.read())
        case argparse.Namespace(file=file, c=None):
            run_file(Path(file.name))


def run_file(filepath: Path):
    code = "\n".join(line[::-1] for line in filepath.read_text().split("\n"))
    with tempfile.NamedTemporaryFile(delete=False, mode="w", suffix=".py") as tmpfile:
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
    class NythopREPL(code.InteractiveConsole):
        cprt = 'Type "pleh", "thgirypoc", "stiderc" or "esnecil" for more information or ")(tixe" to exit.'
        banner = f"Nythop {__version__} on Python {sys.version} on {sys.platform}\n{cprt}"

        def raw_input(self, prompt="Nythop>"):
            return input(prompt)[::-1]

    c = NythopREPL()
    c.interact(banner=c.banner, exitmsg="")


def run_command(command: str):
    code = "\n".join(line[::-1] for line in command.split("\n"))

    try:
        exec(code)
        sys.exit(0)
    except SystemExit as e:
        sys.exit(e.code)
    except Exception as e:
        tb_lines = traceback.format_exception(type(e), e, e.__traceback__)
        del tb_lines[1]  # This line references nythop library. Don't want to show users
        sys.stdout.write("".join(tb_lines))
        sys.exit(1)
