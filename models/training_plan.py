class TrainingPlan:
    def __init__(self, name, difficulty, duration_weeks):
        self._name = name
        self._difficulty = difficulty
        self._duration_weeks = duration_weeks
        self._exercises = []

    def add_exercise(self, exercise):
        self._exercises.append(exercise)

    def get_exercises(self):
        return self._exercises.copy()

    def get_total_duration_minutes(self):
        return sum(ex._duration_minutes for ex in self._exercises)

    def display_plan(self):
        print(f"\n Plan: {self._name} (trudność: {self._difficulty}, {self._duration_weeks} tyg)")
        for i, ex in enumerate(self._exercises, 1):
            print(f"  {i}. {ex}")