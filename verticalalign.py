import sublime, sublime_plugin

class VerticalAlignCommand(sublime_plugin.TextCommand):

    def get_col(self, r):
        row, col = self.view.rowcol(r.begin())
        return col

    def run(self, edit):
        n = max((self.get_col(r) for r in self.view.sel()))  
        for r in self.view.sel():
            col = self.get_col(r)
            for i in range(n-col):
                self.view.insert(edit, r.begin(), " ")
                

