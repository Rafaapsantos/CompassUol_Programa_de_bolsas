### 1° - Comecei o desafio criando o diretório ecommerce e colocando o arquivo dados_de_venda.csv dentro dele.
![criando_ecommerce](https://github.com/user-attachments/assets/4325b24a-eaf5-4f7c-bc20-9731bae28da9)

### 2° - Depois eu fiz o scrpit processamento_de_vendas.sh usando o editor de texto nano. 

![script](https://github.com/user-attachments/assets/f88eef0a-6e24-4a37-be22-444fccabec14)
![script](https://github.com/user-attachments/assets/b2768434-4b55-4ce1-976a-7b305e898e3c)
![script](https://github.com/user-attachments/assets/cc22e7bf-602d-463e-b9bb-07988bf9e488)

### 3° - Tornei o arquivo processamento_de_vendas.sh executável.
![executavel](https://github.com/user-attachments/assets/a40fd833-57f0-436d-b0b1-7a26d8f1a718)

### 4° - Fiz um agendamento usando o crontab para executar todos os dias da semana as 15:27
![crontab](https://github.com/user-attachments/assets/21a66519-a1d6-426f-b33c-acbaa40d80c0)

### 5° - Iniciei o crontab todos os dias e ele rodou o script criando os relatorios
![crontab](https://github.com/user-attachments/assets/a895b274-d536-4607-9d23-a882991cf4d5)

### 6° - Após o crontab executar o script, o cenario é esse: 
##### Dentro do diretório ecommerce, foi criado uma pasta vendas, que dentro dessa pasta vendas foi criado uma pasta backup. Dentro da pasta backup, foi criado o relatorio e um arquivo zip.
![cenario](https://github.com/user-attachments/assets/cbba2ba8-9fe6-4aa2-9d3b-0fddbb3b7e83)


### 7° - Após o script ser executado eu parei o crontab.
![crontab](https://github.com/user-attachments/assets/2aad8b3e-0088-4aea-9142-f0c426c040a8)


### 8° - Depois de rodar o script usando o crontab os 4 dias, eu fiz um script chamado consolidador_de_processamento_de_vendas.sh que juntou todos os relatórios dos 4 dias em um único relatorio 
![consolidador](https://github.com/user-attachments/assets/cc5ee5b7-7b05-410c-a43a-c2834f0aad44)
![consolidador](https://github.com/user-attachments/assets/bfa663ec-f04b-4ba6-b76e-7b9432543295)

### 9° - Tornei o arquivo consolidador_de_processamento_de_vendas.sh executável.

### 10° - Executei manualmente o script consolidador_de_processamento_de_vendas.sh

### 9° - Após isso foi criado o relatorio_final.txt, onde contém todos os relatórios.
