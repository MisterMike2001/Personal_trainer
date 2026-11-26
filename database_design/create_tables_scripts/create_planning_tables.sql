
-- ============================================
-- CREATE PLANNING SCHEMA
-- ============================================

CREATE SCHEMA IF NOT EXISTS planning;


-- ============================================
-- 1. EQUIPMENT
-- ============================================

CREATE TABLE IF NOT EXISTS planning.equipment (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    image TEXT,

    is_active BOOLEAN NOT NULL DEFAULT TRUE
);


-- ============================================
-- 2. MUSCLE GROUPS
-- ============================================

CREATE TABLE IF NOT EXISTS planning.muscle_groups (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT
);


-- ============================================
-- 3. EXERCISES
-- ============================================

CREATE TABLE IF NOT EXISTS planning.exercises (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    name VARCHAR(150) NOT NULL,
    description TEXT,

    motion_image_1 TEXT,
    motion_image_2 TEXT,

    equipment_id INTEGER,

    is_active BOOLEAN NOT NULL DEFAULT TRUE,

    CONSTRAINT fk_exercises_equipment
        FOREIGN KEY (equipment_id)
        REFERENCES planning.equipment(id)
        ON DELETE SET NULL
);


-- ============================================
-- 4. EXERCISE MUSCLE GROUPS
-- ============================================

CREATE TABLE IF NOT EXISTS planning.exercise_muscle_groups (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    exercise_id INTEGER NOT NULL,
    muscle_group_id INTEGER NOT NULL,

    create_dt TIMESTAMPTZ NOT NULL
        DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_exercise_muscle_exercise
        FOREIGN KEY (exercise_id)
        REFERENCES planning.exercises(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_exercise_muscle_group
        FOREIGN KEY (muscle_group_id)
        REFERENCES planning.muscle_groups(id)
        ON DELETE CASCADE,

    CONSTRAINT uq_exercise_muscle_group
        UNIQUE (exercise_id, muscle_group_id)
);


-- ============================================
-- 5. WORKOUT PLAN
-- ============================================

CREATE TABLE IF NOT EXISTS planning.workout_plan (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    user_id INTEGER NOT NULL,

    name VARCHAR(150) NOT NULL,
    description TEXT,

    cycle_length_days INTEGER NOT NULL,

    is_active BOOLEAN NOT NULL DEFAULT TRUE,

    create_dt TIMESTAMPTZ NOT NULL
        DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_workout_plan_user
        FOREIGN KEY (user_id)
        REFERENCES auth.users(id)
        ON DELETE CASCADE,

    CONSTRAINT chk_workout_plan_cycle
        CHECK (cycle_length_days > 0)
);


-- ============================================
-- 6. WORKOUT
-- ============================================

CREATE TABLE IF NOT EXISTS planning.workout (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    workout_plan_id INTEGER NOT NULL,

    name VARCHAR(150) NOT NULL,

    order_no INTEGER NOT NULL,
    cycle_day INTEGER,

    is_active BOOLEAN NOT NULL DEFAULT TRUE,

    create_dt TIMESTAMPTZ NOT NULL
        DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_workout_plan
        FOREIGN KEY (workout_plan_id)
        REFERENCES planning.workout_plan(id)
        ON DELETE CASCADE,

    CONSTRAINT chk_workout_order
        CHECK (order_no > 0),

    CONSTRAINT chk_workout_cycle_day
        CHECK (cycle_day IS NULL OR cycle_day > 0),

    CONSTRAINT uq_workout_plan_order
        UNIQUE (workout_plan_id, order_no)
);


-- ============================================
-- 7. WORKOUT MUSCLE GROUPS
-- ============================================

CREATE TABLE IF NOT EXISTS planning.workout_muscle_groups (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    workout_id INTEGER NOT NULL,
    muscle_group_id INTEGER NOT NULL,

    create_dt TIMESTAMPTZ NOT NULL
        DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_workout_muscle_workout
        FOREIGN KEY (workout_id)
        REFERENCES planning.workout(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_workout_muscle_group
        FOREIGN KEY (muscle_group_id)
        REFERENCES planning.muscle_groups(id)
        ON DELETE CASCADE,

    CONSTRAINT uq_workout_muscle_group
        UNIQUE (workout_id, muscle_group_id)
);


-- ============================================
-- 8. WORKOUT EXERCISES
-- ============================================

CREATE TABLE IF NOT EXISTS planning.workout_exercise (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    workout_id INTEGER NOT NULL,
    exercise_id INTEGER NOT NULL,

    exercise_order INTEGER NOT NULL,

    create_dt TIMESTAMPTZ NOT NULL
        DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_workout_exercise_workout
        FOREIGN KEY (workout_id)
        REFERENCES planning.workout(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_workout_exercise_exercise
        FOREIGN KEY (exercise_id)
        REFERENCES planning.exercises(id),

    CONSTRAINT chk_exercise_order
        CHECK (exercise_order > 0),

    CONSTRAINT uq_workout_exercise_order
        UNIQUE (workout_id, exercise_order)
);


-- ============================================
-- 9. WORKOUT EXERCISE SETS
-- ============================================

CREATE TABLE IF NOT EXISTS planning.workout_exercise_set (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    workout_exercise_id INTEGER NOT NULL,

    set_no INTEGER NOT NULL,

    target_reps_min INTEGER,
    target_reps_max INTEGER,

    target_weight NUMERIC(7,2),

    rest_seconds INTEGER,

    set_type VARCHAR(30) NOT NULL DEFAULT 'working',

    create_dt TIMESTAMPTZ NOT NULL
        DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_workout_exercise_set
        FOREIGN KEY (workout_exercise_id)
        REFERENCES planning.workout_exercise(id)
        ON DELETE CASCADE,

    CONSTRAINT uq_workout_exercise_set
        UNIQUE (workout_exercise_id, set_no),

    CONSTRAINT chk_set_number
        CHECK (set_no > 0),

    CONSTRAINT chk_target_reps
        CHECK (
            (target_reps_min IS NULL OR target_reps_min > 0)
            AND
            (target_reps_max IS NULL OR target_reps_max > 0)
            AND
            (
                target_reps_min IS NULL
                OR target_reps_max IS NULL
                OR target_reps_min <= target_reps_max
            )
        ),

    CONSTRAINT chk_target_weight
        CHECK (target_weight IS NULL OR target_weight >= 0),

    CONSTRAINT chk_rest_seconds
        CHECK (rest_seconds IS NULL OR rest_seconds >= 0)
);


-- ============================================
-- INDEXES
-- ============================================

CREATE INDEX IF NOT EXISTS idx_exercises_equipment
ON planning.exercises(equipment_id);

CREATE INDEX IF NOT EXISTS idx_exercise_muscle_group
ON planning.exercise_muscle_groups(muscle_group_id);

CREATE INDEX IF NOT EXISTS idx_workout_plan_user
ON planning.workout_plan(user_id);

CREATE INDEX IF NOT EXISTS idx_workout_muscle_group
ON planning.workout_muscle_groups(muscle_group_id);

CREATE INDEX IF NOT EXISTS idx_workout_exercise_id
ON planning.workout_exercise(exercise_id);
