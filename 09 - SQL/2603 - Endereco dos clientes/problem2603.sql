/* 
	URI Online Judge 
	Problema 2603 - Endereço dos clientes
    https://www.urionlinejudge.com.br/repository/UOJ_2603.html
 */

SELECT
    name, street
FROM
    customers
WHERE
    city = 'Porto Alegre'