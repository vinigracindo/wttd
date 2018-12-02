# Eventex


Sistema de eventos encomendado pela Morena.

[![Code Health](https://landscape.io/github/Riverfount/wttd/master/landscape.svg?style=flat)](https://landscape.io/github/Riverfount/wttd/master)
[![Build Status](https://travis-ci.org/Riverfount/wttd.svg?branch=master)](https://travis-ci.org/Riverfount/wttd)
[![codecov](https://codecov.io/gh/Riverfount/wttd/branch/master/graph/badge.svg)](https://codecov.io/gh/Riverfount/wttd)
[![Updates](https://pyup.io/repos/github/Riverfount/wttd/shield.svg)](https://pyup.io/repos/github/Riverfount/wttd/)



## Como desenvolver?

1. Clone o repositório;
2. Instale as dependências com Pipenv;
3. Configure a instância de desenvolvimento com o _.env_;
4. Execute os testes.

```console
git clone git@github.com:Riverfount/wttd.git
cd wttd
pipenv install --dev
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy no Heroku?

1. Crie uma instância no Heroku;
2. Envie as configurações para o Heroku;
3. Defina uma SECRET_KEY para a instância;
4. Defina DEBUG=False;
5. Configure o serviço de e-mail;
6. Envie o código para o Heroku.

```console
heroku create minhainstancia
# Para executar o configu:push se necessário instale o plugin push do Heroku
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configuração do e-mail dependerá de sua instância no heroku
git push heroku master --force
```