/* 
	URI Online Judge 
	Problema 2605 - Representantes Executivos
    https://www.urionlinejudge.com.br/repository/UOJ_2605.html
 */

SELECT 
    products.name,
    providers.name
FROM
    products 
        INNER JOIN providers 
            ON products.id_providers=providers.id
WHERE
    products.id_categories = 6
    