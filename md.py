from python_md import Markdown


md = Markdown('assets/examples.md')
content = md.h1('simple python-md example')
header = ['this', 'is', 'a', 'table', 'header']
body = [
    ['this', 'is', 'the', 'first', 'row'],
    ['this', 'is', 'the', 'second', 'row'],
    ['this', 'is', 'the', 'third', 'row'],
]
content += md.table(header, body)
md.write_to_file(content, 'w+')