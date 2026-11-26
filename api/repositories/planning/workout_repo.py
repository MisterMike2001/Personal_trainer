from models.planning.workout_model import Workout
from schemas.planning.workout_schema import CreateWorkout, UpdateWorkout

class WorkoutRepository:
    def __init__(self, db):
        self.db = db

    def get_workouts(self, workout_plan_id: int) -> list[Workout]:
        workouts = self.db.query(Workout).filter(Workout.workout_plan_id == workout_plan_id).order_by(Workout.order_no).all()
        return workouts

    def create_workout(self, workout: CreateWorkout):
        new_workout = Workout(**workout.model_dump())
        self.db.add(new_workout)
        self.db.commit()
        self.db.refresh(new_workout)
        return new_workout

    def update_workout(self, updated_workout: UpdateWorkout) -> Workout | None:
        old_workout = self.db.query(Workout).filter(Workout.id == updated_workout.id, Workout.workout_plan_id == updated_workout.workout_plan_id).first()

        if old_workout is None:
            return None

        changes = updated_workout.model_dump(exclude_unset=True, exclude={"id", "workout_plan_id"})
        for field, value in changes.items():
            setattr(old_workout, field, value)

        self.db.commit()
        self.db.refresh(old_workout)
        return old_workout
