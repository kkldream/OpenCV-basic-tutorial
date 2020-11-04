a = 10
b = 'Hello' #這是註解
c = [1, 2, 'AAA', 4]
'''
這是多行註解
'''
def add(var):
    return var + 1

if a > 20 and a < 30:
    print('>')
else:
    print('<')
print('-----')
for i in c:
    print(i)
print('-----')
for j in range(3):
    print(j)
print('-----')
while a < 15:
    a = add(a)
    print(a, end = '@')
'''
if True:
    if True:
        print('AAA')
print('BBB')
  print('CCC')
'''
