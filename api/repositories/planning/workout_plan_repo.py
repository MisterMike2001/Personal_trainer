from models.planning.workout_plan_model import WorkoutPlan
from schemas.planning.workout_plan_schema import CreateWorkoutPlan, UpdateWorkoutPlan

class WorkoutPlanRepository:
    def __init__(self, db):
        self.db = db

    def get_workout_plans(self, user_id: int) -> list[WorkoutPlan]:
        workout_plans = self.db.query(WorkoutPlan).filter(WorkoutPlan.user_id == user_id).all()
        return workout_plans

    def create_workout_plan(self, workout_plan: CreateWorkoutPlan):
        new_workout_plan = WorkoutPlan(**workout_plan.model_dump())
        self.db.add(new_workout_plan)
        self.db.commit()
        self.db.refresh(new_workout_plan)
        return new_workout_plan

    def update_workout_plan(self, updated_workout_plan: UpdateWorkoutPlan) -> WorkoutPlan | None:
        old_workout_plan = self.db.query(WorkoutPlan).filter(WorkoutPlan.id == updated_workout_plan.id, WorkoutPlan.user_id == updated_workout_plan.user_id).first()

        if old_workout_plan is None:
            return None

        changes = updated_workout_plan.model_dump(exclude_unset=True, exclude={"id", "user_id"})
        for field, value in changes.items():
            setattr(old_workout_plan, field, value)

        self.db.commit()
        self.db.refresh(old_workout_plan)
        return old_workout_plan
