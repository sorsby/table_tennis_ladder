from quik import FileLoader, Template


class Htmlify:

    template_filepath = 'html'
    out_filepath = 'html/out/'
    ladder_template = 'ladder_template.html'

    def __init__(self, group, ladder):
        self.group = group
        self.loader = FileLoader(self.template_filepath)
        self.template = self.loader.load_template(self.ladder_template)

        # put data in format ready for html templating
        html_players = []
        i = 0
        for player in ladder:
            i += 1
            html_players.append({'name': player.name, 'rank': i})

    def gen_html(self):
        html = self.template.render(
            locals(), loader=self.loader).encode('utf-8')
        self.write_html(html)

    def write_html(self, html):
        with open(self.out_filepath + self.group + '.html', 'w') as f:
            f.writelines(html)
