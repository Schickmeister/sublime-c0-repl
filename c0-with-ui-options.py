#Sublime C0 IDE Plugin for Sublime 3
#By Austin Schick
#Adapted from sublime-python-ide-plugin.py by David Kosbie, 
#Josh Korn, Rohan Varma, and Kevin Zheng

#############################################################################

import sublime, sublime_plugin

class c0coinCommand(sublime_plugin.WindowCommand):
    def run(self):
        if (self.window.num_groups() != 2):
            self.window.run_command(
                'set_layout',
                {"cols":[0.0, 1.0],
                 "rows":[0.0, 0.5, 1.0],
                 "cells":[[0, 0, 1, 1], [0, 1, 1, 2]]
                }
            )

        # save file (if necessary) in current view
        C0EditorsGroup = 0
        self.window.focus_group(C0EditorsGroup)
        view = self.window.active_view()
        if (view.is_dirty()):
            view.run_command('save')

        # close old C0 interpreters, if any
        C0InterpretersGroup = 1
        for view in self.window.views_in_group(C0InterpretersGroup):
            view.close()

        # run the C0 interpreter
        self.window.run_command(
            'repl_open',
            {"type": "subprocess",
             "encoding": "utf8",
             "cmd": ["coin", "-d", "$file"],
             "cwd": "$file_path",
             "syntax": "Packages/Text/Plain text.tmLanguage",
             "external_id": "C0"
            }
        )

        # And move the interpreter into group 1, with focus
        self.window.run_command(
            'move_to_group',
            { "group": C0InterpretersGroup }
        )

        view = self.window.active_view()
        layout_width, layout_height = view.layout_extent()
        window_width, window_height = view.viewport_extent()
        new_top = layout_height - window_height
        view.set_viewport_position((0, max(new_top, 0)))

class c0compileCommand(sublime_plugin.WindowCommand):
    def run(self):
        if (self.window.num_groups() != 2):
            self.window.run_command(
                'set_layout',
                {"cols":[0.0, 1.0],
                 "rows":[0.0, 0.5, 1.0],
                 "cells":[[0, 0, 1, 1], [0, 1, 1, 2]]
                }
            )

        # save file (if necessary) in current view
        C0EditorsGroup = 0
        self.window.focus_group(C0EditorsGroup)
        view = self.window.active_view()
        if (view.is_dirty()):
            view.run_command('save')

        # close old C0 interpreters, if any
        C0InterpretersGroup = 1
        for view in self.window.views_in_group(C0InterpretersGroup):
            view.close()

        # run the C0 interpreter
        self.window.run_command(
            'repl_open',
            {"type": "subprocess",
             "encoding": "utf8",
             "cmd": ["cc0", "-d", "-x", "$file"],
             "cwd": "$file_path",
             "syntax": "Packages/Text/Plain text.tmLanguage",
             "external_id": "C0"
            }
        )

        # And move the interpreter into group 1, with focus
        self.window.run_command(
            'move_to_group',
            { "group": C0InterpretersGroup }
        )

        view = self.window.active_view()
        layout_width, layout_height = view.layout_extent()
        window_width, window_height = view.viewport_extent()
        new_top = layout_height - window_height
        view.set_viewport_position((0, max(new_top, 0)))