# -*- coding: utf-8 -*-
import random
from time import sleep
from IPython.display import clear_output


def generate_random_phrase(num):
    if num == 1:
        bank = ["Тут миленько!", "Если честно: планетка так себе.", "Тут холодно! Можно назад?",
                "Как-то тут попахивает неприятно!", "А можно в следующий раз в Диснейленд?",
                "Говори, человек, что дальше?", "Готов к приключениям!", "Лалала-лала, все будет хорошо!",
                "Жду дальнейших указаний!", "Надеюсь, вы уверены, что нам это надо.", "Готов к работе, как никогда!",
                "Чудо планета!", "Йуху!!!!", "Ура!!!", "Отличная планета!", "Чувствую будет несладко!"]
        return bank[random.randint(0, len(bank) - 1)]
    return ""


class Planet:
    def __init__(self, width=6, height=7, base_x=0, base_y=0, hills=0, shape="Square"):
        self.area = [[dict() for i in range(height)] for j in range(width)]
        self.width = width
        self.height = height
        self.shape = shape
        for i in range(width):
            for j in range(height):
                self.area[i][j]["surface"] = 0
                self.area[i][j]["artifacts"] = []
        ready_hills = 0
        while ready_hills < hills:
            hill_x = random.randint(0, width - 1)
            hill_y = random.randint(0, height - 1)
            if self.area[hill_x][hill_y]["surface"] == 0 and (hill_x != base_x or hill_y != base_y):
                self.area[hill_x][hill_y]["surface"] = 1
                ready_hills += 1
        self.area[base_x][base_y]["objects"] = ["База"]
        self.base_x = base_x
        self.base_y = base_y

    def place_objects(self, obj_amount, obj_name):
        ready_objs = 0
        while ready_objs < obj_amount:
            obj_x = random.randint(0, self.width - 1)
            obj_y = random.randint(0, self.height - 1)
            if self.area[obj_x][obj_y]["surface"] == 0 and obj_name not in self.area[obj_x][obj_y]["artifacts"] and (
                    obj_x != self.base_x or obj_y != self.base_y):
                self.area[obj_x][obj_y]["artifacts"].append(obj_name)
                ready_objs += 1


def generate_random_hilled_planet():
    ground_9 = Planet(base_x=1, base_y=0, hills=10)
    return ground_9


def generate_real_planet(player):
    ground_10 = Planet(width=4, height=5, base_x=1, base_y=0, shape="Sphere")
    ground_10.area[0][0]["surface"] = 1
    ground_10.area[0][1]["surface"] = 1
    ground_10.area[0][2]["surface"] = 1
    ground_10.area[1][2]["surface"] = 1
    ground_10.area[0][4]["surface"] = 1
    ground_10.area[3][0]["surface"] = 1
    ground_10.area[3][3]["surface"] = 1
    ground_10.area[3][4]["surface"] = 1
    ground_10.place_objects(1, "Золото")
    if player == 1:
        return ground_10
    else:
        ground_11 = Planet(width=ground_10.height, height=ground_10.width, base_x=ground_10.base_y,
                           base_y=ground_10.base_y, shape="Sphere")
        for i in range(ground_11.width):
            for j in range(ground_11.height):
                ground_11.area[i][j]["surface"] = ground_10.area[j][i]["surface"]
                ground_11.area[i][j]["artifacts"] = ground_10.area[j][i]["artifacts"]


