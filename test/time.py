import time

print(time.time())
print(time.localtime())
print(time.asctime())
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())) 

import datetime

print(datetime.date.today()) 
print(datetime.date.today().strftime('%d/%m/%Y'))
print(datetime.date(1941, 1, 5))

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
def generate_tr(name, score):
    if score < 60:
        return '<tr><td>%s</td><td style="color:red">%s</td></tr>' % (name, score)
    return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)

tds = [generate_tr(name, score) for name, score in d.items()]
print ('<table border="1">')
print ('<tr><th>Name</th><th>Score</th><tr>')
print ('\n'.join(tds))
print ('</table>')