-- SQL-команды для создания таблиц

CREATE TABLE employees
(
    post_id int PRIMARY KEY,
    title varchar(100) NOT NULL,
    content text
);

CREATE TABLE customers
(
    post_id int PRIMARY KEY,
    title varchar(100) NOT NULL,
    content text
);

CREATE TABLE orders
(
    post_id int PRIMARY KEY,
    title varchar(100) NOT NULL,
    content text
);
