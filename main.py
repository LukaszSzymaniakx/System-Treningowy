from models.exercise import Running, Swimming, WeightLifting
from models.user import Member, Trainer
from models.training_plan import TrainingPlan
from models.training_session import TrainingSession


def main():
    print("=== SYSTEM ZARZĄDZANIA TRENINGAMI FITNESS ===\n")

    running = Running("Poranny bieg", 30, "medium", 5.2)
    swimming = Swimming("Basen", 45, "hard", "motylkowy", 40)
    weights = WeightLifting("Klatka piersiowa", 20, "easy", 4, 12, 60)

    plan = TrainingPlan("FitStart", "medium", 4)
    plan.add_exercise(running)
    plan.add_exercise(swimming)
    plan.add_exercise(weights)
    plan.display_plan()

    trainer = Trainer("Anna Kowalska", "anna@fitness.pl", 32, "trening siłowy", 120)
    member = Member("Jan Nowak", "jan@example.com", 28, "premium", 78)


    member.assign_trainer(trainer)

    print("\n=== UŻYTKOWNICY SYSTEMU ===")
    print(member.display_info())
    print(trainer.display_info())


    print("\n=== ROZPOCZĘCIE SESJI TRENINGOWEJ ===")
    session = TrainingSession(member, plan)

    print("\n Wykonywanie ćwiczeń:")
    session.perform_exercise(0)
    session.perform_exercise(1)

    print(f"\n{session.get_progress()}")
    session.summary()


    member.add_training_session(session)

    print(f"\n Łącznie spalone kalorie we wszystkich sesjach: {member.get_total_calories_burned():.0f} kcal")


    print("\n=== DEMONSTRACJA POLIMORFIZMU ===")
    exercises = [running, swimming, weights]
    for ex in exercises:
        calories = ex.calculate_calories_burned(member.get_weight())
        print(f"{ex.get_name()}: {calories:.0f} kcal spalonych")
        print(f"  Typ obiektu: {type(ex).__name__}")
        print(f"  Szczegóły: {ex}\n")


if __name__ == "__main__":
    main()