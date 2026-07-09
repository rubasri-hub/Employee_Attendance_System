CREATE DATABASE employee_attendance;

USE employee_attendance;

CREATE TABLE employee (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(100),
    department VARCHAR(50),
    designation VARCHAR(50)
);

CREATE TABLE attendance (
    attendance_id INT AUTO_INCREMENT PRIMARY KEY,
    emp_id INT,
    attendance_date DATE,
    status VARCHAR(10),
    FOREIGN KEY (emp_id) REFERENCES employee(emp_id)
);

INSERT INTO employee VALUES
(101, 'Rahul', 'HR', 'Manager'),
(102, 'Priya', 'IT', 'Developer'),
(103, 'Arun', 'Finance', 'Accountant'),
(104, 'Divya', 'Sales', 'Executive'),
(105, 'Karthik', 'Marketing', 'Analyst');

SELECT * FROM employee;