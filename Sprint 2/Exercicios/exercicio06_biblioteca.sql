SELECT 
autor.codautor, 
autor.nome, 
COUNT(livro.autor) as quantidade_publicacoes
from autor 
left join livro
on livro.autor = autor.codautor 
GROUP by autor.codautor, autor.nome 
ORDER BY quantidade_publicacoes DESC 
LIMIT 1
