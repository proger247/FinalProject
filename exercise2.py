import requests
from bs4 import BeautifulSoup


car_list = []
numbers = []
def extra_word(list):
    """Функция выделяет ключевые слова(марки машин) из тескта"""

    for k in range(len(car_list)):
        extra = car_list[k].split()

        for x in range(len(extra)):

            if 'Mercedes-Benz' in extra[x] :
                car_list[k] = 'Mercedes-Benz'
                print('ok')
                break
            else:
                if extra[x].isalpha():
                    car_list[k]= extra[x]
                    break

# def calculate(b):
#     for q in range(len(b)):
#         k = 0
#         for w in range(len(b)):
#             if b[q] == b[w]:
#                 k += 1
#         numbers.append(k)
#     print(numbers)

k = requests.get("https://spb.autospot.ru/used-car/")
bsoup = BeautifulSoup(k.text, "html.parser")
result = bsoup.select('.filters-car-top__mark-model')

for i in range(len(result)):
  car_list.append(result[-i-1].text)


print(car_list)
extra_word(car_list)
calculate(car_list)
print(car_list)

