CREATE DATABASE tweetanalyzer;
use tweetanalyzer;

CREATE TABLE test_table (
    name        VARCHAR(20),
    description VARCHAR(128)
);

INSERT INTO test_table (name, description) VALUES 
    ('test1', 'This is a test description'),
    ('test2', 'This is another test description');
