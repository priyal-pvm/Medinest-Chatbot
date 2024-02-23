CREATE DATABASE  IF NOT EXISTS `hospitalapt`;
use `hospitalapt`;


create table `apt`(
    `pid` INT NOT NULL,
    `name` varchar(50) NOT NULL,
    `age` VARCHAR(20) NOT NULL,
    `doctor` varchar(50) not null,
    `gender` varchar(20) not null,
    `date` DATETIME not NULL, primary key(`pid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

LOCK TABLES `apt` WRITE;

insert into `apt` values (1,'Arpita Roy',21,'Dr Tanaya','Female','2024-03-10T12:00:00+05:30'),(2,'Priya Patel', 30, 'Dr. Gupta', 'Female', '2024-05-15T14:30:00+05:30');

UNLOCK TABLES;


create table `report`(
    `pid` INT NOT NULL,
    `rid` int not null,
    `name` varchar(50) NOT NULL,
    `doctor` varchar(50) not null,
    `disease` varchar(80) not null,
    `type` varchar(80) not null,
    `date` DATETIME not NULL, primary key(`pid`,`rid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

LOCK TABLES `report` WRITE;

INSERT INTO `report` (`pid`, `rid`, `name`, `doctor`, `disease`, `type`, `date`)
VALUES
    (1, 101, 'Arpita Roy', 'Dr. Tanaya', 'Fever', 'Lab Report', '2024-03-10 12:00:00'),
    (2, 102, 'Rahul Sharma', 'Dr. Gupta', 'Diabetes', 'Health Checkup', '2024-03-11 14:30:00'),
    (3, 103, 'Ananya Das', 'Dr. Reddy', 'Hypertension', 'Cardiology', '2024-03-12 10:15:00');

UNLOCK TABLES;
