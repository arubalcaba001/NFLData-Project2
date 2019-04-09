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

CREATE TABLE Players (
    player_id INT AUTO_INCREMENT NOT NULL,
    First_name VARCHAR(50),
    Last_name VARCHAR(50),
    Team VARCHAR(150),
    Age INT,
    Salary INT,
    PRIMARY KEY (player_id)
);

CREATE TABLE player_game_data (
    player_id INT AUTO_INCREMENT NOT NULL,
    First_name VARCHAR(50),
    Last_name VARCHAR(50),
    Team VARCHAR(150),
    G INT,
    GS INT,
    PRIMARY KEY (player_id)
);

CREATE TABLE player_passing_data (
    player_id INT AUTO_INCREMENT NOT NULL,
    First_name VARCHAR(50),
    Last_name VARCHAR(50),
    Team VARCHAR(150),
    Cmp INT,
    Att INT,
    Yds INT,
    TD INT,
    PRIMARY KEY (player_id)
);

CREATE TABLE player_rushing_data (
    player_id INT AUTO_INCREMENT NOT NULL,
    First_name VARCHAR(50),
    Last_name VARCHAR(50),
    Team VARCHAR(150),
    Att INT,
    Yds INT,
    Y/A INT,
    TD INT,
    PRIMARY KEY (player_id)
);


CREATE TABLE player_fumbles_data (
    player_id INT AUTO_INCREMENT NOT NULL,
    First_name VARCHAR(50),
    Last_name VARCHAR(50),
    Team VARCHAR(150),
    Fmb INT,
    Fl INT,
    PRIMARY KEY (player_id)
);


CREATE TABLE player_scoring_data (
    player_id INT AUTO_INCREMENT NOT NULL,
    First_name VARCHAR(50),
    Last_name VARCHAR(50),
    Team VARCHAR(150),
    TD INT,
    2PM INT,
    PRIMARY KEY (player_id)
);
