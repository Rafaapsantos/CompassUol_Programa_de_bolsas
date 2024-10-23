#!/bin/bash

DATAATUAL=$(date +"%Y%m%d")

# aqui ele muda para o diretrio ecommerce e dentro dele cria o diretório vendas, depois copia o arquivo dados_de_vendas.csv para dentro do diretorio vendas  
cd ecommerce
mkdir -p vendas
cp dados_de_vendas.csv vendas/

# cria o diretorio backup dentro do diretório vendas e copia o arquivo com o nome e a data
mkdir -p vendas/backup
cp vendas/dados_de_vendas.csv "vendas/backup/dados-$DATAATUAL.csv"

# Renomeia o arquivo no diretório backup
mv "vendas/backup/dados-$DATAATUAL.csv" "vendas/backup/backup-dados-$DATAATUAL.csv"

# Cria o relatório com informações de vendas como data da 1° venda, data da ultima venda e qntd de itens vendidos
echo "$(date +"%Y/%m/%d %H:%M")" > vendas/backup/relatorio.txt
echo "DATA DA PRIMEIRA VENDA: $(awk -F, 'NR==2 {print $5}' vendas/dados_de_vendas.csv)" >> vendas/backup/relatorio.txt
echo "DATA DA ULTIMA VENDA: $(awk -F, 'END{print $5}' vendas/dados_de_vendas.csv)" >> vendas/backup/relatorio.txt
echo "QUANTIDADE TOTAL DE ITENS QUE SÃO DIFERENTES VENDIDOS: $(awk -F, 'NR>1 {print $2}' vendas/dados_de_vendas.csv | sort | uniq | wc -l)" >> vendas/backup/relatorio.txt

# Mostra as 10 primeiras linhas do arquivo e coloca eles no relatório
head -n 10 "vendas/backup/backup-dados-$DATAATUAL.csv"
head -n 10 "vendas/backup/backup-dados-$DATAATUAL.csv" >> "vendas/backup/relatorio-$DATAATUAL.txt"

#junta o relatorio.txt no relatorio-$DATAATUAL.txt e exclui o relatorio.txt
cat vendas/backup/relatorio.txt >> "vendas/backup/relatorio-$DATAATUAL.txt"
rm vendas/backup/relatorio.txt

# Comprime o arquivo backup-dados-<yyyymmdd>.csv para backup-dados-<yyyymmdd>.zip
zip "vendas/backup/backup-dados-$DATAATUAL.zip" "vendas/backup/backup-dados-$DATAATUAL.csv"

# Apaga os arquivos originais depois que comprime
rm "vendas/backup/backup-dados-$DATAATUAL.csv"
rm vendas/dados_de_vendas.csv
