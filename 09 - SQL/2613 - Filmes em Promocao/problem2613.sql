/* 
    URI Online Judge 
	Problema 2613 - Filmes em Promocao
    https://www.urionlinejudge.com.br/repository/UOJ_2613.html 
 */

SELECT 
    movies.id,
    movies.name
FROM 
    movies INNER JOIN prices ON movies.id_prices=prices.id
WHERE 
    prices.value < 2