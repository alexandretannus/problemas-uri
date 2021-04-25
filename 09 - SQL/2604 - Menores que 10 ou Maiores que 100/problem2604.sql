/* 
	URI Online Judge 
	Problema 2604 - Menores que 10 ou Maiores que 100
    https://www.urionlinejudge.com.br/repository/UOJ_2604.html
 */

SELECT
    id, name
FROM
    products
WHERE
    price < 10 OR price > 100