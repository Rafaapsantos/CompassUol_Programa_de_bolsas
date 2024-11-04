SELECT tbvendas.cdpro,
tbvendas.nmcanalvendas, 
tbvendas.nmpro,
SUM(tbvendas.qtd) as quantidade_vendas 
from tbvendas 
WHERE tbvendas.status = 'Concluído'
GROUP by tbvendas.cdpro, tbvendas.nmcanalvendas 
ORDER by quantidade_vendas 
LIMIT 10
