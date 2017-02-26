# sublime-c0-repl
Allows coin to be run directly in Sublime, and to be opened and run with the current project

## Installation Instructions
The SublimeREPL package must already be installed for the files included in sublime-c0-repl to work.
To install these files, first move the `C0` folder into Sublime's `packages/SublimeREPL/config` folder. This will make the C0 REPL available in Sublime, and availbel to other files.

Next, move `c0-with-ui-options.py` to Sublime's `packages/user directory`. This script automatically splits the Sublime window into code and a REPL window, and either compiles and executes the code or runs coin with the code based on a keypress.

Lastly, you can copy the key bindings from `c0.sublime-keymap` and add them to your own key bindings. These bindings are scoped specifically to c0, and allow you to access the functionality of `c0-with-ui-options.py`.
