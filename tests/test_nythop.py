# SPDX-FileCopyrightText: 2024-present Luiz Eduardo Amaral <luizamaral306@gmail.com>
#
# SPDX-License-Identifier: GPL-3.0-or-later
from pathlib import Path
from unittest.mock import patch

import pytest

from nythop.nythop import cli, run_command, run_file

ROOT_DIR = Path(__file__).parent.resolve()
TEST_SUCCESS_SCRITPS_DIR = ROOT_DIR / "examples" / "success"
TEST_SUCCESS_SCRITPS = [f for f in TEST_SUCCESS_SCRITPS_DIR.iterdir() if f.suffix == ".yp"]
TEST_FAIL_SCRITPS_DIR = ROOT_DIR / "examples" / "fail"
TEST_FAIL_SCRITPS = [f for f in TEST_FAIL_SCRITPS_DIR.iterdir() if f.suffix == ".yp"]


@pytest.mark.parametrize("file", TEST_SUCCESS_SCRITPS)
def test_success_scripts(file):
    with pytest.raises(SystemExit) as exc_info:
        run_command(file.read_text())
    assert exc_info.value.code == 0


@pytest.mark.parametrize("file", TEST_FAIL_SCRITPS)
def test_fail_scripts(file):
    with pytest.raises(SystemExit) as exc_info:
        run_command(file.read_text())
    assert exc_info.value.code == 1


@pytest.mark.parametrize("file", TEST_SUCCESS_SCRITPS)
def test_success_files(file):
    with pytest.raises(SystemExit) as exc_info:
        run_file(file)
    assert exc_info.value.code == 0


@pytest.mark.parametrize("file", TEST_FAIL_SCRITPS)
def test_fail_files(file):
    with pytest.raises(SystemExit) as exc_info:
        run_file(file)
    assert exc_info.value.code == 1


@pytest.mark.parametrize("file", TEST_SUCCESS_SCRITPS)
def test_success_cli_file(file):
    with patch("sys.argv", new=["nythop", str(file)]):
        with pytest.raises(SystemExit) as exc_info:
            cli()
        assert exc_info.value.code == 0


@pytest.mark.parametrize("file", TEST_FAIL_SCRITPS)
def test_fail_cli_file(file):
    with patch("sys.argv", new=["nythop", str(file)]):
        with pytest.raises(SystemExit) as exc_info:
            cli()
        assert exc_info.value.code == 1


@pytest.mark.parametrize("file", TEST_SUCCESS_SCRITPS)
def test_success_cli_command(file):
    with patch("sys.argv", new=["nythop", "-c", file.read_text()]):
        with pytest.raises(SystemExit) as exc_info:
            cli()
        assert exc_info.value.code == 0


@pytest.mark.parametrize("file", TEST_FAIL_SCRITPS)
def test_fail_cli_command(file):
    with patch("sys.argv", new=["nythop", "-c", file.read_text()]):
        with pytest.raises(SystemExit) as exc_info:
            cli()
        assert exc_info.value.code == 1
