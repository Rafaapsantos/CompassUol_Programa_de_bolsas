import json
import boto3
import requests
from datetime import datetime


chave_api = "api_key"
LANGUAGE = "en-US"  # idioma das respostas da API
layer = "Raw/TMDB/JSON"  # caminho da camada no bucket
max_registros = 100 # número máximo de registros que deve ter por arquivo
tamanho_max_arquivo = 10 * 1024 * 1024  # tamanho máximo que deve ter por arquivo (10 MB)

# cliente do S3
s3_client = boto3.client('s3')


def lambda_handler(event, context):
    # lista de IDs do IMDb para buscar as informações na API
    imdb_ids = ["tt10356932","tt11644218","tt12498118","tt1740495","tt1935089","tt2186712","tt2245924","tt2270456","tt2385126","tt2515180","tt2547584","tt2674426","tt2707722","tt2787570","tt2931140","tt3215826","tt3227442","tt3312884","tt3344694","tt3517044","tt3530896","tt3530978","tt3548978","tt3581704","tt3584390","tt3675606","tt3722726","tt3766366","tt3777860","tt3794028","tt3794392","tt3797868","tt3840534","tt3920890","tt4024814","tt4047456","tt4061196","tt4109998","tt4113916","tt4116388","tt4126694","tt4171876","tt4179950","tt4188654","tt4193394","tt4262174","tt4262516","tt4291600","tt4305148","tt4327510","tt4331970","tt4385026","tt4399594","tt4439194","tt4446472","tt4462372","tt4495846","tt4551008","tt4568352","tt4579982","tt4581548","tt4613254","tt4625334","tt4641478","tt4655294","tt4682786","tt4726166","tt4746506","tt4805816","tt4828926","tt4837126","tt4842648","tt4842932","tt4874298","tt4898726","tt4921812","tt4932154","tt4937518","tt4988692","tt4996022","tt5002872","tt5011242","tt5011290","tt5012910","tt5025550","tt5069012","tt5073620","tt5082662","tt5096628","tt5108912","tt5112054","tt5123944","tt5143826","tt5152652","tt5159384","tt5160154","tt5174974","tt5211596","tt5211710","tt5224814","tt5233410","tt5240732","tt5271772","tt5275314","tt5281432","tt5307382","tt5312232","tt5321816","tt5324962","tt5330644","tt5358948","tt5359624","tt5452814","tt5468386","tt5486170","tt5498526","tt5500468","tt5509142","tt5511546","tt5542470","tt5571230","tt5584426","tt5592228","tt5597452","tt5599016","tt5604446","tt5615904","tt5665940","tt5670190","tt5687416","tt5696096","tt5700648","tt5700962","tt5702600","tt5708800","tt5717110","tt5719222","tt5721654","tt5732458","tt5741848","tt5742306","tt5751836","tt5755796","tt5755912","tt5769516","tt5769916","tt5784778","tt5796478","tt5796986","tt5812842","tt5819870","tt5831146","tt5841956","tt5843056","tt5851030","tt5857918","tt5866732","tt5883008","tt5883632","tt5885620","tt5889406","tt5891136","tt5912454","tt5917118","tt5917958","tt5925180","tt5934922","tt5937802","tt5944422","tt5946128","tt5968008","tt5974454","tt5975248","tt5999588","tt6036428","tt6047852","tt6048582","tt6048828","tt6054290","tt6071568","tt6074202","tt6088370","tt6091936","tt6102000","tt6121564","tt6123210","tt6129730","tt6149804","tt6168298","tt6182402","tt6205538","tt6207962","tt6209662","tt6215376","tt6229786","tt6242664","tt6274338","tt6283780","tt6381764","tt6389310","tt6397242","tt6402466","tt6449114","tt6582868","tt6768348","tt7032958","tt7308238","tt7360646","tt7370564","tt7407098","tt7507402","tt7698812","tt7836584","tt7951786","tt8483452","tt8620002","tt8750600","tt8835580","tt9257662"]  
    
    # lista para armazenar os registros que serão coletados
    dados_json = []
    count_arquivo = 1 # contador dos arquivos
    
    # itera sobre os IDs do IMDb
    for imdb_id in imdb_ids:
        # URL de requisição da API do TMDB
        url = f"https://api.themoviedb.org/3/movie/{imdb_id}?api_key={chave_api}&language=en-US"
        response = requests.get(url) # faz a requisição
        
        # se a resposta foi bem-sucedida, coverte ela para JSON
        if response.status_code == 200:
            dados_movie = response.json()
            
            # extrai as informações relevantes para a minha análise dos filmes
            registros = {
                "budget": dados_movie.get("budget"),
                "production_countries": dados_movie.get("production_countries"),
                "popularity": dados_movie.get("popularity"),
                "origin_country": dados_movie.get("origin_country"),
                "original_language": dados_movie.get("original_language")
            }
            dados_json.append(registros) # adiciona os registros na lista
            
            # verifica se o número de registros ou tamanho do arquivo atinge o limite, se sim ele..
            if len(dados_json) >= max_registros or len(json.dumps(dados_json).encode("utf-8")) >= tamanho_max_arquivo:
                save_to_s3(dados_json, count_arquivo) # salva os dados no S3
                dados_json = [] # limpa a lista para o próximo arquivo
                count_arquivo += 1 # incrementa o contador
        else:
             # senão imprime um erro caso a requisição falhe
            print(f"Erro ao buscar dados para ID {imdb_id}: {response.status_code}")
    
    # salva os dados restantes (se tiver) no S3
    if dados_json:
        save_to_s3(dados_json, count_arquivo)

def save_to_s3(data, count_arquivo):
    # pega a data atual no formato YYYY/MM/DD para criar os caminhos no bucket S3
    data = datetime.now().strftime("%Y/%m/%d")
    nome_arquivo = f"arquivo-{count_arquivo}.json" # nome do arquivo
    caminho_arquivo = f"{layer}/{data}/{nome_arquivo}" # caminho do bucket
    
    # faz o upload do arquivo para o S3
    s3_client.put_object(
        Bucket="datalake-rafaela-santos",
        Key=caminho_arquivo,
        Body=json.dumps(data),
        ContentType="application/json"
    )
    print(f"Arquivo salvo no S3: {caminho_arquivo}") 