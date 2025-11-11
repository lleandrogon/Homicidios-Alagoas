# Homicídios em Alagoas - Engenharia/Análise de Dados

## 📋 Sobre o Projeto
Este projeto realiza a análise de dados sobre homicídios no estado de Alagoas, utilizando Apache Airflow para orquestração do pipeline de dados, Pandas para processamento e Power BI para visualização dos dados.

## 🏗️ Estrutura do Projeto
Homicidios-Alagoas/
├── config/                # Arquivos de configuração
├── dags/                  # DAGs do Apache Airflow
├── logs/                  # Logs de execução
├── plugins/               # Plugins customizados do Airflow
├── volumes/               # Volumes de dados
└── docker-compose.yaml    # Orquestração de containers

## 🚀 Tecnologias Utilizadas
- Apache Airflow - Orquestração e agendamento do pipeline de dados
- Pandas - Processamento e transformação de dados
- Docker - Containerização da aplicação
- Docker Compose - Orquestração de múltiplos containers
- Power BI - Dashboard e visualização de dados

## 📊 Funcionalidades
- Coleta e processamento de dados sobre homicídios em Alagoas
- Pipeline de ETL (Extract, Transform, Load) automatizado
- Dashboard interativo no Power BI para análise dos dados
- Agendamento e monitoramento de tarefas via Airflow

## 🛠️ Pré-requisitos
- Docker
- Docker Compose

## ⚡ Instalação e Execução

```bash
# Clone o repositório
git clone <url-do-repositorio>
cd Homicidios-Alagoas

# Execute o projeto
docker-compose up -d

# Acesse o Airflow
# http://localhost:8080

# Execute o arquivo pbix no Power BI