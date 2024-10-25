### 1° - Comecei o desafio criando o diretório ecommerce e colocando o arquivo dados_de_venda.csv dentro dele.
![evidencia1](/Sprint%201/Evidencias/evidencia1.jpeg)

### 2° - Depois eu fiz o script processamento_de_vendas.sh usando o editor de texto nano. 

![evidencia2](/Sprint%201/Evidencias/evidencia2.jpeg)
![evidencia2.1](/Sprint%201/Evidencias/evidencia2.1.jpeg)
![evidencia2.2](/Sprint%201/Evidencias/evidencia2.2.jpeg)

### 3° - Tornei o arquivo processamento_de_vendas.sh executável.
![evidencia3](/Sprint%201/Evidencias/evidencia3.jpeg)

### 4° - Fiz um agendamento usando o crontab para executar todos os dias da semana as 15:27
![evidencia4](/Sprint%201/Evidencias/evidencia4.jpeg)
![evidencia4.1](/Sprint%201/Evidencias/evidencia4.1.jpeg)

### 5° - Iniciei o crontab todos os dias e ele rodou o script criando os relatorios
![evidencia5](/Sprint%201/Evidencias/evidencia5.jpeg)

### 6° - Após o crontab executar o script, o cenario é esse: 
Dentro do diretório ecommerce, foi criado uma pasta vendas, que dentro dessa pasta vendas foi criado uma pasta backup. Dentro da pasta backup, foi criado o relatorio do 1° dia e um arquivo zip.
![evidencia6](/Sprint%201/Evidencias/evidencia6.jpeg)

### 6.1° -  Depois do crontab ter executado o script por 4 dias, o cenario é esse: 
![evidencia6.1](/Sprint%201/Evidencias/evidencia6.1.jpeg)

### 7° - Após o script ser executado eu parei o crontab.
![evidencia7](/Sprint%201/Evidencias/evidencia7.jpeg)


### 8° - Depois de rodar o script usando o crontab os 4 dias, eu fiz um script chamado consolidador_de_processamento_de_vendas.sh que juntou todos os relatórios dos 4 dias em um único relatorio 
![evidencia8](/Sprint%201/Evidencias/evidencia8.jpeg)
![evidencia8.1](/Sprint%201/Evidencias/evidencia8.1.jpeg)


### 9° - Tornei o arquivo consolidador_de_processamento_de_vendas.sh executável.
![evidencia9](/Sprint%201/Evidencias/evidencia9.jpeg)

### 10° - Executei manualmente o script consolidador_de_processamento_de_vendas.sh
![evidencia10](/Sprint%201/Evidencias/evidencia10.jpeg)

### 11° - Após isso foi criado o relatorio_final.txt, onde contém todos os relatórios.
A minha interpretação do desafio foi que precisava mostrar 10 linhas, então foi isso que eu fiz. 1° linha é a do cabeçalho e 9 linha dos itens.
![evidencia10](/Sprint%201/Evidencias/evidencia11.jpeg)
