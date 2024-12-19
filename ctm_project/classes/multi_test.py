# from Processors import llm_processor

# a = llm_processor()

# answer = a.process('Maria foi ao banheiro. João foi para o corredor. Maria foi para o escritório. Onde está Maria?', 'user')
# print('\nResposta:', answer)

from UpTree import UpTree
from Processors import *
from STM import STM
from LTM import LTM

stm = STM()
ltm = LTM(8)

upt = UpTree(stm=stm, ltm=ltm)

gist = {
    'sentence': 'Eu não sou capaz de acreditar que a raíz quadrada de 2 é um número irracional.',
	'syntatic_tree_stanza': ['Eu -> nsubj -> capaz',
	'não -> advmod -> capaz',
	'sou -> cop -> capaz',
	'capaz -> root -> ROOT',
	'de -> mark -> acreditar',
	'acreditar -> xcomp -> capaz',
	'que -> mark -> número',
	'a -> det -> raíz',
	'raíz -> nsubj -> número',
	'quadrada -> amod -> raíz',
	'de -> case -> 2',
	'2 -> nmod -> raíz',
	'é -> cop -> número',
	'um -> det -> número',
	'número -> ccomp -> acreditar',
	'irracional -> amod -> número',
	'. -> punct -> capaz'],
	'syntatic_tree_spacy': ['Eu -> nsubj -> capaz',
	'não -> advmod -> capaz',
	'sou -> cop -> capaz',
	'capaz -> ROOT -> capaz',
	'de -> mark -> acreditar',
	'acreditar -> xcomp -> capaz',
	'que -> mark -> número',
	'a -> det -> raíz',
	'raíz -> nsubj -> número',
	'quadrada -> advmod -> raíz',
	'de -> case -> 2',
	'2 -> nmod -> quadrada',
	'é -> cop -> número',
	'um -> det -> número',
	'número -> ccomp -> acreditar',
	'irracional -> amod -> número',
	'. -> punct -> capaz'],
	'irony': 'ironic',
	'hate_speech': [],
	'emotion_detection': ['surprise'],
	'sentiment_analysis': [{'label': '1 star', 'score': 0.45975199341773987}],
	'ner': [],
	'summarization': 'I no sabe que a raz quadrada de 2 é um nmero irracional.'
}

ltm.process(str(gist), 'user')