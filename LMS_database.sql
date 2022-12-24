'''#NAME_OF_DATASEFILE_SHOULD_BE_"School_portal.sql"'''

mysql> create database school_portal;
Query OK, 1 row affected (0.10 sec)
mysql> create table assignments(
-> Subject varchar ( 20 ),
-> Chapter varchar ( 20 ),
-> Topic varchar ( 40 ),
-> Link varchar ( 100 ),
-> LastDate date )
-> assign_id int (10) PRIMARY KEY;
Query OK, 0 rows affected (0.17 sec)
mysql> create table attendance(
-> Student varchar ( 20 ),
-> NoOfDaysPresent int ( 11 )
-> );
Query OK, 0 rows affected (0.06 sec)
mysql> create table chemistry(
-> Chapter varchar ( 20 ),
-> ClassNumber int ( 11 ),
-> Notes varchar ( 70 ),
-> Recording varchar ( 70 )
-> );
Query OK, 0 rows affected (0.14 sec)
mysql> create table cs(
-> Chapter varchar ( 20 ),
48
-> ClassNumber int ( 11 ),
-> Notes varchar ( 70 ),
-> Recording varchar ( 70 )
-> );
Query OK, 0 rows affected (0.14 sec)
mysql> create table maths(
-> Chapter varchar ( 20 ),
-> ClassNumber int ( 11 ),
-> Notes varchar ( 70 ),
-> Recording varchar ( 70 )
-> );
Query OK, 0 rows affected (0.14 sec)
mysql> create table physics(
-> Chapter varchar ( 20 ),
-> ClassNumber int ( 11 ),
-> Notes varchar ( 70 ),
-> Recording varchar ( 70 )
-> );
Query OK, 0 rows affected (0.14 sec)
mysql> create table liveclasslink(
-> Link varchar ( 60 )
-> );
Query OK, 0 rows affected (0.11 sec)
mysql> create table students(
-> Name varchar ( 20 ),
-> Pin int ( 4 ),
-> RegistrationNo int ( 7 ) PRIMARY KEY,
-> DOB date ,
49
-> ContactNo bigint ( 10 ),
-> Grade int ( 2 ),
-> Section char ( 1 ),
-> emailID varchar ( 40 )
-> );
Query OK, 0 rows affected (0.14 sec)
mysql> create table teachers(
-> Name varchar ( 20 ),
-> Pin int ( 4 ),
-> Subject varchar ( 10 ),
-> RegistrationNo int ( 7 ) PRIMARY KEY,
-> DOB date ,
-> ContactNo bigint ( 10 ),
-> emailID varchar ( 40 )
-> );
Query OK, 0 rows affecte
mysql> create table assig_submit(
-> idno int(10),
-> student_name varchar ( 100 ),
-> reg_no int (30) ,
-> assign_id int(10),
-> link varchar(256),
->UPLOAD int ;
Query OK, 0 rows affected (0.17 sec)
