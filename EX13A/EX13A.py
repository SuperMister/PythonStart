"""Find the next departure time of a bus."""


class FindBusTime:
    """Class for finding the time of the next bus departure."""

    def __init__(self, file):
        """Class constructor."""
        self.message = "Write your current time: "
        self.dict_of_times = {}
        self.file = file

    def get_message(self):
        """Get message."""
        return self.message

    def file_to_dict(self):
        """Convert info from txt.file to the dictionary."""
        y = open(self.file)
        hours = []
        minutes = []
        for i in y:
            hours.append(i.split("\t")[0])
            minutes.append(i.rstrip("\n").split("\t")[1])
        for x in range(len(hours)):
            self.dict_of_times[int(hours[x])] = minutes[x].split()
        return self.dict_of_times

    def find_time(self, input_time):
        """Find the time when will departure next bus."""
        hour = int(input_time.split(":")[0])
        minutes = int(input_time.split(":")[1])
        all_keys = len(list(self.dict_of_times.keys()))

        if hour not in list(self.dict_of_times.keys()):
            hour = list(self.dict_of_times)[0]
            minutes = self.dict_of_times[hour][0]
            return "Your buss will departure at " + str(hour) + ":" + minutes

        if hour == list(self.dict_of_times.keys())[all_keys - 1]:
            range_of_minutes = self.dict_of_times[hour]
            if minutes > int(range_of_minutes[-1]):
                hour = list(self.dict_of_times)[0]
                minutes = self.dict_of_times[hour][0]
                return "Your buss will departure at " + str(hour) + ":" + minutes

        range_of_minutes = self.dict_of_times[hour]
        for i in range(len(range_of_minutes)):
            if minutes <= int(range_of_minutes[i]):
                minutes = int(range_of_minutes[i])
                break
            elif minutes > int(range_of_minutes[len(range_of_minutes) - 1]):
                hour += 1
                range_of_minutes = self.dict_of_times[hour]
                minutes = range_of_minutes[0]
                break
        return "Your buss will departure at " + str(hour) + ":" + str(minutes)


class AskUser:
    """Class for asking user input information."""

    def __init__(self, search):
        """Class constructor."""
        self.search = search

    def find_user_time(self):
        """Find next bus departure basing on the given time."""
        while True:
            user_input = input(self.search.get_message())
            try:
                int(user_input.split(":")[0]) is int()
                int(user_input.split(":")[1]) is int()
            except ValueError:
                print("Please use numbers only or use " + "\"" + ":" + "\"" + " between hours and minutes!")
                continue
            if int(user_input.split(":")[1]) not in range(0, 60):
                print("Minutes should be in range 0-60!")
                continue
            if int(user_input.split(":")[0]) not in range(0, 23):
                print("Hours should be in range 0-23!")
                continue
            break
        self.search.file_to_dict()
        return self.search.find_time(user_input)


find_bus_time = FindBusTime("bussiajad.txt")
info_from_user = AskUser(find_bus_time)
print(info_from_user.find_user_time())
