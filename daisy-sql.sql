-- Create database (if it doesn't exist)
CREATE DATABASE IF NOT EXISTS daisy;

-- Use the database
USE daisy;

-- Create table 'entry' for storing mood journal entries
CREATE TABLE IF NOT EXISTS entry (
    entry_id INT AUTO_INCREMENT PRIMARY KEY,
    emotion VARCHAR(255) NOT NULL,
    tol_score INT NOT NULL,
    reaction TEXT,
    date_added DATETIME DEFAULT CURRENT_TIMESTAMP
);