from urllib.request import urlopen
from html.parser import HTMLParser

def getSource(url):
    response = urlopen(url)
    html = response.read()
    return html.decode()

html = getSource('http://www.uol.com.br')


class Myparser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for atrr in attrs:
                if atrr [0] == 'href':
                    print(atrr[1])


def news(url, topics):
    '''conta no recurso com URL url a frequência
       de cada tópico na lista topics '''
    response = urlopen(url)
    html = response.read()
    content = html.decode().lower()
    for topic in topics:
        n = content.count(topic)
        print('{} appears {} times.'.format(topic, n))


class myHTMLPARSER(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.indent = 0

    def handle_starttag(self, tag, attrs):
        print('{}{} start'.format(self.indent * ' ', tag))
        self.indent += 4
    def handle_endtag(self, tag):
        print('{}{} end'.format(self.indent * ' ', tag))
        self.indent -= 4

'''arquivo = open('index.html')
content = arquivo.read()
arquivo.close()
myParse = myHTMLPARSER()
myParse.feed(content)'''