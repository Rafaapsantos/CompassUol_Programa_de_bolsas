select tbvendas.cdpro, tbvendas.nmpro
from 
tbvendas
where 
tbvendas.status = 'Concluído'
and
tbvendas.dtven BETWEEN '2014-02-03' and '2018-02-02'
GROUP by tbvendas.cdpro
ORDER by COUNT(*) DESC 
LIMIT 1
