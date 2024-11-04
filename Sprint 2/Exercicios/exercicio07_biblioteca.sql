SELECT autor.nome
from autor
left join livro
	on autor.codautor = livro.autor 
WHERE livro.autor ISNULL 
ORDER by autor.nome