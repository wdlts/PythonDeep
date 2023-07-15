# 4. Создайте словарь со списком вещей для похода в качестве ключа
# и их массой в качестве значения. Определите какие вещи влезут в
# рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть
# один допустимый вариант.

maxkg = 20

backpack = []
backpackkg = 0

things = {'food':10, 'tent':4, 'boots':3, 'sleeping bag':16, 'smartphone':1, 'matchstiks':1, 'knife':2}

for k, v in things.items():
    if (backpackkg + v) >= maxkg:
        continue
    else:
        backpack.append(k)
        backpackkg+=v

print(backpack)