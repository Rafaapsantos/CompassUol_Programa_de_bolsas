SELECT tbvendas.cdcli , 
tbvendas.nmcli,
SUM(tbvendas.qtd * tbvendas.vrunt) as gasto
from tbvendas 
WHERE tbvendas.status = 'Concluído'
GROUP by tbvendas.cdcli 
ORDER by gasto DESC 
LIMIT 1

