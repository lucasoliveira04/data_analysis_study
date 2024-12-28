### **O que é Pandas?**
Pandas é uma biblioteca essencial no ecossistema Python, projetada para análise e manipulação de dados. Ela oferece estruturas como `DataFrame` (tabelas) e `Series` (colunas ou dados unidimensionais), que permitem trabalhar com dados de maneira intuitiva e eficiente. É amplamente utilizada para:  
- **Leitura e escrita** de dados em formatos como CSV, Excel, HTML, JSON.  
- **Transformação e limpeza** de dados.  
- **Análise estatística e filtragem** de grandes volumes de dados.  

---

### **Funcionalidades Básicas**

#### **Leitura de Arquivos**
- **`read_excel`**: Lê arquivos Excel (.xlsx).  
  Exemplo:  
  ```python
  df = pd.read_excel('arquivo.xlsx')
  ```
- **`read_csv`**: Lê arquivos CSV.  
  Exemplo:  
  ```python
  df = pd.read_csv('arquivo.csv')
  ```
- **`read_html`**: Lê tabelas diretamente de arquivos ou URLs HTML.  
  Exemplo:  
  ```python
  df = pd.read_html('pagina.html')[0]
  ```

---

#### **Visualizando Informações do DataFrame**
- **`info`**: Retorna um resumo sobre as colunas, tipos de dados e valores nulos.  
  ```python
  df.info()
  ```
- **`head`**: Mostra as primeiras 5 linhas do DataFrame.  
  ```python
  df.head()
  ```
- **`tail`**: Mostra as últimas 5 linhas.  
  ```python
  df.tail()
  ```
- **`shape`**: Mostra o tamanho do DataFrame (linhas, colunas).  
  ```python
  df.shape
  ```
- **`columns`**: Retorna os nomes das colunas.  
  ```python
  df.columns
  ```
- **`index`**: Retorna os rótulos do índice (linhas).  
  ```python
  df.index
  ```

---

### **Filtrando Dados**

#### **Com `loc`**  
Usado para selecionar linhas ou colunas com base nos rótulos (nomes).  
- **Exemplo 1**: Filtrar linha pelo índice:  
  ```python
  df.loc[2]
  ```
- **Exemplo 2**: Filtrar uma célula específica (linha e coluna):  
  ```python
  df.loc[2, 'Coluna']
  ```
- **Exemplo 3**: Filtrar um intervalo de linhas e colunas:  
  ```python
  df.loc[1:3, ['Coluna1', 'Coluna2']]
  ```

---

#### **Com `iloc`**  
Seleciona dados por posições inteiras (índices).  
- **Exemplo 1**: Selecionar uma linha pelo índice:  
  ```python
  df.iloc[0]
  ```
- **Exemplo 2**: Selecionar uma célula específica:  
  ```python
  df.iloc[0, 1]
  ```
- **Exemplo 3**: Selecionar intervalo de linhas e colunas:  
  ```python
  df.iloc[0:3, 1:3]
  ```

---

#### **Com `query`**  
Filtra linhas com base em expressões booleanas.  
- **Exemplo**: Filtrar onde a coluna 'Idade' é maior que 25.  
  ```python
  df.query('Idade > 25')
---