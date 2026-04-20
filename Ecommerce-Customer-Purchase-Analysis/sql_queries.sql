CREATE DATABASE E_COMMERCE_DB;
USE E_COMMERCE_DB;

CREATE TABLE PURCHASES (
customer_id INT, customer_name VARCHAR(50), city VARCHAR(50), product VARCHAR(50), Brand VARCHAR(50), quantity INT, price INT);

SELECT * FROM purchases;

SELECT customer_name,
       SUM(quantity * price) AS total_spent
FROM purchases
GROUP BY customer_name
ORDER BY total_spent DESC;

SELECT product,
       SUM(quantity) AS total_quantity
FROM purchases
GROUP BY product
ORDER BY total_quantity DESC;

SELECT city,
       SUM(quantity * price) AS revenue
FROM purchases
GROUP BY city
ORDER BY revenue DESC;

SELECT brand,
       SUM(quantity * price) AS brand_revenue
FROM purchases
GROUP BY brand
ORDER BY brand_revenue DESC;
SELECT COUNT(*) FROM purchases;