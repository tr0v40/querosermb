
# Quero Ser Mb
[![Build Status](https://travis-ci.org/tr0v40/querosermb.svg?branch=main)](https://travis-ci.org/tr0v40/querosermb)
## Teste para Backend - Variações de Médias Moveis Simples



## Sobre 
Este serviço entrega variações de médias móveis simples das moedas Bitcoin e Etherium com valores provinientes da Candles do MB.


## Pre Requisitos
[Local]
Python 3.4+
Fabric3==1.14.post1
Prostgresql 10+

[Server]
Ubuntu 20.04


## Instalação
[Local]
Com o python 3.4+ instalado em sua máquina (https://www.python.org/downloads/), crie uma virtualenv.
Os requisitos devem ser instalados utilizando ```pip install -r requirements.txt```
Após clonar o projeto será necessário criar um banco com nome ```querosermb_db``` e usuário ```querosermb``` com prvilédios de superuser.
Rodar ```python manage.py migrate``` e para popular ```python populate.py```.

[Remoto]
Com seu local pronto, instale o Fabric ´´´pip install Fabric3==1.14.post1´´´.
No arquivo fabfile.py, troque a variável ```env.hosts``` para o domínio do seu server.
No terminal com a sua virtualenv ativa rode o comando ```fab full_instalattion```. Aguarde que esse processo é demorado, porém após sua conclusão seu ubuntu estará atualizado com todas suas dependencias e o sistema ativo para uso sem precisar executar mais nenhum comando.


## Métodos
Requisições para a API devem seguir os padrões
| Método | Descrição |
| --- | --- |
| `GET` | Retorna informações de um ou mais registros . |


## Respostas
| Código | Descrição |
|---|---|
| `200` | Requisição executada com sucesso (success).|
| `403` | Requisição negada(Criptomoeda indisponivel, Valor de mms não permitido).|

## EndPoint
`http://198.211.114.165/pair/mms/?from=timsestamp&to=timestamp`
| Código | Descrição |
|---|---|
| `pair` | Permitido os valores `BRLBTC` e `BRLETH`.|
| `mms` | Permitido `20`, `50` e `200`.|
| `timestamp` | Permitido timestamp no formato Epoch `1617597886`.|

## Resultado
Response 200 (application/json)
```
[
 {
   "timestamp": 1610064000,
   "mms": 77733.80807
 },
]
```
## Incrementações Diárias
As incrementações diárias são feitas através de uma crontab que executa um management command do próprio django a cada 60 minutos

## Testes
Os testes são monitorados pelo Travis, foram feitos com django-test
