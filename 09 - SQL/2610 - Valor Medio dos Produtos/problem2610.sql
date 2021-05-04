/* 
    URI Online Judge 
	Problema 2610 - Valor Medio dos Produtos
    https://www.urionlinejudge.com.br/repository/UOJ_2610.html 
 */

SELECT 
    ROUND(AVG(price), 2) AS price 
FROM 
    products