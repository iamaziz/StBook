
from io import StringIO
import sys

from code_editor import code_editor
from .optional_imports import *


def run_code(code):
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    exec(code, globals())
    sys.stdout = old_stdout
    return redirected_output.getvalue()


def code_runner(code, theme="light", key="cell"):

    res = code_editor(code, theme=theme, key=key)

    if len(res['id']) != 0 and (res['type'] == 'submit' or res['type'] == 'selection'):
        code = res['text']
        return run_code(code)