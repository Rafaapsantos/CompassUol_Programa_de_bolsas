SELECT 
autor.nome as nome, 
autor.codautor, 
autor.nascimento, 
COUNT(livro.cod) as quantidade 
from autor 
left join livro 
group by nome 
order by nome 