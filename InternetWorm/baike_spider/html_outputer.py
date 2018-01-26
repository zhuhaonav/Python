class HtmlOutputer(object):
    def __init__(self, *args, **kwargs):
        self.datas = []
    def collect_data(self):
        if data is None:
            return
        self.datas.append(data)
    def output_html(self):
        fout = open('output.html','w')
        fout.write('<html>')
        fout.write('<body>')
        fout.write('<table>')

        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>' % data['url'].encode('utf-8'))
            fout.write('<td>%s</td>' % data['summary'].encode('utf-8'))

        fout.write('</body>')
        fout.write('</html>')

        fout.close()