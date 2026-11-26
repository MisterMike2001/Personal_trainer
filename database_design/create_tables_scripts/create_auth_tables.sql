
-- ============================================
-- CREATE AUTH SCHEMA
-- ============================================

CREATE SCHEMA IF NOT EXISTS auth;


-- ============================================
-- USERS TABLE
-- ============================================

CREATE TABLE IF NOT EXISTS auth.users (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    name VARCHAR(100) NOT NULL,
    surname VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    cell VARCHAR(20) NOT NULL,
    password TEXT NOT NULL,

    is_admin BOOLEAN NOT NULL DEFAULT FALSE,

    create_dt TIMESTAMPTZ NOT NULL
        DEFAULT CURRENT_TIMESTAMP
);


-- ============================================
-- REFRESH SESSION TABLE
-- ============================================

CREATE TABLE IF NOT EXISTS auth.refresh_session (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    user_id INTEGER NOT NULL,

    token_hash TEXT NOT NULL UNIQUE,
    expires_at TIMESTAMPTZ NOT NULL,
    revoked_at TIMESTAMPTZ,

    CONSTRAINT fk_refresh_session_user
        FOREIGN KEY (user_id)
        REFERENCES auth.users(id)
        ON DELETE CASCADE
);


-- ============================================
-- INDEXES
-- ============================================

CREATE INDEX IF NOT EXISTS idx_refresh_session_user_id
ON auth.refresh_session(user_id);

CREATE INDEX IF NOT EXISTS idx_refresh_session_expires_at
ON auth.refresh_session(expires_at);
