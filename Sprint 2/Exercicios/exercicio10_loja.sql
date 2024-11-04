SELECT tbvendedor.nmvdd as vendedor, 
SUM(tbvendas.qtd * tbvendas.vrunt) as valor_total_vendas,
ROUND((SUM(tbvendas.qtd * tbvendas.vrunt)* tbvendedor.perccomissao/100),2) as comissao
from tbvendas
left join tbvendedor 
	on tbvendas.cdvdd  = tbvendedor.cdvdd 
WHERE tbvendas.status = 'Concluído' 
GROUP BY tbvendedor.nmvdd 
ORDER by comissao DESC

