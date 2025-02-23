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
    padrao = r"### Respostas Completas: (\[.*?\])"
    match = re.search(padrao, conteudo, re.DOTALL)
    
    if match:
        respostas = eval(match.group(1))  # Converte a string da lista para uma lista real
        return respostas
    return []

def padronizar_tamanho_listas(*listas):
    max_length = max(len(lista) for lista in listas)
    return [lista + [None] * (max_length - len(lista)) for lista in listas]

count = 55

made_tasks = [file.split('.')[0] for file in os.listdir('/Users/guisalesfer/CTM_implementation/tasks/babi-tasks/results')]
tasks_todo = set(os.listdir('/Users/guisalesfer/CTM_implementation/tasks/babi-tasks/test')) - set(made_tasks)

# for test in os.listdir('/Users/guisalesfer/CTM_implementation/tasks/babi-tasks/test'):
for test in tasks_todo:
    count += 5
    df = pd.DataFrame(columns=['question', 'y', 'y_hat', 'task_number'])
    print(f'\nTarefas de {test}')
    
    tasks = select_random(os.listdir(os.path.join('/Users/guisalesfer/CTM_implementation/tasks/babi-tasks/test', test)), 1)
    for task in tasks:
        if task.endswith('.txt'):
            
            file1 = "output_report.txt"
            file2 = "uptree_competition.txt"
            files_to_check = [file1, file2]
            for file in files_to_check:
                if os.path.exists(file):
                    os.remove(file)
                    
            with open(os.path.join('/Users/guisalesfer/CTM_implementation/tasks/babi-tasks/test', test, task)) as f:
                task_content = f.read()
            print('\t- Executando', task)

            qa = []
            context = []
            story = []
            for line in task_content.split('\n'):
                actual_sentence = ' '.join(line.split(' ')[1:])
                if '?' in actual_sentence:
                    question = actual_sentence.split('\t')
                    context.append(question[0].strip())
                    context = ' '.join(context)
                    story.append(context)
                    qa.append((context, question[1], question[2]))
                    context = []
                else:
                    context.append(actual_sentence)
                    
                questions = [q[0] for q in qa]
                ground_truth = [q[1] for q in qa]
                
            ctm = CTM(8, story)
            ctm.run()
            
            
            with open("/Users/guisalesfer/CTM_implementation/ctm_project/classes/output_report.txt", "r", encoding="utf-8") as f:
                conteudo = f.read()
            y_hat = extract_answers(conteudo)
            try:
                df = pd.concat([df, pd.DataFrame({'question': questions, 'y': ground_truth, 'y_hat': y_hat, 'task_number': task.split('_')[1].replace('.txt', '')})], ignore_index=True)
            except:
                questions, ground_truth, y_hat = padronizar_tamanho_listas(questions, ground_truth, y_hat)
                df = pd.concat([df, pd.DataFrame({'question': questions, 'y': ground_truth, 'y_hat': y_hat, 'task_number': task.split('_')[1].replace('.txt', '')})], ignore_index=True)
            sleep(60)
            
    df.to_csv(f'/Users/guisalesfer/CTM_implementation/tasks/babi-tasks/results/{test}.csv', index=False)
    print(f'\n{test} Results Saved ! | Progress: {count}%')
