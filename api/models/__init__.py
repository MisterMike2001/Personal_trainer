"""Register all table mappings on the shared SQLAlchemy metadata."""

from models.base import Base
from models.auth.users_model import User
from models.auth.refresh_session_model import RefreshSession
from models.planning.equipement_model import Equipment
from models.planning.exercises_model import Exercise
from models.planning.muscle_groups_model import MuscleGroup
from models.planning.excersise_mussle_groups_model import ExerciseMuscleGroup
from models.planning.workout_plan_model import WorkoutPlan
from models.planning.workout_model import Workout
from models.planning.workout_exercises_model import WorkoutExercise
from models.planning.workout_exercise_set_model import WorkoutExerciseSet
from models.planning.workout_muscle_groups_model import WorkoutMuscleGroup
from models.profile.progress_photis_model import ProgressPhoto
from models.profile.user_measurements_model import UserMeasurements
from models.profile.user_profile_model import UserProfile
from models.profile.user_weight_model import UserWeight
from models.tracker.workout_session_model import WorkoutSession
from models.tracker.workout_session_exercise_model import WorkoutSessionExercise
from models.tracker.workout_session_exercise_set_model import WorkoutSessionExerciseSet
