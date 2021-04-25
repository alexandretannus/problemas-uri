/* 
	URI Online Judge 
	Problema 2606 - Categorias
    https://www.urionlinejudge.com.br/repository/UOJ_2606.html
 */

SELECT 
    products.id,
    products.name
FROM
    products 
        INNER JOIN categories
            ON products.id_categories=categories.id
WHERE
    categories.name LIKE 'super%'