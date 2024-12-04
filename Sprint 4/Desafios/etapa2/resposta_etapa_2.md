# É possível reutilizar containers?

Quando executa o comando __docker run <nome_do_container>__ , um novo container é criado. Mesmo após sua execução, o container permanece na máquina, podendo ser listado com o comando __docker ps -a__. Dessa forma, é possível reiniciá-lo utilizando __docker start <nome_do_container>__. 

Se o container foi criado com a opção __--rm__, ele será automaticamente removido após o término de sua execução, ou seja, não poderá reutilizar ele futuramente.