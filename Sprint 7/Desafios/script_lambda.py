import json
import boto3
import requests
from datetime import datetime


API_KEY = "api_key"
LANGUAGE = "en-US"
url = "https://api.themoviedb.org/3/movie/"
bucket = "nome bucket"
layer = "Raw/TMDB/JSON"
max_registros = 100
tamanho_max_arquivo = 10 * 1024 * 1024  # 10 MB

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    imdb_ids = ["tt10356932","tt11644218","tt11656988","tt12498118","tt13231658","tt1740495","tt1935089","tt2186712","tt2245924","tt2270456","tt2385126","tt2515180","tt2547584","tt2674426","tt2707722","tt2787570","tt2931140","tt3215826","tt3227442","tt3312884","tt3344694","tt3517044","tt3526416","tt3530896","tt3530978","tt3548978","tt3581704","tt3584390","tt3675606","tt3722726","tt3766366","tt3777860","tt3794028","tt3794392","tt3797868","tt3840534","tt3920890","tt4024814","tt4047456","tt4061196","tt4109998","tt4113916","tt4116388","tt4126694","tt4171876","tt4179950","tt4188654","tt4193394","tt4262174","tt4262516","tt4291600","tt4305148","tt4327510","tt4331970","tt4332342","tt4385026","tt4399594","tt4439194","tt4446472","tt4462372","tt4495846","tt4551008","tt4568352","tt4579982","tt4581548","tt4613254","tt4625334","tt4641478","tt4655294","tt4682786","tt4726166","tt4746506","tt4805816","tt4828926","tt4837126","tt4842648","tt4842932","tt4874298","tt4898726","tt4921812","tt4932154","tt4937518","tt4988692","tt4996022","tt5002872","tt5011242","tt5011290","tt5012910","tt5025550","tt5069012","tt5073620","tt5082662","tt5096628","tt5108912","tt5112054","tt5123944","tt5143826","tt5152652","tt5159384","tt5160154"]  
    
    dados_json = []
    count_arquivo = 1
    
    for imdb_id in imdb_ids:
        url = f"{url}{imdb_id}?api_key={API_KEY}&language={LANGUAGE}"
        response = requests.get(url)
        
        if response.status_code == 200:
            dados_movie = response.json()
            
            registros = {
                "budget": dados_movie.get("budget"),
                "production_countries": dados_movie.get("production_countries"),
                "popularity": dados_movie.get("popularity"),
                "origin_country": dados_movie.get("origin_country"),
                "original_language": dados_movie.get("original_language")
            }
            dados_json.append(registros)
            
            if len(dados_json) >= max_registros or len(json.dumps(dados_json).encode("utf-8")) >= tamanho_max_arquivo:
                save_to_s3(dados_json, count_arquivo)
                dados_json = []
                count_arquivo += 1
        else:
            print(f"Erro ao buscar dados para ID {imdb_id}: {response.status_code}")
    
    if dados_json:
        save_to_s3(dados_json, count_arquivo)

def save_to_s3(data, count_arquivo):
    data = datetime.now().strftime("%Y/%m/%d")
    nome_arquivo = f"file-{count_arquivo}.json"
    caminho_arquivo = f"{layer}/{data}/{nome_arquivo}"
    
    s3_client.put_object(
        Bucket=bucket,
        Key=caminho_arquivo,
        Body=json.dumps(data),
        ContentType="application/json"
    )
    print(f"Arquivo salvo no S3: {caminho_arquivo}") 