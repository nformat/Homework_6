import requests

def book(url,book1, change):
    #Создаем книгу
    r = requests.post(url+"books", data=book1)
    book_url = url + "books/" + str(r.json()["id"])

    #Проверяем
    r1 = requests.get(book_url)
    for i in book1:
         if book1[i] != r1.json()[i]:
           raise Exception("Ошибка создания книги")
    print(f"Книга создалась:  {r1.status_code} , {r1.text}")

    #Изменяем и проверяем
    r2 = requests.put(book_url, data={"title": change})
    if requests.get(book_url).json()["title"] == change:
        print(f"Книга изменилась: {r2.status_code} , {r2.text}")
    else:
        raise Exception("Ошибка изменения книги")

    #Удаляем и проверяем
    requests.delete(book_url)
    r1 = requests.get(book_url)
    if r1.status_code != 404:
        raise Exception("Ошибка удаления книги")
    print(f"Проверяем что удалилась: {r1.status_code} , {r1.text}")


def book_with_hero(url, book1, hero, n_hname):
    r = requests.post(url+"books", data=book1)
    book = r.json()
    book_url = url + "books/" + str(book["id"])

    # Связывем героя с книгой и сздаем его
    hero["book"] = book_url
    r2 = requests.post(url+"roles", data=hero)
    hero = r2.json()
    hero_url = url + "roles/" + str(hero["id"])

    #Проверяем
    r2 = requests.get(hero_url)
    for i in hero:
         if hero[i] != r2.json()[i]:
           raise Exception("Ошибка создания героя")
    print(f"\nПроверяем что создалась роль:\n{r2.status_code} , {r2.text}")

    #Изменяем и проверяем
    r3 = requests.put(hero_url, data={"type": n_hname})
    if requests.get(hero_url).json()["type"] != n_hname:
        raise Exception("Ошибка изменения роли")
    print(f"\nРоль изменилась: \n{r3.status_code} , {r3.text}")

    #Удаляем роль и проверяем
    requests.delete(hero_url)
    r4 = requests.get(hero_url)
    if r4.status_code != 404:
        raise Exception("Ошибка удаления роли")
    print(f"\nПроверяем что удалилась роль: \n{r4.status_code} , {r4.text}")

    #Удаляем книгу и проверяем
    requests.delete(book_url)
    r5 = requests.get(book_url)
    if r5.status_code != 404:
        raise Exception("Ошибка удаления книги")
    print(f"\nПроверяем что удалилась книга: \n{r5.status_code} , {r5.text}")


url = "http://pulse-rest-testing.herokuapp.com/"
d = {"title": "PY for Dummies", "author": "JK"}
n_title = "PY for Dummies and others"
h = {"name": "Udav ", "type": "snake", "level": 10}
n_heroname = "evil snake"

book(url, d, n_title)
book_with_hero(url, d, h , n_heroname)
