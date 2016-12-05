"""Find the next departure time of a bus."""


class FindBusTime:
    """Class for finding the time of the next bus departure."""

    def __init__(self):
        """Class constructor."""
        self.message = "Write your current time! "
        self.dict_of_times = {}

    def get_message(self):
        """Get message."""
        return self.message

    def file_to_dict(self):
        """Convert info from txt.file to the dictionary."""
        y = open("bussiajad.txt", "r")
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
        if hour in range(0, 5):
            return "Your buss will departure at 5:26"
        if hour == 23:
            range_of_minutes = self.dict_of_times[hour]
            if minutes > range_of_minutes[-1]:
                return "Your buss will departure at 5:26"
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

    def find_time(self):
        """Find next bus departure basing on the given time."""
        user_input = input(self.search.get_message())
        self.search.file_to_dict()
        return self.search.find_time(user_input)


find_bus_time = FindBusTime()
info_from_user = AskUser(find_bus_time)
print(info_from_user.find_time())
