from abc import ABC, abstractmethod
import uuid


class Exercise(ABC):

    def __init__(self, name, duration_minutes, difficulty):
        self._id = str(uuid.uuid4())[:8]
        self._name = name
        self._duration_minutes = duration_minutes
        self._difficulty = difficulty
        self._is_completed = False

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def set_name(self, name):
        if len(name) > 2:
            self._name = name

    @abstractmethod
    def calculate_calories_burned(self, weight_kg):
        pass

    def complete(self):
        self._is_completed = True

    def __str__(self):
        return f"{self._name} ({self._duration_minutes}min, {self._difficulty})"


class Running(Exercise):
    def __init__(self, name, duration_minutes, difficulty, distance_km):
        super().__init__(name, duration_minutes, difficulty)
        self._distance_km = distance_km

    def calculate_calories_burned(self, weight_kg):
        return self._distance_km * weight_kg * 1.036

    def __str__(self):
        return f"{super().__str__()} - dystans: {self._distance_km}km"


class Swimming(Exercise):
    def __init__(self, name, duration_minutes, difficulty, style, laps):
        super().__init__(name, duration_minutes, difficulty)
        self._style = style
        self._laps = laps

    def calculate_calories_burned(self, weight_kg):
        return self._duration_minutes * 8.5

    def __str__(self):
        return f"{super().__str__()} - styl: {self._style}, długości: {self._laps}"


class WeightLifting(Exercise):
    def __init__(self, name, duration_minutes, difficulty, sets, reps, weight_kg):
        super().__init__(name, duration_minutes, difficulty)
        self._sets = sets
        self._reps = reps
        self._weight_kg = weight_kg

    def calculate_calories_burned(self, weight_kg):
        base = self._duration_minutes * 6
        extra = (self._weight_kg / 10) * self._sets
        return base + extra

    def __str__(self):
        return f"{super().__str__()} - {self._sets}x{self._reps} ({self._weight_kg}kg)"