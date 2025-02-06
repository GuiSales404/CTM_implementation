from CTM import CTM 
import warnings
warnings.filterwarnings('ignore')
import os
import pandas as pd
os.environ["TOKENIZERS_PARALLELISM"] = "false"

with open('/Users/guisalesfer/CTM_implementation/tasks/babi-tasks/test/three-supporting-facts/story_1.txt') as f:
    task = f.read()
qa = []
context = []
story = []
for line in task.split('\n'):
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

file1 = "output_report.txt"
file2 = "uptree_competition.txt"
files_to_check = [file1, file2]
for file in files_to_check:
    if os.path.exists(file):
        os.remove(file)

ctm = CTM(2, story)
ctm.run()