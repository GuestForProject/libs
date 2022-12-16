from html import HTML
h = HTML()
h.p('Hello, world!')
h.br
print(h)

t = h.table(border='1')
for i in range(2):
    r = t.tr
    r.td('column 1')
    r.td('column 2')
print(t)



