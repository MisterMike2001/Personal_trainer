
-- ============================================
-- CREATE TRACKER SCHEMA
-- ============================================

CREATE SCHEMA IF NOT EXISTS tracker;


-- ============================================
-- 1. WORKOUT SESSION
-- ============================================

CREATE TABLE IF NOT EXISTS tracker.workout_session (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    user_id INTEGER NOT NULL,
    workout_id INTEGER,

    start_dt TIMESTAMPTZ NOT NULL
        DEFAULT CURRENT_TIMESTAMP,

    end_dt TIMESTAMPTZ,

    status VARCHAR(20) NOT NULL
        DEFAULT 'in_progress',

    create_dt TIMESTAMPTZ NOT NULL
        DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_workout_session_user
        FOREIGN KEY (user_id)
        REFERENCES auth.users(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_workout_session_workout
        FOREIGN KEY (workout_id)
        REFERENCES planning.workout(id)
        ON DELETE SET NULL,

    CONSTRAINT chk_workout_session_status
        CHECK (
            status IN (
                'in_progress',
                'completed',
                'cancelled'
            )
        ),

    CONSTRAINT chk_workout_session_dates
        CHECK (
            end_dt IS NULL
            OR end_dt >= start_dt
        )
);


-- ============================================
-- 2. WORKOUT SESSION EXERCISES
-- ============================================

CREATE TABLE IF NOT EXISTS tracker.workout_session_exercise (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    workout_session_id INTEGER NOT NULL,
    exercise_id INTEGER NOT NULL,

    workout_exercise_id INTEGER,

    exercise_order INTEGER NOT NULL,

    create_dt TIMESTAMPTZ NOT NULL
        DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_session_exercise_session
        FOREIGN KEY (workout_session_id)
        REFERENCES tracker.workout_session(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_session_exercise_exercise
        FOREIGN KEY (exercise_id)
        REFERENCES planning.exercises(id)
        ON DELETE RESTRICT,

    CONSTRAINT fk_session_exercise_planned
        FOREIGN KEY (workout_exercise_id)
        REFERENCES planning.workout_exercise(id)
        ON DELETE SET NULL,

    CONSTRAINT chk_session_exercise_order
        CHECK (exercise_order > 0),

    CONSTRAINT uq_session_exercise_order
        UNIQUE (workout_session_id, exercise_order)
);


-- ============================================
-- 3. WORKOUT SESSION EXERCISE SETS
-- ============================================

CREATE TABLE IF NOT EXISTS tracker.workout_session_exercise_set (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    workout_session_exercise_id INTEGER NOT NULL,

    set_no INTEGER NOT NULL,

    reps_completed INTEGER,

    weight NUMERIC(7,2),

    rpe NUMERIC(3,1),

    rest_seconds INTEGER,

    completed_dt TIMESTAMPTZ,

    create_dt TIMESTAMPTZ NOT NULL
        DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_session_exercise_set
        FOREIGN KEY (workout_session_exercise_id)
        REFERENCES tracker.workout_session_exercise(id)
        ON DELETE CASCADE,

    CONSTRAINT uq_session_exercise_set
        UNIQUE (workout_session_exercise_id, set_no),

    CONSTRAINT chk_session_set_number
        CHECK (set_no > 0),

    CONSTRAINT chk_session_set_reps
        CHECK (
            reps_completed IS NULL
            OR reps_completed >= 0
        ),

    CONSTRAINT chk_session_set_weight
        CHECK (
            weight IS NULL
            OR weight >= 0
        ),

    CONSTRAINT chk_session_set_rpe
        CHECK (
            rpe IS NULL
            OR rpe BETWEEN 1 AND 10
        ),

    CONSTRAINT chk_session_set_rest
        CHECK (
            rest_seconds IS NULL
            OR rest_seconds >= 0
        )
);


-- ============================================
-- INDEXES
-- ============================================

-- Workout history per user
CREATE INDEX IF NOT EXISTS idx_workout_session_user_date
ON tracker.workout_session(user_id, start_dt DESC);


-- Sessions linked to planned workouts
CREATE INDEX IF NOT EXISTS idx_workout_session_workout
ON tracker.workout_session(workout_id);


-- Exercise performance history
CREATE INDEX IF NOT EXISTS idx_session_exercise_exercise
ON tracker.workout_session_exercise(exercise_id);


-- Optional planned exercise reference
CREATE INDEX IF NOT EXISTS idx_session_exercise_planned
ON tracker.workout_session_exercise(workout_exercise_id);
