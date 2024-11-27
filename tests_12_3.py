import unittest
import runner


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner1 = runner.Runner('runner1')
        for i in range(10):
            runner1.walk()
        self.assertEqual(runner1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner2 = runner.Runner('runner2')
        for i in range(10):
            runner2.run()
        self.assertEqual(runner2.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge (self):
        runner1 = runner.Runner('runner1')
        runner2 = runner.Runner('runner2')
        for i in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)



import runner_and_tournament


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
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

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
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

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
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

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
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

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
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
