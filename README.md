# Sistema de Gestão Hospitalar

Trabalho final da disciplina de Estruturas de Dados — Tema 1 (Sistema de Gestão Hospitalar).

## Como executar o sistema

1. Abra o terminal (prompt de comando ou PowerShell no Windows).
2. Navegue até a pasta do projeto:

```bash
cd \sistema-gestao-hospitalar
```

3. Execute o programa:

```bash
python main.py
```

4. Utilize o menu numérico para navegar entre as abas:
   - (1) Controle de Atendimentos — Fila de triagem (FIFO)
   - (2) Controle de Prontuários — Pilha de prontuários médicos (LIFO)
   - (3) Controle de Pacientes — Lista de pacientes internados
   - (4) Controle de Especialidades — Árvore de especialidades e diagnósticos
   - (5) Sair

Os dados são salvos automaticamente no arquivo `dados_sistema.txt` a cada operação de inclusão, atualização ou remoção.

## Estrutura de dados escolhida e justificativa técnica

O projeto implementa as quatro estruturas fundamentais estudadas na disciplina, cada uma desempenhando seu papel operacional no contexto hospitalar:

### 1. Fila — Atendimento/Triagem de pacientes (FIFO)

**Estrutura utilizada:** `collections.deque` da biblioteca padrão do Python.

**Justificativa:** A triagem hospitalar segue estritamente a ordem de chegada: o primeiro paciente a ser cadastrado deve ser o primeiro a ser atendido. Isso é o comportamento clássico de uma Fila (First-In, First-Out). A operação de inserção ocorre no final da fila (`append`) e a remoção/atendimento ocorre no início (`popleft`), respeitando a regra de atendimento sequencial e justo dos pacientes.

### 2. Pilha — Histórico de prontuários médicos acessados (LIFO)

**Estrutura utilizada:** `list` nativa do Python.

**Justificativa:** Os prontuários acessados recentemente precisam ser revisados rapidamente, sendo o último prontuário acessado o primeiro a ser exibido para consulta ou correção. Esse comportamento é o de uma Pilha (Last-In, First-Out). A inserção e a remoção ocorrem sempre no topo da pilha (`append` e `pop`), permitindo acesso rápido ao último registro manipulado.

### 3. Lista — Cadastro dinâmico de pacientes internados e leitos ocupados

**Estrutura utilizada:** `list` de dicionários.

**Justificativa:** O cadastro de pacientes internados exige manipulação por índice ou chave (busca por nome, atualização de leito e status, remoção por alta). Uma lista permite inserção dinâmica no final, consulta de todos os internados, atualização de campos específicos e exclusão de pacientes que deram alta, sem a rigidez de ordem imposta por filas ou pilhas.

### 4. Árvore — Indexação hierárquica de especialidades médicas e diagnósticos clínicos

**Estrutura utilizada:** Classe `No` com lista de subcategorias (árvore de dicionários/nós aninhados).

**Justificativa:** As especialidades médicas e seus diagnósticos possuem naturalmente uma organização hierárquica (ex: Clínica Geral → Cardiologia → Arritmia). Uma árvore permite representar essa relação pai-filho de forma clara, suportando navegação por níveis, cadastro de subcategorias e diagnósticos, além de consultas organizadas por especialidade.

## Persistência de dados

Todo o estado do sistema é salvo em um único arquivo de texto chamado `dados_sistema.txt`, utilizando o delimitador pipe (`|`). Não são utilizados bancos de dados, JSON, CSV ou bibliotecas de serialização como `pickle`.

Exemplo do formato do arquivo:

```
FILA|205|Roberto Alves|Prioridade Alta
PILHA|PRONT-889|Paciente 101|Consulta Cardiologia
LISTA|101|Carlos Silva|Leito 04|Estavel
ARVORE|Clinica Geral|Cardiologia|Arritmia
```

O arquivo é lido automaticamente ao iniciar o programa (`carregar_dados()`) e sobrescrito a cada operação de escrita (`salvar_dados()`).
