-- users table
CREATE TABLE IF NOT EXISTS users (
    user_id INT PRIMARY KEY,
    name TEXT,
    email TEXT,
    created_at TIMESTAMP
);

-- orders table
CREATE TABLE IF NOT EXISTS orders (
    order_id INT PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
    product TEXT,
    amount DECIMAL,
    created_at TIMESTAMP,
    shipped_at TIMESTAMP,
    delivered_at TIMESTAMP,
    returned_at TIMESTAMP
);
