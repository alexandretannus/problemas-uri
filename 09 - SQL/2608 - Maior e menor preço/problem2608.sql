/* 
	URI Online Judge 
	Problema 2608 - Maior e menor preço
    https://www.urionlinejudge.com.br/repository/UOJ_2608.html
 */
 
SELECT 
    MAX(price) AS price, 
    MIN(price) AS price
FROM 
    products;