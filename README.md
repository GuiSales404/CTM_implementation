
# CTM_Implementation 🚀  

Implementação experimental da **Conscious Turing Machine (CTM)** baseada na teoria proposta por Manuel e Lenore Blum.  

📌 **Objetivo**  
Este projeto explora a modelagem computacional da consciência, avaliando a CTM em tarefas de **raciocínio lógico** e **inferência narrativa**, utilizando conjuntos de dados como **bAbI Toy Tasks** e **RocStories**.  

📚 **Referência Teórica**  
A **CTM** é inspirada na **Global Workspace Theory (GWT)** e modela processos **conscientes** e **inconscientes** em uma estrutura computacional. Mais detalhes podem ser encontrados no artigo:  
📄 [Avaliação da Capacidade Computacional e Representação de Consciência de uma Conscious Turing Machine](https://doi.org/10.1145/nnnnnnn.nnnnnnn)  

---

## 🔧 **Instalação**  
Antes de rodar o código, instale as dependências necessárias:  

```bash
git clone https://github.com/GuiSales404/CTM_implementation.git  
cd CTM_implementation  
pip install -r requirements.txt  
```
---

## 🚀 **Uso**  

### **Exemplo de Teste com a CTM**
```python
from CTM import CTM  
import os  
import pandas as pd  
import random  

def select_random(lista, quantidade=5):
    return random.sample(lista, quantidade)  

# Carregar um conjunto de tarefas para avaliação  
tasks = select_random(os.listdir("tasks/babi-tasks/test"), 1)  

for task in tasks:
    with open(f"tasks/babi-tasks/test/{task}") as f:
        task_content = f.read()  

    # Processamento da CTM
    story = [line.split("\t")[0] for line in task_content.split("\n") if "?" not in line]
    ctm = CTM(8, story)  
    ctm.run()  

    # Exibir Resultados  
    print(f"Resultados da tarefa {task} armazenados!")  
```

---

## 📊 **Experimentos**
Foram conduzidos testes com dois conjuntos de dados:  
📌 **bAbI Toy Tasks** – Avaliação de inferência lógica e aprendizado contextual  
📌 **RocStories** – Inferência narrativa e compreensão de histórias  

🔍 **Resultados**  
- A CTM apresentou desempenho comparável a modelos individuais de linguagem, com maior interpretabilidade.  
- O custo computacional foi maior do que modelos convencionais de IA.  

🔗 **Detalhes e gráficos disponíveis no artigo.**  

---

## 🤝 **Contribuindo**
💡 Quer melhorar o projeto?  
1. Faça um **fork** do repositório  
2. Crie um **branch** para sua feature (`git checkout -b minha-feature`)  
3. Submeta um **pull request** 🚀  

---

## 📄 **Licença**
Este projeto é distribuído sob a licença **MIT**.  