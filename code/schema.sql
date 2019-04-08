-- Create and use customer_db
CREATE DATABASE nfl_db;
USE nfl_db;

CREATE TABLE team (
    id INT AUTO_INCREMENT NOT NULL,
    Team VARCHAR(150),
    Tm VARCHAR(100),
    W INT(11),
    L INT(11),
    T INT(11),
    rate VARCHAR(100),
    PF INT(11),
    PA INT(11),
    PD INT(11),
    PRIMARY KEY (id)
);