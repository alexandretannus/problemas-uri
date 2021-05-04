/* 
    URI Online Judge 
	Problema 2609 - Produtos por Categorias
    https://www.urionlinejudge.com.br/repository/UOJ_2609.html 
 */

SELECT 
    categories.name AS "name",
    sum(products.amount) AS "sum"
FROM 
    categories INNER JOIN products ON products.id_categories=categories.id
GROUP BY
    categories.id
ORDER BY
    categories.name