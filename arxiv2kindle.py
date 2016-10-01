"""
To generate a kindle friendly html file from the current arxiv RSS
usage: arxiv2kindle.py [subject] 
input: 
	[subject] is the subject category you want to browser, e.g., cs, math, astro-ph ...
can also be sub-category like astro-ph.CO, astro-ph.GA...
	defaults to astro-ph

output:
	[subject][date].html

Pre-requisite python packages: feedparser, html

Jiaxin Han, 27/05/2013
Durham
"""

import feedparser as f
from html import HTML
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
out=HTML('html')
h=out.head()
t=h.title(data['feed']['title'])
t.text(data['feed']['updated'][:10])
body=out.body()
body.h1(subject+' '+data['feed']['updated'][:10]+', '+str(len(data['entries']))+' submissions')
l=body.ol
for paper in data['entries']:
	li=l.li
	li.text(format_title(paper),escape=False)
	li.p(paper['author'],escape=False)
	li.p(paper['summary'],escape=False)

outfile=file(subject+data['feed']['updated'][:10]+'.html','w')
outfile.write(str(out))
outfile.close()



