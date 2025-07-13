-- Create users table
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(100) NOT NULL
);

-- Insert sample users
INSERT INTO users (username, password) VALUES
('alice', 'wonderland'),
('bob', 'secure456'),
('admin', 'adminpass');

-- Create hardware table
CREATE TABLE IF NOT EXISTS hardware (
    id VARCHAR(20) PRIMARY KEY,
    type VARCHAR(50),
    ram VARCHAR(20),
    cpu VARCHAR(50),
    storage VARCHAR(50)
);

-- Insert sample hardware data
INSERT INTO hardware (id, type, ram, cpu, storage) VALUES
('HW101', 'Laptop', '16GB', 'Intel i7', '512GB SSD'),
('HW102', 'Desktop', '32GB', 'AMD Ryzen 7', '1TB HDD'),
('HW103', 'Server', '64GB', 'Intel Xeon', '2TB SSD');