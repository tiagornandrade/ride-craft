# RideCraft

**RideCraft** é um projeto de estudo que busca entender o **System Design** de plataformas de mobilidade sob demanda, inspirando-se em conceitos de sistemas como o da Lyft. Esse projeto explora a construção de uma arquitetura orientada a eventos, utilizando microserviços e bancos de dados relacionais, com geração de dados sintéticos para simular cenários reais de transporte urbano.

## Objetivo do Projeto

O objetivo do **RideCraft** é simular e compreender os componentes de um sistema de transporte sob demanda:
- Gerenciamento de corridas, motoristas e passageiros.
- Orientação a eventos com comunicação assíncrona.
- Integração com banco de dados para armazenamento e consultas.
- API Gateway para controlar e rotear requisições.
- Geração de dados sintéticos para testes e simulações.

## Tecnologias Utilizadas

- **Python** (FastAPI) — Construção da API e dos microserviços.
- **Apache Kafka** — Mensageria para comunicação assíncrona entre serviços.
- **PostgreSQL** — Banco de dados relacional para persistência.
- **Redis** — Cache para armazenar dados em tempo real, como localização dos motoristas.
- **Docker** e **Docker Compose** — Orquestração dos containers para fácil deploy dos serviços.
- **Faker** — Biblioteca para geração de dados sintéticos (passageiros, motoristas, localizações, etc).

## Arquitetura

RideCraft adota uma arquitetura de microserviços orientada a eventos:

- **API Gateway** — Centraliza e distribui as requisições para os serviços.
- **Serviço de Corridas (Ride Service)** — Gerencia a criação e o status das corridas.
- **Serviço de Localização (Location Service)** — Processa dados de localização de motoristas em tempo real.
- **Serviço de Preço (Pricing Service)** — Calcula o valor estimado das corridas com base em distância e outros fatores.
- **Mensageria (Kafka)** — Utilizada para troca de mensagens entre os serviços, garantindo escalabilidade e comunicação eficiente.

![Architecture Diagram](path/to/architecture-diagram.png)

> **Nota**: A arquitetura acima usa mensagens entre os microserviços via Kafka para manter o sistema desacoplado e responsivo.

## Recursos Extras

- **Autenticação JWT**: Segurança para verificar autenticação em cada requisição usando tokens JWT.
- **Proxy Reverso com NGINX**: NGINX roteia as requisições para o API Gateway e prepara o ambiente para balanceamento de carga futuro.
- **Monitoramento com Prometheus e Grafana**: Coleta de métricas para monitoramento e visualização em tempo real.
- **Documentação Swagger**: Endpoints documentados automaticamente com Swagger, acessíveis em `/docs`.

## Instalação e Configuração

...

### Integração com NGINX e Monitoramento

Após configurar e executar o ambiente com `docker-compose up`, acesse:

- **Swagger**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **Grafana**: [http://localhost:3000](http://localhost:3000)
  - **Credenciais padrão**: `admin` / `admin`
- **Prometheus**: [http://localhost:9090](http://localhost:9090)

### Autenticação JWT

Para acessar as rotas protegidas, adicione um token JWT no cabeçalho `Authorization: Bearer <TOKEN>`.

## Configuração e Instalação

### Pré-Requisitos

- **Docker** e **Docker Compose** devem estar instalados.
- **Python 3.9+**

### Passo a Passo

1. Clone o repositório:

   ```bash
   git clone https://github.com/tiagornandrade/ridecraft.git
   cd ridecraft
   ```

2. Configure variáveis de ambiente:

   Crie um arquivo `.env` com as variáveis de configuração para conectar aos serviços. Por exemplo:

   ```env
   KAFKA_BROKER_URL=kafka:9092
   POSTGRES_USER=ridecraft_user
   POSTGRES_PASSWORD=securepassword
   POSTGRES_DB=ridecraft_db
   ```

3. Execute o ambiente com Docker Compose:

   ```bash
   docker-compose up --build
   ```

   Esse comando inicializa o ambiente com todos os serviços — API Gateway, microserviços, Kafka, Redis e PostgreSQL.

4. Acesse a documentação da API:

   O **FastAPI** gera uma documentação automática dos endpoints, disponível em: [http://localhost:8000/docs](http://localhost:8000/docs).

## Estrutura de Pastas

```plaintext
project-root/
│
├── gateway/                   # API Gateway
│   ├── main.py                # Código principal do API Gateway
│   ├── config.py              # Configurações do Gateway
│   └── routers/               # Definição dos endpoints e rotas
│       ├── rides.py           # Endpoints relacionados a corridas
│       ├── drivers.py         # Endpoints para motoristas
│       └── pricing.py         # Endpoints de preços
│
├── ride_service/              # Serviço de gestão de corridas
├── location_service/          # Serviço de localização
├── pricing_service/           # Serviço de cálculo de preços
└── docker-compose.yml         # Configuração para subir o ambiente
```

## Exemplos de Uso

### Criar uma Corrida

Envie uma solicitação POST para o endpoint `/rides/` para criar uma nova corrida. Exemplo de payload:

```json
{
  "passenger_id": "12345",
  "pickup_location": {"lat": -23.563, "long": -46.654},
  "dropoff_location": {"lat": -23.565, "long": -46.656}
}
```

### Consultar Status de uma Corrida

Envie uma solicitação GET para `/rides/{ride_id}` para obter o status de uma corrida em andamento.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## Licença

Este projeto é licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais informações.
