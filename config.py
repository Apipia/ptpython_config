"""
configuration example for ``ptpython``.

Copy this file to ~/.ptpython/config.py
"""
from __future__ import unicode_literals
from prompt_toolkit.filters import ViInsertMode
from prompt_toolkit.key_binding.key_processor import KeyPress
from prompt_toolkit.keys import Keys
from pygments.token import Token

from ptpython.layout import CompletionVisualisation

__all__ = (
    'configure',
)


def configure(repl):
    """
    Configuration method. This is called during the start-up of ptpython.

    :param repl: `PythonRepl` instance.
    """
    # Vi mode.
    repl.vi_mode = True

    # Show function signature (bool).
    repl.show_signature = False

    # Show docstring (bool).
    repl.show_docstring = True

    # Show completions. (NONE, POP_UP, MULTI_COLUMN or TOOLBAR)
    repl.completion_visualisation = CompletionVisualisation.POP_UP

    repl.insert_blank_line_after_output = False
    repl.enable_history_search = True
    repl.use_code_colorscheme('monokai')
    repl.enable_auto_suggest = True



    """
    # Custom key binding for some simple autocorrection while typing.
    corrections = {
        'impotr': 'import',
        'pritn': 'print',
    }

    @repl.add_key_binding(' ')
    def _(event):
        ' When a space is pressed. Check & correct word before cursor. '
        b = event.cli.current_buffer
        w = b.document.get_word_before_cursor()

        if w is not None:
            if w in corrections:
                b.delete_before_cursor(count=len(w))
                b.insert_text(corrections[w])

        b.insert_text(' ')
    """


# Custom colorscheme for the UI. See `ptpython/layout.py` and
# `ptpython/style.py` for all possible tokens.
_custom_ui_colorscheme = {
    # Blue prompt.
    Token.Layout.Prompt:                          'bg:#eeeeff #000000 bold',

    # Make the status toolbar red.
    Token.Toolbar.Status:                         'bg:#ff0000 #000000',
}
