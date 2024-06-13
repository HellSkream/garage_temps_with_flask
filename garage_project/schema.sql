DROP TABLE IF EXISTS garage_temps;

CREATE TABLE garage_temps (
    log_time TIMESTAMP PRIMARY KEY,
    cpu_temp REAL NOT NULL,
    garage_temp REAL NOT NULL,
    perth_temp REAL NOT NULL,
    weath_desc TEXT NOT NULL,
    weath_time TIMESTAMP NOT NULL
);

DROP TABLE IF EXISTS weath_desc;

CREATE TABLE weath_desc (
    weath_desc TEXT PRIMARY KEY,
    weath_code TEXT NOT NULL
);

