SELECT tbvendedor.cdvdd, tbvendedor.nmvdd
from tbvendedor
left join tbvendas
	on tbvendedor.cdvdd = tbvendas.cdvdd
WHERE tbvendas.status = 'Concluído'
GROUP by tbvendedor.cdvdd, tbvendedor.nmvdd
ORDER by COUNT(tbvendas.cdven) DESC
LIMIT 1