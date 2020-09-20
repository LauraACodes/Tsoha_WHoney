CREATE TABLE producers (
    producer_id SERIAL PRIMARY KEY, 
    name VARCHAR(100)
);
CREATE TABLE queens (
    queen_id SERIAL PRIMARY KEY, 
    producer_id INTEGER REFERENCES producers,
    date DATE NOT NULL, 
    name VARCHAR (20) NOT NULL, 
    alive SMALLINT DEFAULT 1
);
CREATE TABLE hives (
    hive_id SERIAL PRIMARY KEY, 
    queen_id INTEGER REFERENCES queens,
    producer_id INTEGER REFERENCES producers,
    date DATE NOT NULL, 
    name VARCHAR (20) NOT NULL, 
    alive SMALLINT DEFAULT 1
); 
CREATE TABLE carelist (
    care_id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);
CREATE TABLE hivecare (
    hivecare_id SERIAL PRIMARY KEY,
    hive_id INTEGER REFERENCES hives,
    care_id INTEGER REFERENCES carelist,
    date DATE NOT NULL
);
CREATE TABLE checkup (
    checkup_id SERIAL PRIMARY KEY,
    hive_id INTEGER REFERENCES hives,
    date DATE NOT NULL,
    allok SMALLINT DEFAULT 1,
    explain VARCHAR(200)
);