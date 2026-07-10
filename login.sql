CREATE DATABASE login;

USE login;

CREATE TABLE login (
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL
);