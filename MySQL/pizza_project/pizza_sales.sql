USE pizza_db;
SELECT * FROM pizza_sales;
DROP VIEW `average order value`;
RENAME TABLE `average order value division`TO `average order value`;
SELECT * FROM `average pizzas / order`;

CREATE VIEW `total orders` AS
SELECT COUNT(DISTINCT order_id) AS `total orders`
FROM pizza_sales;


CREATE VIEW `average pizzas / order` AS
SELECT SUM(quantity) / COUNT(DISTINCT order_id) AS `average pizzas / order`
FROM pizza_sales;
-- DAILY TREND OF SALES ----------

CREATE VIEW `daily trend for total orders` AS
SELECT DAYNAME(STR_TO_DATE(order_date, '%d-%m-%Y')) AS `Day`, COUNT(DISTINCT order_id) AS `total orders`
FROM pizza_sales
GROUP BY `Day`
ORDER BY `total orders`;

-- HOURLY TREND---
 
CREATE VIEW `Hourly trend for pizza sales` AS
SELECT HOUR(order_time) AS `Hour`, COUNT(DISTINCT order_id) AS `Total orders`
FROM pizza_sales
GROUP BY `Hour`
ORDER BY `Total orders` DESC;

-- PERCENTAGE OF SALES BY CATEGORY--

CREATE VIEW `Percentage of sales by category` AS
SELECT DISTINCT pizza_category, ROUND(SUM(total_price) * 100 / (
						SELECT SUM(total_price) FROM pizza_sales),2)
AS `% Of sales`
FROM pizza_sales
GROUP BY pizza_category
ORDER BY `% Of sales`;

-- PERCENTAGE OF SALES BY SIZE --

CREATE VIEW `percentage of sales by size` AS
SELECT DISTINCT pizza_size, ROUND(SUM(total_price) * 100 / (
							SELECT SUM(total_price) FROM
                            pizza_sales),2) 
AS `% of sales`
FROM pizza_sales
GROUP BY pizza_size
ORDER BY `% of sales`;

-- TOP 5 BEST PIZZAS BY QUANTITY SOLD --

CREATE VIEW `Top 5 best pizzas by quantity` AS
SELECT DISTINCT pizza_name, SUM(quantity) AS `Total pizzas sold`
FROM pizza_sales
GROUP BY pizza_name
ORDER BY `Total pizzas sold` DESC
LIMIT 5;

-- BOTTOM 5 PIZZAS BY QUANTITY SOLD --

CREATE VIEW `Bottom 5 best pizzas by quantity` AS
SELECT DISTINCT pizza_name, SUM(quantity) AS `Total pizzas sold`
FROM pizza_sales
GROUP BY pizza_name
ORDER BY `Total pizzas sold`
LIMIT 5;

SELECT * FROM `bottom 5 best pizzas by quantity`;


