from models.planning.exercises_model import Exercise
from schemas.planning.exercises_schema import CreateExercise, UpdateExercise

class ExerciseRepository:
    def __init__(self, db):
        self.db = db

    def get_exercises(self) -> list[Exercise]:
        exercises = self.db.query(Exercise).all()
        return exercises

    def create_exercise(self, exercise: CreateExercise):
        new_exercise = Exercise(**exercise.model_dump())
        self.db.add(new_exercise)
        self.db.commit()
        self.db.refresh(new_exercise)
        return new_exercise

    def update_exercise(self, updated_exercise: UpdateExercise) -> Exercise | None:
        old_exercise = self.db.query(Exercise).filter(Exercise.id == updated_exercise.id).first()

        if old_exercise is None:
            return None

        changes = updated_exercise.model_dump(exclude_unset=True, exclude={"id"})
        for field, value in changes.items():
            setattr(old_exercise, field, value)

        self.db.commit()
        self.db.refresh(old_exercise)
        return old_exercise
