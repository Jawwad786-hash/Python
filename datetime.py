print("Mohd.Jawwad Ali Farooqui, USN:1AY24AI070, SEC:O")
class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    def total_seconds(self):
        """Returns total time in seconds"""
        return self.hours * 3600 + self.minutes * 60 + self.seconds
    @classmethod
    def from_seconds(cls, total_secs):
        """Creates a Time object from total seconds"""
        hours = total_secs // 3600
        remainder = total_secs % 3600
        minutes = remainder // 60
        seconds = remainder % 60
        return cls(int(hours), int(minutes), int(seconds))

    def print_time(self):
        """Nicely formats and prints time"""
        print(f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}")
    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}
def mul_time(time_obj, factor):
    """Multiplies a Time object by a number"""
    total_secs = time_obj.total_seconds() * factor
    return Time.from_seconds(total_secs)
def avg_pace(finishing_time, distance):
    """Returns average pace (time per unit distance)"""
    return mul_time(finishing_time, 1 / distance)
# ----------- Example Usage -----------
if __name__ == "__main__":
    # Suppose you ran a 10-mile race in 1 hour 30 minutes (01:30:00)
    finish_time = Time(1, 30, 0)
    distance = 10 
    print("Finishing Time:", finish_time)
    pace = avg_pace(finish_time, distance)
    print("Average Pace (per mile):", pace)
