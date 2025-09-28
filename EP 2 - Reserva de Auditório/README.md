# EP2 - Sistema de Gerenciamento e Análise de Reservas de Auditório (ICCD/USP)

Este projeto, desenvolvido como o segundo Exercício-Programa (EP2) da disciplina Introdução à Ciência da Computação e Dados (ICC) da USP, consiste em um sistema em **Python** para o gerenciamento e análise de dados de reservas de um auditório fictício.

O sistema opera sobre um conjunto de dados (`.csv`) contendo informações detalhadas sobre as reservas e oferece um menu interativo para diversas operações de consulta e análise.

## 🚀 Funcionalidades

O programa principal (`main()`) apresenta um menu de operações que permite ao usuário interagir com os dados das reservas:

1.  **Listar todas as reservas:** Exibe todas as informações de cada reserva (ID, Solicitante, Datas, Valores, etc.).
2.  **Filtrar por categoria:** Lista as reservas de uma categoria específica, **USP** ou **Externo**.
3.  **Calcular total arrecadado:** Calcula e exibe o valor total arrecadado para cada categoria de solicitante (USP e Externo).
4.  **Exibir estatísticas gerais:**
    * Calcula a **média de diárias** por reserva.
    * Calcula o **percentual de reservas com desconto**.

## 🛠️ Detalhes da Implementação

* **Linguagem:** Python
* **Estrutura de Dados:** Utilização de uma lista de listas para armazenar e manipular os dados do arquivo CSV, conforme a especificação.
* **Modularização:** O código é estruturado em funções dedicadas (`listar_reservas`, `filtrar_por_categoria`, `calcular_total_arrecadado`, `exibir_estatisticas`) para promover boas práticas de programação.
* **Análise de Dados:** Implementação de lógica para cálculo de diferenças entre datas (número de diárias) e operações financeiras (cálculo de arrecadação e percentuais de desconto).

## 📄 Estrutura do Repositório

* `ep2.py`: Arquivo principal contendo a implementação de todas as funções do sistema.
* `Enunciado_EP2.pdf`: O arquivo original do enunciado do Exercício-Programa (incluído para referência).
* *`(outros arquivos, como esqueleto_EP2.py, se aplicável)`*

---

Este projeto demonstra a aplicação de conceitos fundamentais de programação, como funções, estruturas de repetição e manipulação de listas, em um contexto de processamento e análise básica de dados.
