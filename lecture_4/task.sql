-- Create table students
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    birth_year INTEGER NOT NULL
);

-- Create table grades
CREATE TABLE grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    subject TEXT NOT NULL,
    grade INTEGER CHECK (grade >= 1 AND grade <= 100),
    FOREIGN KEY (student_id) REFERENCES students(id)
);

-- Insert data to students
INSERT INTO students (full_name, birth_year) VALUES
('Alice Johnson', 2005),
('Brian Smith', 2004),
('Carla Reyes', 2006),
('Daniel Kim', 2005),
('Eva Thompson', 2003),
('Felix Nguyen', 2007),
('Grace Patel', 2005),
('Henry Lopez', 2004),
('Isabella Martinez', 2006);

-- Insert data to grades
INSERT INTO grades (student_id, subject, grade) VALUES
(1, 'Math', 88),
(1, 'English', 92),
(1, 'Science', 85),
(2, 'Math', 75),
(2, 'History', 83),
(2, 'English', 79),
(3, 'Science', 95),
(3, 'Math', 91),
(3, 'Art', 89),
(4, 'Math', 84),
(4, 'Science', 88),
(4, 'Physical Education', 93),
(5, 'English', 90),
(5, 'History', 85),
(5, 'Math', 88),
(6, 'Science', 72),
(6, 'Math', 78),
(6, 'English', 81),
(7, 'Art', 94),
(7, 'Science', 87),  
(7, 'Math', 90),  
(8, 'History', 77),  
(8, 'Math', 83),  
(8, 'Science', 80),  
(9, 'English', 96),  
(9, 'Math', 89),  
(9, 'Art', 92);


-- All grades for Alice Johnson
SELECT subject, grade FROM grades
WHERE student_id = 1;

-- Average grade per student
SELECT s.full_name as name, ROUND(AVG(g.grade),1) as "average grade" FROM grades g
JOIN students s on s.id = g.student_id
GROUP BY s.id, s.full_name;

-- Students born after 2004 
SELECT full_name FROM students
where birth_year > 2004;
 
-- Average grade per subject
SELECT subject, ROUND(AVG(grade),1) as "average grade" FROM grades
GROUP BY subject;

-- Top 3 students
SELECT s.full_name as name, ROUND(AVG(g.grade),1) as average_grade FROM grades g
JOIN students s on s.id = g.student_id
GROUP BY s.id, s.full_name
ORDER BY average_grade DESC
LIMIT 3;

-- Students with a score below 80 in any subject
SELECT DISTINCT s.full_name as name  FROM grades g
JOIN students s on s.id = g.student_id
WHERE g.grade < 80