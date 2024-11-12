import sys
import traceback
from io import StringIO

from pyscript import document, window


def nythop_convert(string: str) -> str:
    return "\n".join(line[::-1] for line in string.split("\n"))


def run_nythop(_):
    input_text = window.cmEditor.getValue()
    output_div = document.querySelector("#output")

    error_highlight = ["border-red-500", "bg-red-200"]
    for c in error_highlight:
        output_div.classList.remove(c)

    capture = StringIO()
    stdout_bak = sys.stdout
    sys.stdout = capture

    try:
        exec(nythop_convert(input_text), {})
        text = capture.getvalue()
        capture.close()
        sys.stdout = stdout_bak
    except Exception as e:
        for c in error_highlight:
            output_div.classList.add(c)
        tb_lines = traceback.format_exception(type(e), e, e.__traceback__)
        tb_lines.pop(1)  # This line references nythop library. Don't want to show users
        text = "".join(tb_lines)

    output_div.innerText = text
