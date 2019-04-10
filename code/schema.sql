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

CREATE TABLE player_salary (
    rank INT AUTO_INCREMENT NOT NULL,
    First_name VARCHAR(50),
    Last_name VARCHAR(50),
    Team VARCHAR(150),
    Salary VARCHAR(50),
    PRIMARY KEY (rank)
);

CREATE TABLE player_game_data (
    rank INT AUTO_INCREMENT NOT NULL,
    First_name VARCHAR(50),
    Last_name VARCHAR(50),
    Team VARCHAR(150),
    G INT(11),
    GS INT(11),
    PRIMARY KEY (rank)
);

CREATE TABLE player_passing_data (
    rank INT AUTO_INCREMENT NOT NULL,
    First_name VARCHAR(50),
    Last_name VARCHAR(50),
    Team VARCHAR(150),
    Cmp INT(11),
    Att INT(11),
    Yds INT(11),
    TD INT(11),
    IT INT(11),
    PRIMARY KEY (rank)
);

CREATE TABLE player_rushing_data (
    rank INT AUTO_INCREMENT NOT NULL,
    First_name VARCHAR(50),
    Last_name VARCHAR(50),
    Team VARCHAR(150),
    Att INT,
    Yds INT,
    YA_rate INT,
    TD INT,
    PRIMARY KEY (rank)
);


CREATE TABLE player_fumbles_data (
    rank INT AUTO_INCREMENT NOT NULL,
    First_name VARCHAR(50),
    Last_name VARCHAR(50),
    Team VARCHAR(150),
    Fmb INT,
    Fl INT,
    PRIMARY KEY (rank)
);


CREATE TABLE player_scoring_data (
    rank INT AUTO_INCREMENT NOT NULL,
    First_name VARCHAR(50),
    Last_name VARCHAR(50),
    Team VARCHAR(150),
    TD INT,
    2PM INT,
    PRIMARY KEY (rank)
);

CREATE TABLE player_info (
   rank INT AUTO_INCREMENT NOT NULL,
   First_name VARCHAR(50),
   Last_name VARCHAR(50),
   Team VARCHAR(50),
   Age INT(11),
   PRIMARY KEY (rank)
);

CREATE TABLE player_receiving_data (
    rank INT AUTO_INCREMENT NOT NULL,
    First_name VARCHAR(50),
    Last_name VARCHAR(50),
    Team VARCHAR(150),
    TGT INT,
    REC INT,
    YDS INT,
    YR_rate INT,
    PRIMARY KEY (rank)
);
