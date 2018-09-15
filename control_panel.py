# -*- coding: utf-8 -*-
import random
class Planet:
    def __init__(self, width=6, height=6, base_x = 0, base_y = 0, hills=0, shape="Square"):
        self.area = [[dict() for i in range(width)] for j in range(height)]
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
            if self.area[obj_x][obj_y]["surface"] == 0 and obj_name not in self.area[obj_x][obj_y]["artifacts"] and (obj_x != self.base_x or obj_y != self.base_y):
                self.area[obj_x][obj_y]["artifacts"].append(obj_name)
                ready_objs += 1

def generate_planet_9():
    ground_9 = Planet(base_x=1, base_y=0, hills = 10)
    return ground_9


def generate_planet_10():
    ground_10 = Planet(base_x=1, base_y=0, shape="Sphere")
    ground_10.area[0][0]["surface"] = 1
    ground_10.area[0][1]["surface"] = 1
    ground_10.area[0][2]["surface"] = 1
    ground_10.area[1][2]["surface"] = 1
    ground_10.area[0][4]["surface"] = 1
    ground_10.area[3][0]["surface"] = 1
    ground_10.area[3][3]["surface"] = 1
    ground_10.area[3][4]["surface"] = 1
    ground_10.place_objects(1, "Золото")
    return ground_10

def renew_resources():
    ground_1 = Planet(base_x=1, base_y=0)
    ground_1.area[1][3]["artifacts"] = ["Яблоко"]

    ground_2 = Planet(base_x=1, base_y=0)
    ground_2.area[2][1]["artifacts"] = ["Яблоко"]

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

    ground_7 = Planet(base_x=1, base_y=0)
    ground_7.area[4][3]["artifacts"] = ["Бомба"]

    ground_8 = Planet(base_x=1, base_y=0, hills=10)
    ground_8.place_objects(10, "Подорожник")

    ground_9 = generate_planet_9()
    ground_10 = generate_planet_10()

    return [None, ground_1, ground_2, ground_3, ground_4, None, None, ground_7, ground_8, ground_9, ground_10]


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

    def go_to_planet(self, planet):
        self.__planet = planet
        self.__x = planet.base_x
        self.__y = planet.base_y
        self.map = dict()
        self.map[planet] = [[False for i in range(planet.width)] for j in range(planet.height)]
        self.unigue_cells = 0
        self.cells = 0
        self.time = 0

    def get_stat(self):
        if self.__planet is None:
            print("Сначала переместите меня на планету.")
            return
        print("Время в движении: {}".format(self.time))
        print("Пройдено клеток: {}".format(self.cells))
        print("Пройдено уникальных клеток: {}".format(self.unigue_cells))

    def restart_stat(self):
        self.time = 0
        self.cells = 0
        self.unigue_cells = 0
        self.map[self.__planet] = [[False for i in range(planet.width)] for j in range(planet.height)]

    def return_to_base(self):
        self.__x = self.__planet.base_x
        self.__y = self.__planet.base_y

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
                self.cells += 1
                if not self.map[self.__planet][x][y]:
                    self.map[self.__planet][x][y] = True
                    self.unigue_cells += 1
                for obj in self.__planet.area[x][y]["artifacts"]:
                    if obj in self.box:
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
        x = self.__x + shift[self.direction][0]
        y = self.__y + shift[self.direction][1]
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





