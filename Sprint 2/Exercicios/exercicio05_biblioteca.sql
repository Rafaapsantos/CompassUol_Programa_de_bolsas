SELECT DISTINCT autor.nome
from autor 
left join livro 
	on autor.codautor = livro.autor 
left JOIN editora 
	on editora.codeditora = livro.editora 
left JOIN endereco 
	on endereco.codendereco = editora.endereco 
	WHERE endereco.estado NOT IN ('PARANÁ', 'RIO GRANDE DO SUL')
ORDER BY autor.nome