def renew_resources():
    ground_1 = Planet(base_x=1, base_y=0)
    ground_1.area[1][3]["artifacts"] = ["Яблоко"]

    ground_2 = Planet(base_x=1, base_y=0, width=1000, height=1000)
    ground_2.area[2][1]["artifacts"] = ["Яблоко"]
    ground_2.area[1][777]["artifacts"] = ["Пульт от телевизора"]

    ground_3 = Planet(base_x=1, base_y=0)
    ground_3.area[1][1]["artifacts"] = ["Банан"]
    ground_3.area[1][2]["artifacts"] = ["Яблоко"]
    ground_3.area[1][3]["artifacts"] = ["Яблоко"]
    ground_3.area[2][3]["artifacts"] = ["Банан"]
    ground_3.area[3][3]["artifacts"] = ["Банан"]
    ground_3.area[4][3]["artifacts"] = ["Банан"]
    ground_3.area[4][2]["artifacts"] = ["Яблоко"]
    ground_3.area[4][1]["artifacts"] = ["Яблоко"]
    ground_3.area[4][0]["artifacts"] = ["Банан"]
    ground_3.area[3][0]["artifacts"] = ["Банан"]
    ground_3.area[2][0]["artifacts"] = ["Банан"]

    ground_4 = Planet(base_x=1, base_y=0)
    ground_4.area[2][1]["artifacts"] = ["Котик"]
    ground_4.area[1][2]["artifacts"] = ["Котик"]
    ground_4.area[2][3]["artifacts"] = ["Котик"]
    ground_4.area[1][4]["artifacts"] = ["Котик"]

    ground_5 = Planet(width=100, height=1000, base_x=0, base_y=0)
    for i in range(ground_5.width):
        for j in range(ground_5.height):
            ground_5.area[i][j]["artifacts"] = ["Рис"]

    ground_6 = Planet(base_x=2, base_y=2)
    ground_6.area[2][1]["artifacts"] = ["Камушек"]
    ground_6.area[1][2]["artifacts"] = ["Странный предмет"]
    ground_6.area[2][3]["artifacts"] = ["Палка колбасы"]
    ground_6.area[3][2]["artifacts"] = ["Хомяк"]

    ground_7 = Planet(base_x=2, base_y=2)
    ground_7.area[2][1]["artifacts"] = ["Мина"]
    ground_7.area[1][2]["artifacts"] = ["Пельмешек"]
    ground_7.area[2][3]["artifacts"] = ["Мина"]
    ground_7.area[3][2]["artifacts"] = ["Мина"]

    ground_8 = Planet(width=5, height=random.randint(100, 1000), base_x=1, base_y=0)
    ground_8.area[1][ground_8.height - 1]["artifacts"] = ["Подорожник"]

    ground_9 = Planet(width=100, height=1000, base_x=0, base_y=0)
    for i in range(ground_9.width):
        for j in range(ground_9.height):
            ground_9.area[i][j]["artifacts"] = ["Рис"]
    ground_9.area[51][215]["artifacts"] = ["Мина"]

    ground_10 = generate_random_hilled_planet()
    ground_11 = generate_random_hilled_planet()
    ground_12 = generate_real_planet(1)
    ground_13 = generate_real_planet(2)

    return [None, ground_1, ground_2, ground_3, ground_4, ground_5, ground_6, ground_7, ground_8, ground_9, ground_10,
            ground_11, ground_12, ground_13]


