export EMAIL=hanjiaxin@gmail.com
export REPLYTO=$EMAIL
rm  -f *.html
python arxiv2kindle_LT.py astroph.CO
echo ' ' | mutt -s "arxiv" hanjiaxin@kindle.com -a *.html

