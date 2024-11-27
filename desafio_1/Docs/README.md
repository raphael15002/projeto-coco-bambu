# Desafio Engenharia de Dados - Coco Bambu 2024

## **Descrição do Projeto**
Este projeto foi desenvolvido como parte do processo seletivo para a posição de **Engenheiro de Dados** da rede de restaurantes **Coco Bambu**. O objetivo é criar um pipeline de **ETL (Extração, Transformação e Carga)** para processar e armazenar dados extraídos de um arquivo JSON.

### **Objetivo**
- **Transformação**: Processar os dados no formato desejado.
- **Carga**: Armazenar os dados processados em um banco de dados SQL.

---

## **Funcionalidades**
- **Extração de Dados**: O projeto utiliza um arquivo json.
- **Processamento e Transformação**: Utiliza **pandas** para processar os dados extraídos.
- **Armazenamento em Banco de Dados**: Usa **SQLAlchemy** para armazenar os dados no banco de dados.
- **Docker** cria uma  instância do mysql em um container para que o ambiente seja replicavel com as mesmas condiçoes em qualquer sistema.
- 

---

## **Tecnologias Usadas**
- **Python 3.x**
- **pandas**: Para manipulação e análise de dados.
- **requests**: Para fazer chamadas de API e obter dados.
- **SQLAlchemy**: Para interagir com bancos de dados SQL.
- **pytest**: Para testes automatizados.
- **Docker**: Para criação do banco e automatização dos scripts.

---
** Mudar o o filepath do transformacao_json.py para o do seu computador.**  
** Subir o docker-compose antes de rodar os scripts.**

