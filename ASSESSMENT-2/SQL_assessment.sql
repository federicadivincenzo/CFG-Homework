USE OrdersInfo;

#	Write a SQL query to find the maximum order (purchase) amount for each customer. 
#	The customer ID should be in the range 3002 and 3007 (begin and end values are included.).
#	Filter the rows for maximum order (purchase) amount is higher than 1000. 
#	Return customer id and maximum purchase amount.


SELECT MAX(purch_amt), customer_id
FROM ORDERS
WHERE customer_id BETWEEN 3002 AND 3007
GROUP BY customer_id
HAVING MAX(purch_amt) > 1000;
