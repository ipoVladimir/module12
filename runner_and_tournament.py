class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        #self.participants = list(participants)
        self.participants = self.sort_participants_by_speed(*participants)

    def sort_participants_by_speed(self, *participants):
        ls_parts = list(participants)

        for cur_ind in range(len(ls_parts)-1):
            max_speed_ind = cur_ind
            for i in range(cur_ind+1, len(ls_parts)):
                if ls_parts[max_speed_ind].speed < ls_parts[i].speed:
                    max_speed_ind = i
            ls_parts[cur_ind], ls_parts[max_speed_ind] = ls_parts[max_speed_ind], ls_parts[cur_ind]

        return ls_parts


    def print_participants(self):
        print("[", end="")
        for it in self.participants:
            print(f"{it}, ", end="")
        print("]")

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            rem_part = []
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    rem_part.append(participant)
                    #self.participants.remove(participant)
            for it in rem_part:
                self.participants.remove(it)

        return finishers