class Shuttle:
    def __init__(self):
        self.direction = "North"
        self.box = dict()
        self.__planet = None
        self.time = 0
        self.cells = None
        self.unigue_cells = None
        self.test = None
        self.photo = None
        self.history = []

    def go_to_planet(self, planet):
        self.direction = "North"
        if planet == None:
            print("Такой планеты не существует.")
            return
        print("Я переместился на указанную планету. " + generate_random_phrase(1))
        self.__planet = planet
        self.__x = planet.base_x
        self.__y = planet.base_y
        self.history = [(self.__x, self.__y)]
        self.map = dict()
        self.map[planet] = [[False for i in range(planet.width * 10)] for j in range(planet.height * 10)]
        self.unigue_cells = 0
        self.cells = 0
        self.time = 0

    def show_stat(self):
        if self.__planet is None:
            print("Сначала переместите меня на планету.")
            return
        print("Местное время: {} минут".format(self.time))
        print("Пройдено клеток: {}".format(self.cells))
        print("Пройдено уникальных клеток: {}".format(self.unigue_cells))
        print("Исследовано {}% процентов планеты".format(
            100 * self.unigue_cells / (self.__planet.width * self.__planet.height)))

    def restart_stat(self):
        print("Статистика сброшена")
        self.time = 0
        self.cells = 0
        self.unigue_cells = 0
        self.map[self.__planet] = [[False for i in range(planet.width)] for j in range(planet.height)]

    def return_to_base(self):

        print("Я на базе. Смотрю на Север.")
        self.__x = self.__planet.base_x
        self.__y = self.__planet.base_y
        self.history = [(self.__x, self.__y)]
        self.direction = "North"

    def go(self):
        self.time += 1
        if self.__planet is None:
            print("Сначала переместите меня на планету.")
        else:
            shift = {
                "North": (0, 1),
                "East": (1, 0),
                "West": (-1, 0),
                "South": (0, -1)
            }
            x = self.__x + shift[self.direction][0]
            y = self.__y + shift[self.direction][1]
            if self.__planet.shape in ["Square", "Torus"] and (x < 0 or x >= self.__planet.width):
                print("Я свалился с поверхности планеты.")
                return
            if self.__planet.shape in ["Square"] and (y < 0 or y >= self.__planet.height):
                print("Я свалился с поверхности планеты.")
                return
            x %= self.__planet.width
            y %= self.__planet.height
            if self.__planet.area[x][y]["surface"] == 0:
                self.__x = x
                self.__y = y
                self.history.append((x, y))
                self.cells += 1
                if not self.map[self.__planet][x][y]:
                    self.map[self.__planet][x][y] = True
                    self.unigue_cells += 1
                for obj in self.__planet.area[x][y]["artifacts"]:
                    if obj in self.box.keys():
                        self.box[obj] += 1
                    else:
                        self.box[obj] = 1
                self.__planet.area[x][y]["artifacts"] = []

    def rotate(self):
        dirs = {
            "North": "East",
            "West": "North",
            "East": "South",
            "South": "West"
        }
        self.direction = dirs[self.direction]

    def show_box(self):
        if len(self.box.keys()) == 0:
            print("Мой кузов пуст")
            return
        print("Содержимое моего кузова:")
        for obj in self.box.keys():
            print("{}: {} шт.".format(obj, self.box[obj]))

    def empty_box(self):
        print("Я опустошил свой кузов.")
        self.box = dict()

    def restart_time(self):
        self.time = 0

    def get_sensor(self, direction):
        shift = {
            "North": (0, 1),
            "East": (1, 0),
            "West": (-1, 0),
            "South": (0, -1)
        }
        x = self.__x + shift[direction][0]
        y = self.__y + shift[direction][1]
        if self.__planet.shape in ["Square", "Torus"] and (x < 0 or x >= self.__planet.width):
            return "Космос"
        if self.__planet.shape in ["Square"] and (y < 0 or y >= self.__planet.height):
            return "Космос"
        x %= self.__planet.width
        y %= self.__planet.height
        if self.__planet.area[x][y]["surface"] != 0:
            return "Холм"
        if len(self.__planet.area[x][y]["artifacts"]) == 1:
            return self.__planet.area[x][y]["artifacts"][0]
        if len(self.__planet.area[x][y]["artifacts"]) != 0:
            return self.__planet.area[x][y]["artifacts"]
        return "Пустота"

    def take_test(self):
        self.test = "Полезных ископаемых"

    def take_photo(self):
        self.photo = self.get_sensor("North")

    def show_test(self):
        if self.test is None:
            print("Тестов проведено не было")
            return
        print(self.test)

    def show_photo(self):
        if self.photo is None:
            print("Я ничего не фотографировал.")
            return
        print("Последнее фото:{}".format(self.photo))

    def show_coordinate(self):
        print((self.__x, self.__y))

    def get_planet(self):
        return self.__planet

def visualize(shuttles, delay=3, mode="animation", planet=None):
    time = max([len(shuttle.history) for shuttle in shuttles])
    if planet == None:
        planet = shuttles[0].get_planet()

    print(shuttles[0].history)
    print(planet.area)
    z = input()

    for t in range(time):
        area = ""
        for h in range(planet.width):
            for w in range(planet.height):
                if len(planet.area[h][w]["artifacts"]) > 0:
                    symb = "*"
                else:
                    if planet.area[h][w]["surface"] > 0:
                        symb = "#"
                    else:
                        symb = " "
                        num = 0
                        for i in range(len(shuttles)):
                            if len(shuttles[i].history) >= time:
                                if shuttles[i].history[t][0] == h and shuttles[i].history[t][1] == w:
                                    num += i + 1
                        if num > 0:
                            symb = str(num)
                area += symb + "|"
            area += "\n"
        print(area)
        if mode == "input":
            waiting = input()
        else:
            sleep(delay)
        clear_output()

