class Clock:
    def __init__(self, hour, minute):
        self._total_minutes = (hour * 60 + minute) % (24 * 60)

    @property
    def hour(self):
        return (self._total_minutes // 60) % 24

    @property
    def minute(self):
        return self._total_minutes % 60
    
    def __repr__(self):
        return f"Clock({self.hour}, {self.minute})"
    
    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}"

    def __eq__(self, other):
        if not isinstance(other, Clock):
            return False
            
        return self._total_minutes == other._total_minutes
    
    def __add__(self, minutes):
        return Clock(self.hour, self.minute + minutes)
    
    def __sub__(self, minutes):
        return Clock(self.hour, self.minute - minutes)
