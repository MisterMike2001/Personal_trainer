from models.tracker.workout_session_model import WorkoutSession
from schemas.tracker.workout_session_schema import GetWorkoutSession,CreateWorkoutSession, UpdateWorkoutSession

class WorkoutSessionRepository:
    def __init__(self,db):
        self.db =db
    
    def get_workout_sessions(self, user_id:int)->list[GetWorkoutSession]:
        workout_sessions = self.db.query(WorkoutSession).filter(WorkoutSession.user_id == user_id).all()
        return workout_sessions
    
    def create_workout_session(self, workout_session: CreateWorkoutSession):
        session = WorkoutSession(** workout_session.model_dump())

        self.db.add(session)
        self.db.commit()
        self.db.refresh(session)

        return session

    def update_workout_session(self,updated_workout_session: UpdateWorkoutSession):
        workout_session = self.db.query(WorkoutSession).filter(WorkoutSession.id == updated_workout_session.id).first()

        if not workout_session:
            return None
        changes = updated_workout_session.model_dump(exclude_unset=True)

        for field, value in changes.items():
            setattr(workout_session, field, value)

        self.db.commit()
        self.db.refresh(workout_session)
        return workout_session