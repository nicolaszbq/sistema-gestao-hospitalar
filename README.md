# Sistema de Gestão Hospitalar

Trabalho final da disciplina de Estruturas de Dados — Tema 1 (Sistema de Gestão Hospitalar).

O sistema roda no terminal e usa as quatro estruturas estudadas na disciplina (Fila, Pilha, Lista e Árvore). Os dados ficam guardados no arquivo de texto `dados_sistema.txt`.

## Requisitos

- Python 3.8 ou superior (não usa nenhuma biblioteca externa, só `collections` e `os`, que já vêm com o Python).

## Como executar o sistema

1. Abra o terminal (Prompt de Comando ou PowerShell no Windows, Terminal no Linux/macOS).
2. Entre na pasta do projeto, onde está o arquivo `main.py`:

```bash
cd caminho/para/sistema-gestao-hospitalar
```

3. Execute o programa:

```bash
python main.py
```

> No Linux/macOS pode ser necessário usar `python3 main.py`.

4. Use o menu numérico para navegar:

| Opção | Menu | Estrutura |
|-------|------|-----------|
| 1 | Controle de Atendimentos — triagem de pacientes | Fila (FIFO) |
| 2 | Controle de Prontuários — prontuários acessados recentemente | Pilha (LIFO) |
| 3 | Controle de Pacientes — pacientes internados e leitos | Lista |
| 4 | Controle de Especialidades — especialidades e diagnósticos (casos) | Árvore |
| 5 | Salvar Dados — grava tudo em `dados_sistema.txt` | — |
| 6 | Sair — pergunta se deseja salvar antes de encerrar | — |

Cada controle tem as operações de inserir, remover, atualizar e consultar, respeitando a regra da sua estrutura.

## Estruturas de dados e justificativa técnica

### 1. Fila — Triagem de pacientes (FIFO)

**Estrutura utilizada:** `collections.deque`.

**Justificativa:** A triagem segue a ordem de chegada: o primeiro paciente a entrar é o primeiro a ser atendido (First-In, First-Out). A inserção acontece no fim da fila (`append`) e o atendimento/remoção no início (`popleft`). O `deque` foi escolhido no lugar da `list` porque remover do início de uma `list` obriga o Python a deslocar todos os outros elementos (O(n)), enquanto o `popleft` do `deque` é O(1).

O campo "prioridade" é apenas informativo: a ordem de atendimento continua sendo a ordem de chegada.

### 2. Pilha — Histórico de prontuários acessados (LIFO)

**Estrutura utilizada:** `list`.

**Justificativa:** O prontuário acessado por último é o primeiro que o médico precisa revisar (Last-In, First-Out). A inserção e a remoção acontecem sempre no topo, que é o final da lista (`append` e `pop`), as duas operações O(1). Na consulta, a pilha é exibida do topo para a base, com o topo marcado.

### 3. Lista — Pacientes internados e leitos ocupados

**Estrutura utilizada:** `list` de dicionários (`{"id", "nome", "leito", "status"}`).

**Justificativa:** O cadastro de internados não tem uma ordem obrigatória de entrada e saída: um paciente pode receber alta ou trocar de leito a qualquer momento. Por isso a lista é manipulada pela chave **ID** de cada paciente (gerada automaticamente), o que permite atualizar ou remover qualquer registro, sem a restrição de início/fim da fila e da pilha.

### 4. Árvore — Especialidades médicas e diagnósticos

**Estrutura utilizada:** classe `No`, em que cada nó tem um `nome` e uma lista `subcategorias` com os nós filhos.

**Justificativa:** Especialidades e diagnósticos são naturalmente hierárquicos. A árvore tem três níveis:

```
Clinica Geral            <- raiz
----Cardiologia          <- especialidade
     -Arritmia           <- caso / diagnóstico
----Ortopedia
     -Fratura
```

É possível cadastrar, renomear e remover especialidades e casos. Não são permitidos casos repetidos dentro da mesma especialidade, e a raiz "Clinica Geral" não pode ser renomeada nem removida. Remover uma especialidade remove também todos os casos dela.

## Persistência de dados

Todo o estado do sistema é salvo em um único arquivo de texto, `dados_sistema.txt`, usando o delimitador pipe (`|`). Não são usados bancos de dados, JSON, CSV ou bibliotecas de serialização como `pickle`.

- **Em memória:** as operações de inserir, atualizar e remover alteram apenas as estruturas em memória (`deque`, `list` e árvore). O arquivo não é modificado durante o uso.
- **Salvar:** a opção **5 — Salvar Dados** do menu principal exporta o estado atual de todas as estruturas para o arquivo (`salvar_dados()`), sobrescrevendo o conteúdo anterior. Ao escolher **6 — Sair**, o programa pergunta se o usuário deseja salvar antes de encerrar, para evitar perder alterações.
- **Carregar:** ao iniciar, o programa verifica se `dados_sistema.txt` existe. Se existir, reconstrói as estruturas a partir dele (`carregar_dados()`); se não existir, começa vazio. O arquivo só é criado quando algum dado é salvo.
- O caractere `|` é removido do que o usuário digita, para não quebrar o formato do arquivo.

Formato de cada linha (o primeiro campo identifica a estrutura):

```
FILA|205|Roberto Alves|Prioridade Alta
PILHA|PRONT-889|Paciente 101|Consulta Cardiologia
LISTA|101|Carlos Silva|Leito 04|Estavel
ARVORE|Clinica Geral|Cardiologia|Arritmia
ARVORE|Clinica Geral|Ortopedia
```

A última linha mostra uma especialidade sem nenhum caso cadastrado: ela é gravada sem o último campo.
