

---

# Trabalho de Grafos: Caminhos Mínimos e Algoritmos Clássicos

## 👥 Alunos

- **Diogo Torres** – responsável por explicar o projeto e o código
- **Marcos Carvalho** – apresentará os pontos teóricos e o funcionamento dos algoritmos
- **Thiago Saggiorato** – apresentará os pontos teóricos e o funcionamento dos algoritmos

---

## ✨ Objetivo

Este projeto tem como objetivo analisar e implementar três algoritmos clássicos de caminho mínimo em grafos:

- Dijkstra
- Bellman-Ford
- Floyd-Warshall

Foram realizados:

- Testes manuais com um grafo baseado em cidades reais da região de Cascavel-PR
- Implementação computacional em Python com medições de desempenho
- Comparativo entre os algoritmos em grafos de pequeno e médio porte

---

## 1. Parte Teórica (Manual)

### 📍 Grafo manual utilizado

O grafo possui 10 vértices representando cidades reais dentro de um raio de 100 km de Cascavel (PR):

Cidades:

- **CA**: Cascavel
- **ST**: Santa Tereza do Oeste
- **CO**: Corbélia
- **LI**: Lindoeste
- **TO**: Toledo
- **CT**: Catanduvas
- **ME**: Medianeira
- **MT**: Matelândia
- **AS**: Assis Chateaubriand
- **MR**: Marechal Cândido Rondon

As arestas foram mapeadas com base em ligações viárias reais entre essas cidades.



### 🧮 Resolução Manual

Para o par de vértices **CA → MR**, aplicamos:

#### a) Algoritmo de Dijkstra

- Utiliza uma fila de prioridade para explorar o caminho mínimo a cada passo.
- Requer que todos os pesos sejam positivos.
- Garante a menor distância com ótima performance.



#### b) Algoritmo de Bellman-Ford

- Permite pesos negativos.
- Executa **V-1** ciclos de relaxamento sobre todas as arestas.
- Detecta ciclos negativos ao final.



#### c) Algoritmo de Floyd-Warshall

- Usa matriz de distâncias e faz comparações de todos os pares de vértices.
- Ideal para quando se precisa dos caminhos mínimos entre todos os pares.



### 🧾 Passo a Passo Manual

- Tabelas de atualização de distâncias e predecessores foram preenchidas manualmente.
- A matriz de adjacência inicial e a matriz de distâncias final foram comparadas.

### ⚖️ Comparativo Manual

| Algoritmo      | Vantagem                             | Limitação                               |
| -------------- | ------------------------------------ | --------------------------------------- |
| Dijkstra       | Rápido para pesos positivos          | Não suporta pesos negativos             |
| Bellman-Ford   | Aceita pesos negativos               | Mais lento que Dijkstra                 |
| Floyd-Warshall | Calcula todos os caminhos de uma vez | Complexidade computacional alta (O(V³)) |

---

## 2. Parte Computacional (Python)

### 🧱 Estrutura do Projeto

O projeto segue uma arquitetura modular inspirada em práticas do Spring:

```
graph_shortest_paths/
├─ domain/           # Modelos puros: Grafo, Fábricas
├─ application/      # Implementações dos algoritmos
├─ infrastructure/   # Exportadores, Logger, Medição
├─ interfaces/       # CLI, integração externa
├─ scripts/          # Automação e benchmarking
├─ tests/            # Pytest automatizado
└─ docs/             # Gráficos e resultados exportados
```

### 🛠️ Tecnologias utilizadas

- **Python 3.11+**
- **pytest** (testes automatizados)
- **matplotlib** (visualização gráfica)
- **csv/json** (exportação de dados)

### 📐 Algoritmos implementados

#### Dijkstra

- Baseado em lista de adjacência e `heapq`.
- Garante melhor caminho se pesos forem positivos.
- Complexidade: **O((V + E) log V)**

#### Bellman-Ford

- Itera sobre todas as arestas V-1 vezes.
- Suporta pesos negativos e detecta ciclos negativos.
- Complexidade: **O(V·E)**

#### Floyd-Warshall

- Usa matriz de distâncias.
- Calcula todos os pares de vértices.
- Complexidade: **O(V³)**

### 🧪 Grafos utilizados

- **Pequeno:** 10 vértices (grafo da parte manual)
- **Médio:** 12 vértices (adicionando Quatro Pontes e Braganey)

### 📤 Exportação de Resultados

- Arquivos `.csv` e `.json` com os caminhos mínimos para cada algoritmo:
  - `docs/resultados/dijkstra_pequeno.csv`
  - `docs/resultados/bellman-ford_medio.json`
- Gráfico comparativo salvo como:
  - `docs/timing.png`

### 🚀 Execução

```bash
python -m graph_shortest_paths
```

Este comando executa todos os algoritmos, exporta os resultados e executa os testes automaticamente.

---

## 3. O que é e como funciona cada algoritmo

### 🔍 Dijkstra

Dijkstra é um algoritmo guloso que sempre expande o caminho com menor custo conhecido até o momento. Ele assume que todos os pesos das arestas são não-negativos. Ideal para redes de transporte, GPS, jogos, etc.

**Pontos-chave:**

- Rápido e eficiente
- Inadequado para pesos negativos
- Usa `heapq` para otimizar busca

### 🔍 Bellman-Ford

Permite pesos negativos e detecta ciclos negativos. Funciona bem em ambientes onde há custos variáveis (ex: taxas financeiras, links de rede com penalizações).

**Pontos-chave:**

- Mais lento
- Seguro para pesos negativos
- Executa V-1 relaxamentos

### 🔍 Floyd-Warshall

Ideal para obter **todos os caminhos mínimos entre todos os pares** de vértices. Muito usado em análise de redes, jogos, planejamento de rotas, etc.

**Pontos-chave:**

- Simples de implementar
- Custo alto: O(V³)
- Baseado em programação dinâmica

---

## 4. Apresentação Oral

### 📋 Divisão de tópicos

- **Diogo Torres**: Explicação do projeto, estrutura de pastas e organização do código
- **Marcos Carvalho**: Apresentação do grafo, resolução manual, conceitos de grafos
- **Thiago Saggiorato**: Funcionamento dos algoritmos, comparativo técnico e gráfico final

---

## 📦 Arquivos Entregues

- Código: `graph_shortest_paths/`
- Executável: `python -m graph_shortest_paths`
- Resultados exportados: `docs/resultados/*.csv`, `.json`
- Gráfico: `docs/timing.png`
- Relatório final: `docs/RELATORIO.pdf`

---

## 🏁 Conclusão

Este projeto possibilitou uma imersão completa no estudo de grafos e algoritmos de caminhos mínimos, tanto manualmente quanto de forma computacional.

**Aprendizados:**

- Diferenças entre algoritmos de caminhos mínimos
- Aplicações práticas e desempenho computacional
- Estruturação de projetos modulares em Python

**Destaques dos algoritmos:**

| Algoritmo      | Ideal para...                                  |
| -------------- | ---------------------------------------------- |
| Dijkstra       | Sistemas com pesos positivos (GPS, jogos)      |
| Bellman-Ford   | Ambientes com possibilidade de pesos negativos |
| Floyd-Warshall | Redes e sistemas que exigem todos os pares     |


