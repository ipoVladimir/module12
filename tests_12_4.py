# Домашнее задание по теме "Логирование"
# Если вы решали старую версию задачи, проверка будет производиться по ней.
# Ссылка на старую версию тут.
# Цель: получить опыт использования простейшего логирования совместно с тестами.
#
# Задача "Логирование бегунов":
# В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub. (Можно скопировать)
# Основное обновление - выбрасывание исключений, если передан неверный тип в name и если передано отрицательное значение в speed.
#
# Для решения этой задачи вам понадобиться класс RunnerTest из предыдущей задачи.
# В модуле tests_12_4.py импортируйте пакет logging и настройте basicConfig на следующие параметры:
#
#     Уровень - INFO
#     Режим - запись с заменой('w')
#     Название файла - runner_tests.log
#     Кодировка - UTF-8
#     Формат вывода - на своё усмотрение, обязательная информация: уровень логирования, сообщение логирования.
#
#
# Дополните методы тестирования в классе RunnerTest следующим образом:
# test_walk:
#
#     Оберните основной код конструкцией try-except.
#     При создании объекта Runner передавайте отрицательное значение в speed.
#     В блок try добавьте логирование INFO с сообщением '"test_walk" выполнен успешно'
#     В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING с сообщением "Неверная скорость для Runner".
#
# test_run:
#
#     Оберните основной код конструкцией try-except.
#     При создании объекта Runner передавайте что-то кроме строки в name.
#     В блок try добавьте логирование INFO с сообщением '"test_run" выполнен успешно'
#     В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING с сообщением "Неверный тип данных для объекта Runner".
#
# Пример результата выполнения программы:
# Пример полученного файла логов runner_tests.log:

import logging
import unittest
import rt_with_exceptions


logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding="UTF-8",
                   format="%(asctime)s - %(levelname)s - %(message)s")


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            runner1 = rt_with_exceptions.Runner('runner1', -5)
            for i in range(10):
                runner1.walk()
            self.assertEqual(runner1.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except TypeError as er:
            logging.warning("Неверный тип данных для объекта Runner (" + str(er) + ")", exc_info=True)
        except ValueError as er:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            runner2 = rt_with_exceptions.Runner(self)
            for i in range(10):
                runner2.run()
            self.assertEqual(runner2.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as er:
            logging.warning("Неверный тип данных для объекта Runner (" + str(er) + ")", exc_info=True)
        except ValueError as er:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge (self):
        runner1 = rt_with_exceptions.Runner('runner1')
        runner2 = rt_with_exceptions.Runner('runner2')
        for i in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == "__main__":
    unittest.main()



