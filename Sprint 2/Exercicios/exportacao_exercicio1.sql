select 
	livro.cod as CodLivro,
	livro.titulo Titulo,
	livro.autor as CodAutor,
	autor.nome as NomeAutor,
	livro.valor as Valor,
	livro.editora as CodEditora,
	editora.nome as NomeEditora
from livro 
left join autor 
	on livro.autor = autor.codautor 
left join editora  
	on livro.editora = editora.codeditora 
order by valor desc
limit 10
