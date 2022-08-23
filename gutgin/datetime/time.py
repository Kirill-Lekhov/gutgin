from typing import Optional, Tuple


class Time:
    def __init__(self, initial: Optional[str] = None, divider: str = ':'):
        self.hour: int = 0
        self.minute: int = 0
        self.second: int = 0
        self.divider: str = divider

        if initial is not None:
            self.hour, self.minute, self.second = self.parse_time(initial, divider)
            self.normalize_time()

    @staticmethod
    def parse_time(val: str, divider: str = ':') -> Tuple[int, int, int]:
        cleaned_val = ''.join(filter(lambda x: x.isdigit() or x == divider, val))
        time_parts = tuple(map(int, cleaned_val.split(divider)))
        time_parts_number = len(time_parts)

        if time_parts_number == 1:
            return 0, 0, time_parts[0]

        elif time_parts_number == 2:
            return 0, time_parts[0], time_parts[1]

        elif time_parts_number == 3:
            return time_parts

        raise ValueError(f"Can't parse time from: '{val}'")

    def normalize_time(self) -> None:
        _minute, self.second = divmod(self.second, 60)
        _hour, self.minute = divmod(self.minute, 60)
        self.minute += _minute
        self.hour += _hour

    def __add__(self, other):
        assert isinstance(other, self.__class__), "Not implemented"

        new_obj = Time()
        new_obj.hour = self.hour + other.hour
        new_obj.minute = self.minute + other.minute
        new_obj.second = self.second + other.second
        new_obj.normalize_time()

        return new_obj

    def __str__(self) -> str:
        return f'{self.hour}:{self.minute:02}:{self.second:02}'


def demo():
    time1_v, time2_v, time3_v = '535', '15:11', '23:59:16'
    time1, time2, time3 = Time(time1_v), Time(time2_v), Time(time3_v)

    print(f"\nI have three time's values:\t\ttime1={time1_v}, time2={time2_v}, time3={time3_v}")
    print(f"When i parse they, i got:\t\ttime1={time1}, time2={time2}, time3={time3}")
    print(f"When i sum they, i got:\t\t\ttime={time1+time2+time3}", end='\n\n')
