with editora_endereco as (
SELECT 
	editora.nome,
	endereco.estado,
	endereco.cidade,
	editora.codEditora
from editora 
left join endereco 
	on editora.endereco = endereco.codendereco 
)
SELECT 
	count(*) as quantidade,
	editora_endereco.nome,
	editora_endereco.estado,
	editora_endereco.cidade
from livro
left join editora_endereco 
	on editora_endereco.codEditora = livro.editora
group by editora_endereco.nome