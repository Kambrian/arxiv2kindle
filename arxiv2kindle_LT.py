"""
To generate a kindle friendly html file from the current arxiv RSS
usage: arxiv2kindle.py [subject] 
input: 
	[subject] is the subject category you want to browser, e.g., cs, math, astro-ph ...
can also be sub-category like astro-ph.CO, astro-ph.GA...
	defaults to astro-ph

output:
	[subject][date].html

Pre-requisite python packages: feedparser (no html requirement)

Jiaxin Han, 27/05/2013
Durham
"""

import feedparser as f
import sys

subject='astro-ph'
if len(sys.argv)>1:
	subject=sys.argv[1]

def format_title(paper):
	s='<b>'+paper['title'][:paper['title'].index('(arXiv:')]+'</b>'
	id=paper['title'][paper['title'].index('(arXiv:')+7:-1]
	s+='<a href='+paper['link']+'>'+id+'</a>'
	return s


data=f.parse('http://export.arxiv.org/rss/'+subject)
date=data['feed']['updated'][:10]
o=file(subject+date+'.html','w')
o.write('<html>\n')
o.write('<head>\n')
o.write('<title>')
o.write(data['feed']['title'])
o.write(' '+date)
o.write('</title>\n')
o.write('</head>\n')
o.write('<body>\n')
o.write('<h1>'+subject+' '+date+', '+str(len(data['entries']))+' submissions </h1>')
o.write('<ol>\n')
for paper in data['entries']:
	o.write('<li>\n')
	o.write(format_title(paper))
	o.write('<p>'+paper['author']+'</p>')
	o.write(paper['summary'])
	o.write('</li>\n')

o.write('</body>\n')
o.write('</html>')
o.close()



