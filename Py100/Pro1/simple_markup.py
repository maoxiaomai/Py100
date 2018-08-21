import sys, re

# sys.path.append(r"D:\Documents\py_pro\Py100\Lib")

from util import *

file = open(r"test_input.txt", 'r')

output = sys.stdout
file1 = open(r"test_ouput.html", 'w')
sys.stdout = file1

print('<html><head><title>...</title><body>')

title = True
for block in blocks(file):
    block = re.sub(r'\*(.+?)\*', r'<em>\1</em>', block)
    if title:
        print('<h1>')
        print(block)
        print('</h1>')
        title = False
    else:
        print('<p>')
        print(block)
        print('</p>')

print('</body></html>')



file.close()
file1.close()
sys.stdout = output
