CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);

INSERT INTO users (name) VALUES ('John Doe'), ('Jane Doe');