import sublime, sublime_plugin

class CopyAllPathsCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        paths = []
        settings = sublime.load_settings("CopyAllPaths.sublime-settings")
        prefix_str = settings.get('prefix_str') or ''
        postfix_str = settings.get('postfix_str') or ''

        for v in self.view.window().views():
            if v.file_name() and len(v.file_name()) > 0:
                paths.append( prefix_str + v.file_name() + postfix_str + '\n')

        sublime.set_clipboard( ''.join([str(p) for p in paths]) )

        mssg = ''
        if len(paths) == 1:
            mssg = "Copied 1 file path"
        else:
            mssg = "Copied %d files paths" % len(paths)

        sublime.status_message(mssg)
