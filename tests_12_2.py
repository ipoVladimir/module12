# Домашнее задание по теме "Методы Юнит-тестирования"
# Цель: освоить методы, которые содержит класс TestCase.
#
# Задача:
# В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub. (Можно скопировать)
# В этом коде сможете обнаружить дополненный с предыдущей задачи класс Runner и новый класс Tournament.
# Изменения в классе Runner:
#
#     Появился атрибут speed для определения скорости бегуна.
#     Метод __eq__ для сравнивания имён бегунов.
#     Переопределены методы run и walk, теперь изменение дистанции зависит от скорости.
#
# Класс Tournament представляет собой класс соревнований, где есть дистанция, которую нужно пробежать и список участников. Также присутствует метод start, который реализует логику бега по предложенной дистанции.
#
# Напишите класс TournamentTest, наследованный от TestCase. В нём реализуйте следующие методы:
#
# setUpClass - метод, где создаётся атрибут класса all_results. Это словарь в который будут сохраняться результаты всех тестов.
# setUp - метод, где создаются 3 объекта:
#
#     Бегун по имени Усэйн, со скоростью 10.
#     Бегун по имени Андрей, со скоростью 9.
#     Бегун по имени Ник, со скоростью 3.
#
# tearDownClass - метод, где выводятся all_results по очереди в столбец.
#
# Так же методы тестирования забегов, в которых создаётся объект Tournament на дистанцию 90. У объекта класса Tournament запускается метод start, который возвращает словарь в переменную all_results. В конце вызывается метод assertTrue, в котором сравниваются последний объект из all_results (брать по наибольшему ключу) и предполагаемое имя последнего бегуна.
# Напишите 3 таких метода, где в забегах участвуют (порядок передачи в объект Tournament соблюсти):
#
#     Усэйн и Ник
#     Андрей и Ник
#     Усэйн, Андрей и Ник.
#
# Как можно понять: Ник всегда должен быть последним.
#
# Дополнительно (не обязательно, не влияет на зачёт):
# В данной задаче, а именно в методе start класса Tournament, допущена логическая ошибка. В результате его работы бегун с меньшей скоростью может пробежать некоторые дистанции быстрее, чем бегун с большей.
# Попробуйте решить эту проблему и обложить дополнительными тестами.
# Пример результата выполнения тестов:
# Вывод на консоль:
# {1: Усэйн, 2: Ник}
# {1: Андрей, 2: Ник}
# {1: Андрей, 2: Усэйн, 3: Ник}
#
# Ran 3 tests in 0.001s
# OK
#
# Примечания:
#
#     Ваш код может отличаться от строгой последовательности описанной в задании. Главное - схожая логика работы тестов и наличие всех перечисленных переопределённых методов из класса TestCase.


import runner_and_tournament
import unittest


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.runUsein = runner_and_tournament.Runner("Усэйн", 10)
        self.runAndrei = runner_and_tournament.Runner("Андрей", 9)
        self.runNik = runner_and_tournament.Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        ind = 0
        #for key, val in cls.all_results.items():
        #    ind += 1
        #    print(f"{ind}) {key}: {val}")
        for ind in range(len(cls.all_results)):
            str_out = str(f"{ind + 1}) {{")
            for key, val in cls.all_results[ind].items():
                str_out += str(f"{key}: {val}, ")
            if len(cls.all_results[ind].items()) > 0:
                str_out = str_out[0:len(str_out)-2]
            str_out += "}"
            print(str_out)


    def test_start1(self):
        """
        Усэйн и Ник
        :return:
        """
        tournament = runner_and_tournament.Tournament(90, self.runUsein, self.runNik)
        #self.all_results.update(tournament.start())
        #self.assertTrue(max(self.all_results.items())[1], self.runNik)
        #print(f"{max(self.all_results.items())[1]}: {self.runNik}")
        res = tournament.start()
        self.all_results.append(res)
        self.assertTrue(max(res.items())[1] == self.runNik)
        # print(f"{max(res.items())[1]} == {self.runNik}")


    def test_start2(self):
        """
        Андрей и Ник
        :return:
        """
        tournament = runner_and_tournament.Tournament(90, self.runAndrei, self.runNik)
        # self.all_results.update(tournament.start())
        # self.assertTrue(max(self.all_results.items())[1], self.runNik)
        # print(f"{max(self.all_results.items())[1]}: {self.runNik}")
        res = tournament.start()
        self.all_results.append(res)
        self.assertTrue(max(res.items())[1] == self.runNik)
        # print(f"{max(res.items())[1]} == {self.runNik}")


    def test_start3(self):
        """
        Усэйн, Андрей и Ник.
        :return:
        """
        tournament = runner_and_tournament.Tournament(90, self.runUsein, self.runAndrei, self.runNik)
        # self.all_results.update(tournament.start())
        # self.assertTrue(max(self.all_results.items())[1], self.runNik)
        # print(f"{max(self.all_results.items())[1]}: {self.runNik}")
        res = tournament.start()
        self.all_results.append(res)
        self.assertTrue(max(res.items())[1] == self.runNik)
        # print(f"{max(res.items())[1]} == {self.runNik}")

    def test_start4(self):
        """
        Усэйн, Андрей и Ник.
        :return:
        """
        tournament = runner_and_tournament.Tournament(3, self.runUsein, self.runNik, self.runAndrei)
        # self.all_results.update(tournament.start())
        # self.assertTrue(max(self.all_results.items())[1], self.runNik)
        # print(f"{max(self.all_results.items())[1]}: {self.runNik}")
        res = tournament.start()
        self.all_results.append(res)
        self.assertTrue(max(res.items())[1] == self.runNik)
        # print(f"{max(res.items())[1]} == {self.runNik}")


if __name__ == "__main__":
    unittest.main()