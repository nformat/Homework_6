import codecs

#4
f = open('c:\\temp\\file.txt', 'w')

def la(a=3, b=3, c=0):
    """
    Генерирует и возвращает песню la-la-la. Функция принимает 3 аргумента:
    a - сколько строк будет в песне
    b - сколько «la» будет в строке («la» в строке объединяются дефисом
    c - если 0, то в конце песни (в конце последней строчки) стоит точка, если 1, то в конце стоит «!».
    """
    e = ("la-"*(b-1)+"la\n")*a
    r = e.strip()+("." if c == 0 else "!")
    return r

print(la(4, 4, 1), file=f)
f.close()

with open('c:\\temp\\file.txt', 'r') as f:
    print(f.read())



f2 = codecs.open( "C:\\py_projects\\Homewrok_5\Homework_5_1.py", "r", encoding="utf-8")
print(f2.read())
f2.close()

#8
with open('c:\\temp\\file.txt', 'r') as f:
    for line in f:
        print(line.strip() + "!")

#9
with open('c:\\temp\\file1.txt', 'w') as f1:
    f1.writelines(["list", "\nof", '\nstring'])
    f1.close()

f1 = open('c:\\temp\\file1.txt', 'r')
f2 = open('c:\\temp\\file2.txt', 'w')
c = 0
for i in f1:
    c += 1
    print(c, i.strip(), file=f2)
f1.close()
f2.close()


#10

f3 = open('c:\\temp\\file3.txt', 'r')
n = []
try:
    for line in f3:
        n.append(int(line))
except ValueError:
    print('Это не числа')
else:
   print('В файле следующие числа:\n', n)
finally:
   f3.close()
   print('Файл закрыт:', f3.closed)


#(with … as).
n2 = []
with open('c:\\temp\\file4.txt', 'r') as f4:
    try:
        for line in f4:
            n2.append(int(line))
    except ValueError:
        print('Это не числа')
    else:
        print('В файле следующие числа:\n', n)
print('Файл закрыт:', f3.closed)
