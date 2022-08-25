USE SqlAssignment;

--1.Display snum,sname,city and comm of all salespeople.
SELECT Snum, Snum, City, Comm
FROM SalesPeople;
GO

--2.Display all snum without duplicates from all orders.
SELECT DISTINCT Snum
FROM Orders;
GO

--3.Display names and commissions of all salespeople in london.
SELECT Snum, Comm
FROM SalesPeople
WHERE City = 'London';
GO

--4.All customers with rating of 100.
SELECT Cname 
FROM Customers
WHERE Rating = 100;
GO

--5.Produce orderno, amount and date form all rows in the order table.
SELECT Onum, AMT, Odate
FROM Orders;
GO

--6.All customers in San Jose, who have rating more than 200
SELECT Cname, City, Rating
FROM Customers
WHERE City = 'San Jose' AND Rating > 200;
GO

--7.All customers who were either located in San Jose or had a rating above 200
SELECT Cname, City, Rating
FROM Customers
WHERE City = 'San Jose' OR Rating > 200;
GO

--8.All orders for more than $1000.
SELECT *
FROM Orders
WHERE AMT > 1000;
GO

--9.Names and cites of all salespeople in london with commission above 0.10.
SELECT Sname, City, Comm
FROM SalesPeople
WHERE City = 'London' AND Comm > 0.10;
GO

--10.All customers excluding those with rating <= 100 unless they are located in Rome
SELECT Cname, City, Rating
FROM Customers
WHERE Rating <= 100 OR City = 'Rome';
GO

--11.All salespeople either in Barcelona or in london.
SELECT Sname, City
FROM SalesPeople
WHERE City IN ('Barcelona','london');
GO

--12.All salespeople with commission between 0.10 and 0.12. (Boundary values should be excluded)
SELECT Sname, Comm
FROM SalesPeople
WHERE Comm > 0.10 AND Comm < 0.12;
GO

--13.All customers with NULL values in city column.
SELECT Cname, City
FROM Customers
WHERE City IS NULL;
GO

--14.All orders taken on Oct 3Rd   and Oct 4th  1994.
SELECT *
FROM Orders
WHERE Odate IN ('03-OCT-94','04-OCT-94');
GO

--15.All customers serviced by peel or Motika.
SELECT Cname
FROM Customers, Orders
WHERE Orders.Cnum = Customers.Cnum 
AND Orders.Snum IN( SELECT Snum FROM SalesPeople WHERE Sname IN ('Peel','Motika'));
GO

--16.All customers whose names begin with a letter from A to B.
SELECT Cname
FROM Customers
WHERE Cname LIKE 'A%' OR Cname LIKE 'B%';
GO

--17.All orders except those with 0 or NULL value in amt field.
SELECT *
FROM Orders
WHERE AMT != 0 OR AMT IS NOT NULL;
GO

--18.Count the number of salespeople currently listing orders in the order table.
SELECT COUNT(DISTINCT Snum) AS 'salespeople currently listing orders'
FROM Orders;
GO

--19.Largest order taken by each salesperson, datewise
SELECT Snum, Odate, MAX(AMT) AS 'Largest order'
FROM Orders
GROUP BY Odate, Snum
ORDER BY Odate,Snum;
GO

--20.Largest order taken by each salesperson with order value more than $3000.
SELECT Snum, Odate, MAX(AMT) AS 'Largest order'
FROM Orders
WHERE AMT > 3000
GROUP BY Odate, Snum
ORDER BY Odate, Snum;
GO

--21.Which day had the hightest total amount ordered.
SELECT Odate, AMT, Snum, Cnum
FROM Orders
WHERE AMT = ( SELECT MAX(AMT) FROM Orders);
GO

--22.Count all orders for Oct 3rd.
SELECT COUNT(*) AS 'Orders on Oct 3rd'
FROM Orders
WHERE Odate = '03-OCT-94';
GO

--23.Count the number of different non NULL city values in customers table.
SELECT COUNT(DISTINCT City)
FROM Customers;
GO

--24.Select each customer’s smallest order.
SELECT Cnum, MIN(AMT)
FROM Orders
GROUP BY Cnum;
GO 

--25.First customer in alphabetical order whose name begins with G.
SELECT MIN(Cname)
FROM Customers
WHERE Cname LIKE 'G%';
GO

-- --26.Get the output like “ For dd/mm/yy there are ___ orders.
-- SELECT 'For'  (CONVERT(varchar(10), GETDATE(),120)) || 'there are' || COUNT(*) || 'Orders'
-- FROM Orders
-- GROUP BY Odate;
-- GO

--27.Assume that each salesperson has a 12% commission. Produce order no., salesperson no., 
--and amount of salesperson’s commission for that order.
SELECT Onum, Snum, AMT, AMT * 0.12 AS 'Commission'
FROM Orders
ORDER BY Snum;
GO

--28. Find highest rating in each city. Put the output in this form. For the city (city), 
--the highest rating is : (rating).
-- Select 'For the city (' || City || '), the highest rating is : (' || MAX(Rating) || ')'
-- FROM Customers
-- GROUP BY city;

--29.Display the totals of orders for each day and place the results in descending order.
SELECT Odate, COUNT(Onum) AS 'Total No of Orders'
FROM Orders
GROUP BY Odate
ORDER BY COUNT(Onum) DESC;
GO

