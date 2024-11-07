DROP TABLE IF EXISTS dim_carro;

CREATE TABLE dim_carro AS 
SELECT 
tb_carro.idCarro,
tb_carro.kmCarro,
tb_carro.classiCarro,
tb_carro.marcaCarro,
tb_carro.modeloCarro,
tb_carro.anoCarro,
tb_combustivel.idCombustivel
FROM tb_carro  
LEFT JOIN tb_combustivel ON tb_carro.idCombustivel = tb_combustivel.idCombustivel;

DROP TABLE IF EXISTS dim_cliente;

CREATE TABLE dim_cliente AS
SELECT 
tb_cliente.idCliente,
tb_cliente.nomeCliente,
tb_endereco.cidadeCliente,
tb_endereco.estadoCliente,
tb_endereco.paisCliente 
FROM tb_cliente 
LEFT JOIN tb_endereco ON tb_cliente.idEndereco = tb_endereco.idEndereco;

DROP TABLE IF EXISTS dim_vendedor;

CREATE TABLE dim_vendedor AS
SELECT 
tb_vendedor.idVendedor,
tb_vendedor.nomeVendedor,
tb_vendedor.sexoVendedor,
tb_vendedor.estadoVendedor 
FROM tb_vendedor;

DROP TABLE IF EXISTS dim_tempo;

CREATE TABLE dim_tempo AS
SELECT 
tb_locacao.idLocacao,
tb_locacao.dataLocacao,
STRFTIME('%Y', tb_locacao.dataLocacao) AS ano,
STRFTIME('%m', tb_locacao.dataLocacao) AS mes,
STRFTIME('%d', tb_locacao.dataLocacao) AS dia,
tb_locacao.horaLocacao,
tb_locacao.dataEntrega,
STRFTIME('%Y', tb_locacao.dataEntrega) AS ano_entrega,
STRFTIME('%m', tb_locacao.dataEntrega) AS mes_entrega,
STRFTIME('%d', tb_locacao.dataEntrega) AS dia_entrega,
tb_locacao.horaEntrega
FROM tb_locacao;

DROP TABLE IF EXISTS fato_locacao;

CREATE TABLE fato_locacao(
idLocacao INTEGER PRIMARY KEY,
idCliente INTEGER,
idVendedor INTEGER,
idCarro INTEGER,
idTempoLocacao INTEGER,
idTempoEntrega INTEGER,
qtdDiaria INT,
vlrDiaria DECIMAL,
FOREIGN KEY (idCarro) REFERENCES dim_carro(idCarro),
FOREIGN KEY (idCliente) REFERENCES dim_cliente(idCliente),
FOREIGN KEY (idVendedor) REFERENCES dim_vendedor(idVendedor),
FOREIGN KEY (idTempoLocacao) REFERENCES dim_tempo(idLocacao),
FOREIGN KEY (idTempoEntrega) REFERENCES dim_tempo(idLocacao)
);

INSERT INTO fato_locacao(idLocacao, idCliente, idVendedor, idCarro, idTempoLocacao, idTempoEntrega, qtdDiaria, vlrDiaria)
SELECT
tb_locacao.idLocacao,
tb_locacao.idCliente,
tb_locacao.idVendedor,
tb_locacao.idCarro,
tb_locacao.idLocacao AS idTempoLocacao,
tb_locacao.idLocacao AS idTempoEntrega,
tb_locacao.qtdDiaria,
tb_locacao.vlrDiaria 
FROM tb_locacao;

SELECT * FROM dim_carro;

SELECT * FROM dim_cliente;

SELECT * FROM dim_vendedor;

SELECT * FROM dim_tempo;

SELECT * FROM fato_locacao;

