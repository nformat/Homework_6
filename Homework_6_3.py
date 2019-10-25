text = """
        Записывает в новый файл все слова в алфавитном порядке из другого файла с текстом. Каждое слово на новой строке.
        Рядом со словом укажите сколько раз оно встречалось в тексте
        """
file1 = "c:\\temp\\file4.txt"
file2 = "c:\\temp\\file5.txt"

with open(file1, "w") as f:
    f.write(text)

#Создаем список слов из файла
with open(file1, "r") as f:
    t = []
    for lines in f:
        t2 = lines.strip().split()
        t += t2
    t = sorted(t, key=str.lower)

with open(file2, "w") as f2:
    for i in t:
        w = str(t.count(i))+" : "+i+"\n"
        f2.write(w)

#Проверяем
with open(file2, "r") as f3:
    print(f3.read())
