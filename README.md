# 📊 Dashboard de Análise de Dados - John Deere

Projeto de análise de dados desenvolvido como parte de uma iniciativa pessoal para a visita à empresa John Deere. O objetivo foi cruzar dados de **área plantada** e **rendimento agrícola** para gerar insights relevantes de forma visual e acessível.

---

## 🧰 Tecnologias e Ferramentas Utilizadas

- Python (Pandas)
- Power BI
- Excel
- Jupyter Notebook
- CSV

---

## 🚀 Como Executar o Projeto

### 1. Clonar o repositório
```bash
git clone https://github.com/gmalisse/area-plantada-vs-rendimento.git
```

### 2. Abrir o Jupyter Notebook

Abra o arquivo `tratamento/tratamento_tabelas.ipynb` para visualizar o tratamento de dados feito com Python e Pandas.

### 3. Abrir o Dashboard no Powwer BI

Use o arquivo `area_plantada_x_rendimento.pbix` no Power BI Desktop para visualizar os gráficos.

---

## 🛠️ Etapas do Projeto

1. **Extração de Dados**  
   Os dados foram obtidos a partir do site oficial do [SIDRA/IBGE](https://sidra.ibge.gov.br/tabela/1612). Foram selecionadas e baixadas no formato CSV as seguintes tabelas para os anos de 1988 a 2023:
   - Área plantada (ha)
   - Rendimento médio da produção (kg/ha) 
   Todas referentes às principais lavouras do país.

2. **Pré-processamento no Excel**  
   Os arquivos CSV foram abertos no Excel para pequenas correções manuais, como:
   - Substituição de caracteres especiais: `ã` por `a` e `ç` por `c`.

3. **Tratamento de Dados com Python (Pandas)**  
   Os dados foram tratados e limpos utilizando a biblioteca `pandas`, com foco em:
   - Padronização de colunas
   - Conversão de tipos
   - Remoção de dados inconsistentes

4. **Importação e Modelagem no Power BI**  
   Os arquivos CSV tratados foram carregados no Power BI para construção do modelo de dados e visualizações.

5. **Unificação das Tabelas de Fato**  
   Como as três tabelas possuiam colunas em comum (cultura, UF, ano), foi realizada uma junção (INNER JOIN) entre elas no Power Query, criando uma tabela fato única. As tabelas originais foram desabilitadas da carga para otimização do modelo.

6. **Criação de Tabelas Dimensão**  
   Foram criadas tabelas dimensão diretamente no Power BI para segmentar e organizar as informações, como:
   - Dimensão de Culturas
   - Dimensão de Unidades da Federação
   - Dimensão de Período  
   O uso de SQL foi descartado neste caso, pois o volume de dados não exigia um banco de dados relacional robusto.

7. **Modelagem em Estrela**  
   O modelo de dados foi estruturado no formato estrela (Star Schema), com relacionamentos 1:N entre as tabelas dimensão e a tabela fato, garantindo melhor desempenho e facilidade na manutenção e expansão do projeto.

8. **Criação do Dashboard no Power BI**  
   Com os dados tratados e o modelo relacional estruturado, foram desenvolvidas visualizações interativas no Power BI para facilitar a análise dos dados. O dashboard foi construído com foco em:
   - Clareza visual e facilidade de interpretação
   - Comparações entre culturas, estados e anos
   - Identificação de padrões como alta produção com baixo rendimento ou vice-versa  
   Foram utilizados gráficos de colunas, linhas, mapas e segmentações para tornar a análise intuitiva e acessível mesmo para quem não tem familiaridade com os dados.

   
---