--30.All combinations of salespeople and customers who shared a city. (ie same city).
SELECT Sname, Cname, S.City AS City
FROM SalesPeople AS S, Customers AS C
WHERE S.City = C.City;
GO

--31.Name of all customers matched with the salespeople serving them
SELECT Cname, Sname 
FROM Customers AS C, SalesPeople AS S
WHERE C.Snum = S.Snum;
GO

--32.List each order number followed by the name of the customer who made the order.
SELECT Onum, Cname
FROM Customers AS C, Orders AS O
WHERE O.Cnum = C.Cnum;
GO

--33.Names of salesperson and customer for each order after the order number.
SELECT Onum, Sname, Cname
FROM Orders AS O, Customers AS C, SalesPeople AS S
WHERE O.Cnum = C.Cnum and O.Snum = S.Snum;
GO

--34.Produce all customer serviced by salespeople with a commission above 12%.
SELECT Cname, Sname, Comm
FROM Customers AS C, SalesPeople AS S
WHERE Comm > 0.12 AND C.Snum = S.Snum;
GO

--35.Calculate the amount of the salesperson’s commission on each order with a rating above 100.
SELECT Sname, AMT*Comm, Rating
FROM Customers AS C, SalesPeople AS S, Orders AS O
WHERE Rating > 100 AND 
        S.Snum = C.Snum AND 
        S.Snum = O.Snum AND 
        O.Cnum = C.Cnum;
GO

--36.Find all pairs of customers having the same rating.
SELECT a.Cname, b.Cname, a.Rating
FROM Customers a, Customers b
WHERE a.Rating = b.Rating and a.Cnum != b.Cnum;
GO

--37.Find all pairs of customers having the same rating, each pair coming once only.
SELECT a.Cname, b.Cname, a.Rating
FROM Customers a, Customers b
WHERE a.Rating = b.Rating AND a.Cnum != b.Cnum AND a.Cnum < b.Cnum;
GO

--38.Policy is to assign three salesperson to each customers. Display all such combinations.
-- Select Cname, Sname
-- FROM SalesPeople, Customers
-- WHERE Sname IN  ( SELECT Sname FROM salespeople WHERE rownum <= 3)
-- ORDER BY Cname;
-- GO

--39.Display all customers located in cities where salesman serres has customer.
SELECT Cname
FROM Customers
WHERE City IN ( SELECT City FROM Customers AS C, Orders AS O
                WHERE C.Cnum = O.Cnum AND 
                    O.Snum IN ( SELECT Snum FROM SalesPeople 
                                WHERE Sname = 'Serres'));
GO

--40.Find all pairs of customers served by single salesperson.
SELECT DISTINCT a.Cname
FROM Customers a ,Customers b
WHERE a.Snum = b.Snum and a.Cnum != b.Cnum;
GO

--41.Produce all pairs of salespeople which are living in the same city. 
--Exclude combinations of salespeople with themselves as well as duplicates with the order reversed.
SELECT a.Sname, b.Sname
FROM SalesPeople a, SalesPeople b
WHERE a.Snum > b.Snum AND a.City = b.City;
GO

--42.Produce all pairs of orders by given customer, names that customers and eliminates duplicates.
SELECT c.Cname, a.Onum, b.Onum
FROM Orders a, Orders b, Customers c
WHERE a.Cnum = b.Cnum AND 
        a.Onum > b.Onum AND 
        c.Cnum = a.Cnum;
GO

--43.Produce names and cities of all customers with the same rating as Hoffman.
SELECT Cname, City
FROM Customers
WHERE Rating = (SELECT Rating FROM Customers WHERE Cname = 'Hoffman') AND Cname != 'Hoffman';
GO

--44.Extract all the orders of Motika.
SELECT Onum
FROM Orders
WHERE Snum = ( SELECT Snum FROM SalesPeople WHERE Sname = 'Motika');
GO

--45.All orders credited to the same salesperson who services Hoffman
SELECT Onum, sname, Cname, AMT
from Orders AS O, SalesPeople AS S, Customers C
where O.Snum = S.Snum AND O.Cnum = C.Cnum AND
          O.Snum = ( SELECT Snum FROM Orders
                        WHERE Cnum = ( SELECT Cnum FROM Customers
                                        WHERE Cname = 'Hoffman'));
GO

--46.All orders that are greater than the average for Oct 4.
SELECT *
FROM Orders
WHERE AMT > ( SELECT AVG(AMT) FROM Orders
                WHERE Odate = '03-OCT-94');
GO

--47.Find average commission of salespeople in london.
SELECT AVG(Comm)
FROM SalesPeople
WHERE City = 'London';
GO

--48.Find all orders attributed to salespeople servicing customers in london.
SELECT Snum, Cnum
FROM Orders
WHERE Cnum IN (SELECT Cnum FROM Customers WHERE City = 'London');
GO

--49.Extract commissions of all salespeople servicing customers in London.
SELECT Comm
FROM SalesPeople
WHERE Snum IN (SELECT Snum FROM Customers WHERE City = 'London');
GO

--50.Find all customers whose cnum is 1000 above the snum of serres.
SELECT Cnum, Cname from Customers
where Cnum > ( SELECT Snum + 1000
                FROM SalesPeople
                WHERE Sname = 'Serres');
GO








