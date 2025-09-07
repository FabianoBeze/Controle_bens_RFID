# Controle de Bens com RFID

Este projeto é um sistema simples para controle de bens utilizando tecnologia RFID, com cadastro de usuários, bens, antenas e registro de movimentações. Ideal para ambientes como escolas, laboratórios ou empresas.

## Funcionalidades

- **Cadastro de bens:** Registre bens com RFID, nome, local e responsável.
- **Cadastro de usuários:** Professores e técnicos podem ser cadastrados.
- **Cadastro de antenas:** Registre antenas/leitores RFID e seus locais.
- **Movimentação de bens:** Registre a movimentação dos bens entre locais.
- **Relatórios:** Emita relatórios de movimentação dos bens.
- **Permissões:** Apenas administradores podem cadastrar e editar dados.

## Estrutura dos arquivos

- `main.py` — Menu principal e lógica do sistema.
- `bem.py` — Classe Bem.
- `usuario.py` — Classe Usuario.
- `administrador.py` — Classe Administrador.
- `antena.py` — Classe Antena.

## Como executar

1. Certifique-se de ter o Python instalado.
2. Coloque todos os arquivos na mesma pasta.
3. Execute o sistema pelo terminal:

```shell
python main.py
```

## Exemplo de uso

- Faça login como administrador.
- Cadastre bens, usuários e antenas.
- Registre movimentações dos bens.
- Consulte relatórios de movimentação.

## Observações

Este sistema é um protótipo e pode ser expandido para incluir persistência em banco de dados, interface gráfica, autenticação avançada,