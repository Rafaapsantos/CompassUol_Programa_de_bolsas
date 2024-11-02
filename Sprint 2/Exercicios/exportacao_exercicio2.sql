select 
	editora.codeditora as CodEditora,
	editora.nome as NomeEditora,
	count(*) as QuantidadeLivros
from livro 
left join editora 
	on livro.editora = editora.codeditora 
group by editora.codeditora 
order by QuantidadeLivros desc
limit 5 