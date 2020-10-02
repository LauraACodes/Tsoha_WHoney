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
    alive SMALLINT DEFAULT 1,
    boxes SMALLINT DEFAULT 2
); 
CREATE TABLE carelist (
    care_id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);
CREATE TABLE diseacelist(
    diseace_id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);
CREATE TABLE hivecare (
    hivecare_id SERIAL PRIMARY KEY,
    hive_id INTEGER REFERENCES hives,
    care_id INTEGER REFERENCES carelist,
    date DATE NOT NULL
);
CREATE TABLE checkup (
    checkup_id SERIAL PRIMARY KEY,
    hivecare_id INTEGER REFERENCES hivecare,
    hive_id INTEGER REFERENCES hives,
    date DATE NOT NULL,
    allok SMALLINT DEFAULT 1,
    explain VARCHAR(200)
);
CREATE TABLE diseacecont(
    diseacecont_id SERIAL PRIMARY KEY,
    hive_id INTEGER REFERENCES hives,
    hivecare_id INTEGER REFERENCES hivecare,
    diseace_id INTEGER REFERENCES diseacelist,
    date DATE NOT NULL
);
CREATE TABLE sugar(
    sugar_id SERIAL PRIMARY KEY,
    hive_id INTEGER REFERENCES hives,
    hivecare_id INTEGER REFERENCES hivecare,
    date DATE NOT NULL,
    kg SMALLINT
);
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY, 
    username TEXT, 
    password TEXT
);