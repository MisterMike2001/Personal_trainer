
-- ============================================
-- CREATE PROFILE SCHEMA
-- ============================================

CREATE SCHEMA IF NOT EXISTS profile;


-- ============================================
-- 1. USER PROFILE
-- ============================================

CREATE TABLE IF NOT EXISTS profile.user_profile (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    user_id INTEGER NOT NULL UNIQUE,

    gender VARCHAR(30),
    date_of_birth DATE,
    height NUMERIC(5,2) NOT NULL,

    create_dt TIMESTAMPTZ NOT NULL
        DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_user_profile_user
        FOREIGN KEY (user_id)
        REFERENCES auth.users(id)
        ON DELETE CASCADE,

    CONSTRAINT chk_profile_height
        CHECK (height > 0)
);


-- ============================================
-- 2. USER WEIGHT HISTORY
-- ============================================

CREATE TABLE IF NOT EXISTS profile.user_weight (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    user_id INTEGER NOT NULL,

    weight NUMERIC(6,2) NOT NULL,

    recorded_dt TIMESTAMPTZ NOT NULL
        DEFAULT CURRENT_TIMESTAMP,

    create_dt TIMESTAMPTZ NOT NULL
        DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_user_weight_user
        FOREIGN KEY (user_id)
        REFERENCES auth.users(id)
        ON DELETE CASCADE,

    CONSTRAINT chk_user_weight
        CHECK (weight > 0)
);


-- ============================================
-- 3. USER MEASUREMENT HISTORY
-- ============================================

CREATE TABLE IF NOT EXISTS profile.user_measurements (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    user_id INTEGER NOT NULL,

    chest NUMERIC(6,2),
    waist NUMERIC(6,2),
    hips NUMERIC(6,2),
    shoulders NUMERIC(6,2),
    arms NUMERIC(6,2),
    thighs NUMERIC(6,2),
    calves NUMERIC(6,2),

    recorded_dt TIMESTAMPTZ NOT NULL
        DEFAULT CURRENT_TIMESTAMP,

    create_dt TIMESTAMPTZ NOT NULL
        DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_user_measurements_user
        FOREIGN KEY (user_id)
        REFERENCES auth.users(id)
        ON DELETE CASCADE,

    CONSTRAINT chk_measurements_positive
        CHECK (
            (chest IS NULL OR chest > 0)
            AND (waist IS NULL OR waist > 0)
            AND (hips IS NULL OR hips > 0)
            AND (shoulders IS NULL OR shoulders > 0)
            AND (arms IS NULL OR arms > 0)
            AND (thighs IS NULL OR thighs > 0)
            AND (calves IS NULL OR calves > 0)
        )
);


-- ============================================
-- 4. PROGRESS PHOTOS
-- ============================================

CREATE TABLE IF NOT EXISTS profile.progress_photos (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    user_id INTEGER NOT NULL,

    front TEXT,
    back TEXT,
    left_side TEXT,
    right_side TEXT,

    recorded_dt TIMESTAMPTZ NOT NULL
        DEFAULT CURRENT_TIMESTAMP,

    create_dt TIMESTAMPTZ NOT NULL
        DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_progress_photos_user
        FOREIGN KEY (user_id)
        REFERENCES auth.users(id)
        ON DELETE CASCADE
);


-- ============================================
-- INDEXES FOR HISTORICAL REPORTING
-- ============================================

CREATE INDEX IF NOT EXISTS idx_user_weight_history
ON profile.user_weight (
    user_id,
    recorded_dt DESC
);

CREATE INDEX IF NOT EXISTS idx_user_measurements_history
ON profile.user_measurements (
    user_id,
    recorded_dt DESC
);

CREATE INDEX IF NOT EXISTS idx_progress_photos_history
ON profile.progress_photos (
    user_id,
    recorded_dt DESC
);
