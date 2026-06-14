from datetime import datetime


class TrainingSession:
    def __init__(self, member, plan, session_date=None):
        self._member = member
        self._plan = plan
        self._session_date = session_date or datetime.now()
        self._completed_exercises = []

    def perform_exercise(self, exercise_index):
        if exercise_index < len(self._plan.get_exercises()):
            ex = self._plan.get_exercises()[exercise_index]
            ex.complete()
            self._completed_exercises.append(ex)
            calories = ex.calculate_calories_burned(self._member.get_weight())
            print(f"Wykonano: {ex.get_name()} - spalone kalorie: {calories:.0f} kcal")
            return calories
        return 0

    def get_total_calories(self):
        total = 0
        for ex in self._completed_exercises:
            total += ex.calculate_calories_burned(self._member.get_weight())
        return total

    def get_progress(self):
        total_ex = len(self._plan.get_exercises())
        completed = len(self._completed_exercises)
        return f"Postęp: {completed}/{total_ex} ćwiczeń ({completed / total_ex * 100:.0f}%)" if total_ex > 0 else "Brak ćwiczeń"

    def summary(self):
        print(f"\n Sesja z dnia {self._session_date.strftime('%Y-%m-%d %H:%M')}")
        print(f"Uczestnik: {self._member.get_name()}")
        print(self.get_progress())
        print(f"Łącznie spalone kalorie: {self.get_total_calories():.0f} kcal")