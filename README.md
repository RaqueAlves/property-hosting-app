# Sistema de Aluguel de Imóveis de Temporada

Este projeto implementa um sistema para o gerenciamento de aluguel de imóveis de temporada, desenvolvido em Python. O sistema permite o cadastro de imóveis, usuários (locadores e locatários), reservas, e avaliações. A aplicação também valida a disponibilidade das datas de locação para impedir a sobreposição de reservas.

## Funcionalidades

### Usuários
- Cadastro de dois tipos de usuários: **Locadores (proprietários)** e **Locatários (clientes)**.
- Cada usuário possui: nome, e-mail e tipo (locador ou locatário).

### Imóveis
- Cadastro de imóveis por locadores.
- Informações de cada imóvel: título, descrição, endereço, valor da diária, disponibilidade e reservas.
- Filtro de imóveis por: localização, faixa de preço e intervalo de datas disponíveis.

### Reservas
- Locatários podem solicitar a reserva de um imóvel por um período (data de entrada e saída).
- O sistema valida a disponibilidade do imóvel no intervalo de datas solicitado.
- Locadores podem aprovar ou recusar as reservas solicitadas.

### Avaliações
- Locatários podem avaliar o imóvel com uma nota (1 a 5) e um comentário após a estadia.

## Requisitos

- **Python 3.8+**
- **Bibliotecas necessárias**:
  - `datetime`
  - `json`
  - `uuid`

## Como rodar o projeto

1. Clone este repositório:
    ```bash
    git clone https://github.com/RaqueAlves/sistema_de_locacao_de_imoveis.git
    ```
2. Acesse o diretório do projeto:
    ```bash
    cd sistema_de_locacao_de_imoveis
    ```
3. Execute o arquivo principal para rodar o sistema:
    ```bash
    python main.py
    ```
