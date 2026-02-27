CREATE DATABASE superstore_db;

\c superstore_db;

CREATE TABLE public_orders (
    order_id VARCHAR(50),
    order_date DATE,
    ship_date DATE,
    ship_mode VARCHAR(50),
    customer_name VARCHAR(100),
    segment VARCHAR(50),
    state VARCHAR(100),
    country VARCHAR(100),
    market VARCHAR(100),
    region VARCHAR(100),
    product_id VARCHAR(50),
    category VARCHAR(100),
    sub_category VARCHAR(100),
    product_name TEXT,
    sales NUMERIC(12,2),
    quantity INT,
    discount NUMERIC(5,2),
    profit NUMERIC(12,2),
    shipping_cost NUMERIC(12,2),
    order_priority VARCHAR(50),
    year INT,
    month INT,
    month_name VARCHAR(20),
    delivery_days INT,
    profit_margin NUMERIC(10,6)
);

COPY public_orders
FROM 'C:/superstore_db/SuperStore_Cleaned.csv'
WITH (
    FORMAT csv,
    HEADER true,
    DELIMITER ',',
    QUOTE '"'
);
