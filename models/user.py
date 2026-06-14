import uuid


class User:
    def __init__(self, name, email, age):
        self._id = str(uuid.uuid4())[:8]
        self._name = name
        self._email = email
        self._age = age
        self._training_history = []

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def add_training_session(self, session):
        self._training_history.append(session)

    def get_total_calories_burned(self):
        return sum(session.get_total_calories() for session in self._training_history)

    def display_info(self):
        return f"{self._name} ({self._email}), wiek: {self._age}"

    def get_role(self):
        return "Użytkownik"


class Member(User):
    def __init__(self, name, email, age, membership_type, weight_kg):
        super().__init__(name, email, age)
        self._membership_type = membership_type
        self._weight_kg = weight_kg
        self._assigned_trainer = None

    def assign_trainer(self, trainer):
        if isinstance(trainer, Trainer):
            self._assigned_trainer = trainer
            trainer.add_member(self)

    def get_role(self):
        return f"Klubowicz (karnet {self._membership_type})"

    def get_weight(self):
        return self._weight_kg

    def display_info(self):
        base = super().display_info()
        trainer_name = self._assigned_trainer.get_name() if self._assigned_trainer else "brak"
        return f"{base} | {self.get_role()} | waga: {self._weight_kg}kg | trener: {trainer_name}"


class Trainer(User):
    def __init__(self, name, email, age, specialization, hourly_rate):
        super().__init__(name, email, age)
        self._specialization = specialization
        self._hourly_rate = hourly_rate
        self._members = []

    def add_member(self, member):
        if member not in self._members:
            self._members.append(member)

    def get_role(self):
        return f"Trener ({self._specialization})"

    def display_info(self):
        base = super().display_info()
        return f"{base} | {self.get_role()} | stawka: {self._hourly_rate} zł/h | liczba podopiecznych: {len(self._members)}"