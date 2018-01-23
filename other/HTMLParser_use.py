from html.parser import HTMLParser
from html.entities import name2codepoint
class myhtmlparser(HTMLParser):
	def handle_starttag(self,tag,attrs):
		print('<%s>'%tag)
	def handle_endtag(self, tag):
		print('</%s>' % tag)

	def handle_startendtag(self, tag, attrs):
		print('<%s/>' % tag)

	def handle_data(self, data):
		print(data)

	def handle_comment(self, data):
		print('<!--', data, '-->')

	def handle_entityref(self, name):
		print('&%s;' % name)

	def handle_charref(self, name):
		print('&#%s;' % name)
parser=myhtmlparser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;&nbsp;&#1231;&#12&#123131;tutorial...<br>END</p>
</body></html>''')
#htmlparser解析