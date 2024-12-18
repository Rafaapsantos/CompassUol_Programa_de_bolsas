import boto3
import os

# Configura as credenciais da AWS
aws_access_key_id = 'ASIAWQUOZ35IUD56MKS3'
aws_secret_access_key = 'I46+t7SKSFtPA9NdmNNDHa6RQgQLDjtv2ExG3um1'
aws_session_token = 'IQoJb3JpZ2luX2VjEJz//////////wEaCXVzLWVhc3QtMSJGMEQCIC3OXK5kqKXMp3IxFILcjmqEeCeeHE75zJj7gMW4IQ87AiBdlVABZbFWurH9fSGhR/l3HC3oJTWikvfxfpkEynS/ECqhAwhlEAAaDDQ0ODA0OTgzMTc2MSIMCtm5ZNIoc/nS6r/xKv4C4sZDWNPL0/EZc+15TM4Jrk79QKvleBcr2vXSMJsiXHKoF4q5pwmhIUenVdk6W4J1GGBQJrRuOwsopyWXxJAQFo6qS6+Fv+gRusm10YEYqTIFF9+aWtqT/LkO68ozJpCvSXS8Gb1ePQ/O0zurBp1o4xXlPc7tnij4gwLqWCw47Rf6bPqrkskAnvcvJG06K1MoljianDVXPf08Y5K18YxfFSeW6HxM24+Bh6W9GRJVjMVAFCsdgghvvysy17pYpqXWPK0soDlhB159b6TdUQHna+FuSHFpByPNmOq4so8sFEQbW6Kfhf+iRxy4soeKIp0or1CTLjW+mRABH0YZkAbrDWoTR8jsTFtRw792TENLaSJJKg7TYTB9iWW/4sCBUJccRPxA5RYFLPh7gEtyr9zC3NjeROAztVehfPcwxz7TCa3ZkGlLnmhZPeJdhzK5+njfBfBzljS/2swpMuGy/eYIg8vVQobTPOyFlZwVMSgc8b9Mt8oWq8OXkTQY+QChyTCg0oy7BjqnAS+yAEVLtuO3MG3qwlX/9FRUSzXmUb7rTVg2K4W3jE5lzH6q+B2XcWB0Rzv+tboVFYbzMrxj3YfJU0FJ3KhEOu+51om+3fKuuQk679j3XBAJg+103dVg7qirM74G9jT8RaRbbXDNceWwYrNBrQKXKbK4eFO5Oi3qR//zHlHPm4pX4ng3FB+bMU+wYDPqHIc3Ya7bxALVXMrN3EBK/l+1pPvFLx/upsfG'

nome_bucket = 'rafaela-santos-desafiosprint5'   # Varíavel com o nome do meu bucket, para ficar mais facil
nome_dataset = 'violencia_domestica_2023.csv'   # Varíavel com o nome do meu dataset, para ficar mais facil
nome_object = os.path.basename(nome_dataset)    #  Varíavel que extrai o nome do dataset para usar no S3

# Cria um cliente S3 usando as minhas credenciais
s3_client = boto3.client(
   's3',
    aws_access_key_id=aws_access_key_id, 
    aws_secret_access_key=aws_secret_access_key, 
    aws_session_token=aws_session_token
)

# Faz o upload do dataset para dentro do bucket
try:
    s3_client.upload_file(nome_dataset, nome_bucket, nome_object) 
    print(f"O dataset {nome_object} foi carregado com sucesso para o bucket {nome_bucket}")
except Exception as e:
    print(f"Erro ao carregar o dataset: {e}")
