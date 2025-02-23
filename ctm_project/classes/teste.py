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


                    
with open('/Users/guisalesfer/CTM_implementation/tasks/babi-tasks/test/simple-negation/story_163.txt') as f:
    task_content = f.read()


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
    
ctm = CTM(4, story)
ctm.run()

with open("/Users/guisalesfer/CTM_implementation/ctm_project/classes/output_report.txt", "r", encoding="utf-8") as f:
    conteudo = f.read()
y_hat = extract_answers(conteudo)

print('y_hat:', y_hat)
print('ground_truth:', ground_truth)
print('questions:', questions)
# try:
#     df = pd.concat([df, pd.DataFrame({'question': questions, 'y': ground_truth, 'y_hat': y_hat, 'task_number': task.split('_')[1].replace('.txt', '')})], ignore_index=True)
# except:
#     print(f'\tERROR: question{len(questions)}, gt:{len(ground_truth)}, y_hat{len(y_hat)}')
#     print('Questions:', questions)
#     print('Ground Truth:', ground_truth)
#     print('Y Hat:', y_hat)
#     questions, ground_truth, y_hat = padronizar_tamanho_listas(questions, ground_truth, y_hat)
#     df = pd.concat([df, pd.DataFrame({'question': questions, 'y': ground_truth, 'y_hat': y_hat, 'task_number': task.split('_')[1].replace('.txt', '')})], ignore_index=True)
# sleep(60)

# df.to_csv(f'/Users/guisalesfer/CTM_implementation/tasks/babi-tasks/results/{test}.csv', index=False)
# print(f'\n{test} Results Saved !')
