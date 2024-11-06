DROP table if exists tb_combustivel;

CREATE TABLE tb_combustivel (
idCombustivel integer primary key autoincrement,
tipoCombustivel varchar(15)
);

DROP table if exists tb_carro;

CREATE table tb_carro (
idCarro integer primary key autoincrement,
kmCarro int,
classiCarro varchar(30),
marcaCarro varchar(30),
modeloCarro varchar(30),
anoCarro date,
idCombustivel int not null,
FOREIGN KEY (idCombustivel) REFERENCES tb_combustivel(idCombustivel)
);

DROP table if exists tb_endereco;

CREATE table tb_endereco (
idEndereco integer primary key autoincrement,
cidadeCliente varchar(20),
estadoCliente varchar(20),
paisCliente varchar(20)
);

DROP table if exists tb_cliente;

CREATE table tb_cliente (
idCliente integer primary key autoincrement,
nomeCliente varchar(40),
idEndereco int not null,
FOREIGN KEY (idEndereco) REFERENCES tb_endereco(idEndereco)
);

DROP table if exists tb_vendedor;

CREATE table tb_vendedor (
idVendedor integer primary key autoincrement,
nomeVendedor varchar(40),
sexoVendedor int,
estadoVendedor varchar(20)
);

DROP table if exists tb_locacao_nova;

CREATE table tb_locacao_nova (
idLocacao integer primary key autoincrement,
idCliente int,
idVendedor int,
idCarro int,
dataLocacao date,
horaLocacao time,
dataEntrega date, 
horaEntrega time,
qtdDiaria int, 
vlrDiaria decimal,
FOREIGN KEY (idCliente) REFERENCES tb_cliente(idCliente),
FOREIGN KEY (idVendedor) REFERENCES tb_vendedor(idVendedor),
FOREIGN KEY (idCarro) REFERENCES tb_carro(idCarro)
);

INSERT into tb_combustivel (idCombustivel, tipoCombustivel)
SELECT DISTINCT 
tb_locacao.idcombustivel, 
tb_locacao.tipoCombustivel 
from tb_locacao; 

INSERT INTO tb_vendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
SELECT DISTINCT
tb_locacao.idVendedor,
tb_locacao.nomeVendedor,
tb_locacao.sexoVendedor, 
tb_locacao.estadoVendedor 
from tb_locacao; 

INSERT INTO tb_endereco (cidadeCliente, estadoCliente, paisCliente)
SELECT DISTINCT 
tb_locacao.cidadeCliente,
tb_locacao.estadoCliente,
tb_locacao.paisCliente 
from tb_locacao; 

INSERT INTO tb_cliente (idCliente, nomeCliente, idEndereco)
SELECT DISTINCT 
tb_locacao.idCliente,
tb_locacao.nomeCliente,
tb_endereco.idEndereco 
from tb_locacao 
join tb_endereco on tb_locacao.cidadeCliente = tb_endereco.cidadeCliente;

INSERT INTO tb_carro (kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel)
SELECT DISTINCT
tb_locacao.kmCarro,
tb_locacao.classiCarro,
tb_locacao.marcaCarro,
tb_locacao.modeloCarro,
tb_locacao.anoCarro,
tb_combustivel.idcombustivel
from tb_locacao 
left join tb_combustivel on tb_locacao.idcombustivel = tb_combustivel.idCombustivel;

INSERT INTO tb_locacao_nova (idLocacao, idCliente, idVendedor, idCarro, dataLocacao, horaLocacao, dataEntrega, horaEntrega, qtdDiaria, vlrDiaria)
SELECT 
tb_locacao.idLocacao,
tb_locacao.idCliente,
tb_locacao.idVendedor,
tb_locacao.idCarro,
DATE(SUBSTR(tb_locacao.dataLocacao, 1, 4) || '-' || SUBSTR(tb_locacao.dataLocacao, 5, 2) || '-' || SUBSTR(tb_locacao.dataLocacao, 7, 2)) as dataLocacao,
tb_locacao.horaLocacao,
DATE(SUBSTR(tb_locacao.dataEntrega, 1, 4) || '-' || SUBSTR(tb_locacao.dataEntrega, 5, 2) || '-' || SUBSTR(tb_locacao.dataEntrega, 7, 2)) as dataEntrega,
tb_locacao.horaEntrega,
tb_locacao.qtdDiaria,
tb_locacao.vlrDiaria
from tb_locacao 
left join tb_cliente on tb_locacao.idCliente = tb_cliente.idCliente 
left join tb_vendedor on tb_locacao.idVendedor = tb_vendedor.idVendedor 
left join tb_carro on tb_locacao.idCarro = tb_carro.idCarro;





