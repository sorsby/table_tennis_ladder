from quik import FileLoader, Template


class Htmlify:

    def __init__(self, group, ladder):
        self.group = group
        self.loader = FileLoader('html')
        self.template = self.loader.load_template('ladder_template.html')

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
        filepath = 'html/out/'
        with open(filepath + self.group + '.html', 'w') as f:
            f.writelines(html)


# players = [{'name': 'Matt', 'rank': 1},
#            {'name': 'Rob', 'rank': 2},
#            {'name': 'Mike', 'rank': 3},
#            {'name': 'James', 'rank': 4}]

# group = "Hermes"
