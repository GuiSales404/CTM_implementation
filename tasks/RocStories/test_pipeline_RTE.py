from CTM import CTM 
import warnings
warnings.filterwarnings('ignore')
import os
import random
import pandas as pd
os.environ["TOKENIZERS_PARALLELISM"] = "false"
import re
from time import sleep

def select_random(lista, quantidade=5):
    if len(lista) < quantidade:
        raise ValueError("A lista deve conter pelo menos {} elementos.".format(quantidade))
    return random.sample(lista, quantidade)

def extract_answers(conteudo):
    padrao = r"### Respostas Completas:\s*(\d+|\[.*?\])"
    match = re.search(padrao, conteudo, re.DOTALL)

    if match:
        respostas = match.group(1).strip()# Converte a string da lista para uma lista real
        return respostas
    return None

def padronizar_tamanho_listas(*listas):
    max_length = max(len(lista) for lista in listas)
    return [lista + [None] * (max_length - len(lista)) for lista in listas]

count = 0
df = pd.read_csv('/Users/guisalesfer/CTM_implementation/tasks/RocStories/cloze_test_val__winter2018-cloze_test_ALL_val - 1 - 1.csv')
tasks = df.sample(25)
output_df = pd.DataFrame(columns=['InputStoryid', 'context', 'question', 'y', 'y_hat'])

print(f'\nExecutando Tarefas de RocStories')

for i, row in tasks.iterrows():
    context = ' '.join([row['InputSentence1'], row['InputSentence2'], row['InputSentence3'], row['InputSentence4']])
    question = f'Which of these fragments concludes the story in a coherent way? \n1. {row["RandomFifthSentenceQuiz1"]} \n2. {row["RandomFifthSentenceQuiz2"]}'
    count += 5
    

    file1 = "output_report.txt"
    file2 = "uptree_competition.txt"
    files_to_check = [file1, file2]
    for file in files_to_check:
        if os.path.exists(file):
            os.remove(file)
    print(f"\t- Executando Story {row['InputStoryid']}")

    story = [context, question]

    ctm = CTM(8, story)
    ctm.run()

    with open("/Users/guisalesfer/CTM_implementation/ctm_project/classes/output_report.txt", "r", encoding="utf-8") as f:
        conteudo = f.read()
    y_hat = extract_answers(conteudo)
    final_row = pd.DataFrame({'InputStoryid':[row['InputStoryid']], 'context':[context], 'question':[question], 'y':[row['AnswerRightEnding']], 'y_hat':[y_hat]})

    output_df = pd.concat([output_df, final_row], ignore_index=True)
    sleep(10)
            
    if count <= 100:
        print(f'\n Results Saved ! | Progress Default: {count}%')
    else:
        print(f'\n Results Saved ! | Progress Extra: {count+20}%')

output_df.to_csv(f"/Users/guisalesfer/CTM_implementation/tasks/RocStories/results/rocstories_result.csv", index=False)
