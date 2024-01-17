# Transport 

A idéia desse micro-serviço é uma construçāo de uma aplicaçāo de transporte feito em python, para a construçāo de um 
artigo sobre SAGA.

## 🚀 Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

Consulte **[Implantação](#-implanta%C3%A7%C3%A3o)** para saber como implantar o projeto.

### 📋 Pré-requisitos

Quais sāo os pré-requisitos para rodar o projeto ?

```
Python
PIP
PyMongo
Fast-API
```

### 🔧 Instalação

Ao executar efetuar a instalaçāo dos pré-requisitos, será necessario executar a seguinte etapa:

Diga como essa etapa será:

```
configurar as variaveis, dentro do arquivo .env
DB_URI
DB_NAME
```
Para criar a imagem rode o seguinte comando 

``
 docker build ./ -t transportservices 
``

Para executar a aplicaçāo estamos usando a porta 8001

``
 docker run -d -p 8001:8001 --name transportservicesapi transportservices
``

## ⚙️ Executando 

Para executar a aplicaçāo rode o seguinte comando


```
python -m uvicorn main:app --reload

```

### 🔩 Analise os testes de ponta a ponta

Explique que eles verificam esses testes e porquê.

```
Dar exemplos
```

### ⌨️ E testes de estilo de codificação

Explique que eles verificam esses testes e porquê.

```
Dar exemplos
```


## 🛠️ Construído com

Mencione as ferramentas que você usou para criar seu projeto

* [FastAPI](https://fastapi.tiangolo.com/tutorial/) - O framework web usado
* [PyMongo](https://pymongo.readthedocs.io/en/stable/) - Framework de conexāo com o Banco de Dados
* [PiP](https://pypi.org/project/pip/) - Usada para controlar dempedencias
* [Uvicorn](https://fastapi.tiangolo.com/deployment/manually/) - Servidor de Aplicaçāo
* 

## 🖇️ Colaborando

Por favor, leia o [COLABORACAO.md](https://gist.github.com/usuario/linkParaInfoSobreContribuicoes) para obter detalhes sobre o nosso código de conduta e o processo para nos enviar pedidos de solicitação.

## 📌 Versão

Nós usamos [SemVer](http://semver.org/) para controle de versão. Para as versões disponíveis, observe as [tags neste repositório](https://github.com/suas/tags/do/projeto). 

## ✒️ Autores

Mencione todos aqueles que ajudaram a levantar o projeto desde o seu início

* **Weberton Ferreira** - *Trabalho Inicial* - [Jose Augusto](https://github.com/ribeiry)

## 📄 Licença

Este projeto está sob a licença (sua licença) - veja o arquivo [LICENSE.md](https://github.com/usuario/projeto/licenca) para detalhes.

## 🎁 Expressões de gratidão

* Conte a outras pessoas sobre este projeto 📢;
* Convide alguém da equipe para uma cerveja 🍺;
* Um agradecimento publicamente 🫂;