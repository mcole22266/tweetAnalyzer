CREATE DATABASE testdb;
use testdb;

CREATE TABLE test_table (
    name        VARCHAR(20),
    description VARCHAR(128)
);

INSERT INTO test_table (name, description) VALUES 
    ('test1', 'This is a test description'),
    ('test2', 'This is another test description');

CREATE TABLE 2test_2table (
    name        VARCHAR(20),
    description VARCHAR(128)
);

INSERT INTO 2test_2table (name, description) VALUES 
    ('test1', 'This is a test description'),
    ('test2', 'This is another test description');
