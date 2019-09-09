DROP TABLE IF EXISTS events_dim;
DROP TABLE IF EXISTS sessions_dim;
DROP TABLE IF EXISTS verifiers_dim;
DROP TABLE IF EXISTS countries_dim;


CREATE TABLE IF NOT EXISTS countries_dim (
    uuid VARCHAR PRIMARY KEY,
    country VARCHAR NOT NULL
);

CREATE TABLE IF NOT EXISTS verifiers_dim (
    uuid VARCHAR PRIMARY KEY,
    verifier_name VARCHAR NOT NULL
);

CREATE TABLE IF NOT EXISTS sessions_dim (
    uuid VARCHAR PRIMARY KEY,
    status VARCHAR NOT NULL,
    verifier_uuid VARCHAR NOT NULL,
    country_uuid VARCHAR NOT NULL
);

CREATE TABLE IF NOT EXISTS events_dim (
    uuid VARCHAR PRIMARY KEY,
    session_uuid VARCHAR NOT NULL,
    event_type VARCHAR NOT NULL,
    created_at TIMESTAMP NOT NULL
);

CREATE TABLE IF NOT EXISTS time_temp (
    session_uuid VARCHAR NOT NULL, 
    time_interval VARCHAR NOT NULL
);

CREATE TABLE IF NOT EXISTS time_fact (
    country_uuid VARCHAR NOT NULL,
    verifier_uuid VARCHAR NOT NULL,
    session_uuid VARCHAR NOT NULL,
    events_uuid VARCHAR NOT NULL,
	time_interval VARCHAR NOT NULL, 
    FOREIGN KEY (verifier_uuid) REFERENCES verifiers_dim (uuid),
    FOREIGN KEY (country_uuid) REFERENCES countries_dim (uuid),
    FOREIGN KEY (session_uuid) REFERENCES sessions_dim (uuid),
    FOREIGN KEY (events_uuid) REFERENCES events_dim (uuid)
);
