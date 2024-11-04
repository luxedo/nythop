# SPDX-FileCopyrightText: 2024-present Luiz Eduardo Amaral <luizamaral306@gmail.com>
#
# SPDX-License-Identifier: MIT
from pathlib import Path

import pytest

from nythop.nythop import run

ROOT_DIR = Path(__file__).parent.resolve()
TEST_SUCCESS_SCRITPS_DIR = ROOT_DIR / "examples" / "success"
TEST_SUCCESS_SCRITPS = [f for f in TEST_SUCCESS_SCRITPS_DIR.iterdir() if f.suffix == ".yp"]
TEST_FAIL_SCRITPS_DIR = ROOT_DIR / "examples" / "fail"
TEST_FAIL_SCRITPS = [f for f in TEST_FAIL_SCRITPS_DIR.iterdir() if f.suffix == ".yp"]


@pytest.mark.parametrize("script_name", TEST_SUCCESS_SCRITPS)
def test_success_cripts(script_name):
    run(script_name.read_text())


@pytest.mark.parametrize("script_name", TEST_FAIL_SCRITPS)
def test_fail_cripts(script_name):
    with pytest.raises(Exception):  # noqa: B017 PT011
        run(script_name.read_text())
