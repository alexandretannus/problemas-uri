/* 
	URI Online Judge 
	Problema 2607 - Cidades em Ordem Alfabética
    https://www.urionlinejudge.com.br/repository/UOJ_2607.html
 */

SELECT 
    DISTINCT(providers.city)
FROM 
    providers
ORDER BY
    providers.city