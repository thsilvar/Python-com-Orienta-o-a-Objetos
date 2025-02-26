Projeto Alura

************************************************
- Criar Ambiente virtual

    python -m venv venv

************************************************

- Ativa Ambiente virtual

    Windows -> source venv/Scripts/activate

************************************************
- Ativa Ambiente virtual

    Windows -> deactivate

************************************************

- Instalar pacotes no python 

    pip install request

 
************************************************

- Vê os pacotes instalados 

    pip freeze   

************************************************

- Gerar arquivos onde vai ter todas as versões dos pacotes instalados

    pip freeze > requirements.txt

************************************************

- instalar FASTAPI

    pip install fastapi e pip install unicorn e rodar o freeze a cima.

************************************************

- iniciar o servidor fastapi

    uvicorn main:app --reload


-> O fast já vem com swagger só colocar /docs    