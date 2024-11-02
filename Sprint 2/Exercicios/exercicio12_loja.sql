SELECT 
    tbdependente.cddep,
    tbdependente.nmdep,
    tbdependente.dtnasc,
    MIN(vendas_por_dependente.valor_total_vendas) as valor_total_vendas
from tbdependente
LEFT JOIN (
    SELECT 
        tbvendas.cdvdd,
        SUM(tbvendas.qtd * tbvendas.vrunt) as valor_total_vendas
    from tbvendas 
    WHERE tbvendas.status = 'Concluído'
    GROUP by tbvendas.cdvdd
) as vendas_por_dependente on tbdependente.cdvdd = vendas_por_dependente.cdvdd
GROUP by tbdependente.cddep, tbdependente.nmdep, tbdependente.dtnasc
ORDER by  tbdependente.cddep DESC 
LIMIT 1