# SPDX-FileCopyrightText: 2024-present Luiz Eduardo Amaral <luizamaral306@gmail.com>
#
# SPDX-License-Identifier: GPL-3.0-or-later

import tempfile
from pathlib import Path
from unittest.mock import patch

import pytest

from nythop.nythop import cli
from nythop.transpile import transpile
from tests.test_nythop import TEST_FAIL_SCRIPTS_DIR, TEST_SUCCESS_SCRIPTS_DIR

TEST_SUCCESS_SCRIPTS = [f for f in TEST_SUCCESS_SCRIPTS_DIR.iterdir() if f.suffix == ".py"]
TEST_FAIL_SCRIPTS = [f for f in TEST_FAIL_SCRIPTS_DIR.iterdir() if f.suffix == ".py"]


@pytest.mark.parametrize("file", TEST_SUCCESS_SCRIPTS)
def test_transpile_success_file(file):
    with patch("sys.argv", new=["nythop-transpile", str(file)]):
        with pytest.raises(SystemExit) as exc_info:
            transpile()
        assert exc_info.value.code == 0


@pytest.mark.parametrize("file", TEST_FAIL_SCRIPTS)
def test_transpile_fail_file(file):
    with patch("sys.argv", new=["nythop-transpile", str(file)]):
        with pytest.raises(SystemExit) as exc_info:
            transpile()
        assert exc_info.value.code == 1


@pytest.mark.parametrize("file", TEST_SUCCESS_SCRIPTS)
def test_transpile_success_command(file):
    with patch("sys.argv", new=["nythop-transpile", "-c", file.read_text()]):
        with pytest.raises(SystemExit) as exc_info:
            transpile()
        assert exc_info.value.code == 0


@pytest.mark.parametrize("file", TEST_FAIL_SCRIPTS)
def test_transpile_fail_command(file):
    with patch("sys.argv", new=["nythop-transpile", "-c", file.read_text()]):
        with pytest.raises(SystemExit) as exc_info:
            transpile()
        assert exc_info.value.code == 1


@pytest.mark.parametrize("file", TEST_SUCCESS_SCRIPTS)
def test_transpile_success_output(file):
    with tempfile.NamedTemporaryFile(suffix=".yp") as tmp_file:
        output_path = Path(tmp_file.name)

        with patch("sys.argv", new=["nythop-transpile", str(file), "-o", str(output_path)]):
            with pytest.raises(SystemExit) as exc_info:
                transpile()

            assert exc_info.value.code == 0
            assert output_path.exists()
            with patch("sys.argv", new=["nythop", str(output_path)]):
                with pytest.raises(SystemExit) as run_exc_info:
                    cli()
                assert run_exc_info.value.code == 0
