SQL - Introduction
 Novice
 By: Guillaume
 Weight: 1
 Your score will be updated as you progress.
 Project over - took place from Mar 8, 2025 12:00 AM to Mar 14, 2025 11:59 PM


Resources
Read or watch:

What is Database & SQL?
A Basic MySQL Tutorial
Basic SQL statements: DDL and DML (no need to read the chapter “Privileges”)
Basic queries: SQL and RA
SQL technique: functions
SQL technique: subqueries
What makes the big difference between a backtick and an apostrophe?
MySQL Cheat Sheet
MySQL 8.0 SQL Statement Syntax
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
What’s a database
What’s a relational database
What does SQL stand for
What’s MySQL
How to create a database in MySQL
What does DDL and DML stand for
How to CREATE or ALTER a table
How to SELECT data from a table
How to INSERT, UPDATE or DELETE data
What are subqueries
How to use MySQL functions
Requirements
General
Allowed editors: vi, vim, emacs
All your files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
All your files should end with a new line
All your SQL queries should have a comment just before (i.e. syntax above)
All your files should start by a comment describing the task
All SQL keywords should be in uppercase (SELECT, WHERE…)
A README.md file, at the root of the folder of the project, is mandatory
The length of your files will be tested using wc
More Info
Comments for your SQL file:
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
Install MySQL 8.0 on Ubuntu 20.04 LTS
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
Connect to your MySQL server:

$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$
Use the sandbox to run MySQL
In the container, credentials are root/root

Ask for container Ubuntu 20.04
Connect via SSH
OR connect via the Web terminal
In the container, you should start MySQL before playing with it:
$ service mysql start                                                   
 * Starting MySQL database server mysqld 
$
$ cat 0-list_databases.sql | mysql -uroot -p                               
Database                                                                                   
information_schema                                                                         
mysql                                                                                      
performance_schema                                                                         
sys                      
$
In the container, credentials are root/root

