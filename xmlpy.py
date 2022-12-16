from html import XML
h = XML('xml')
h.p
h += XML('some-tag', 'some text')
print(h)