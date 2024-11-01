from transformers import pipeline
from sentence_transformers import SentenceTransformer, util
import random

# Configuração dos processadores especializados
sentiment_analyzer = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")
embedding_model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')  # Para medir a "novidade"

# Classe que representa um Processador Subconsciente
class SubconsciousProcessor:
    def __init__(self, process_function, name):
        self.process_function = process_function
        self.name = name

    def process(self, input_data, *args):
        return self.process_function(input_data, *args)

# Funções para os processadores subconscientes
def calculate_excitation(text):
    result = sentiment_analyzer(text)[0]
    excitation_score = int(result['label'].split()[0]) / 5  # Score de 1 a 5
    return {'name': 'excitation', 'score': excitation_score}

def calculate_novelty(new_text, previous_texts):
    new_embedding = embedding_model.encode(new_text)
    previous_embeddings = embedding_model.encode(previous_texts)
    novelty_score = 1 - util.pytorch_cos_sim(new_embedding, previous_embeddings).max().item()
    return {'name': 'novelty', 'score': novelty_score}

# Classe da Máquina de Turing Consciente (CTM)
class ConsciousTuringMachine:
    def __init__(self, threshold=0.5):
        self.memory_active = []            # Memória ativa (informação em foco)
        self.memory_long_term = []         # Memória de longo prazo
        self.global_workspace = []         # Espaço de trabalho global
        self.threshold = threshold         # Limiar inicial de estímulo
        self.reward_increment = 0.05       # Incremento de recompensa
        self.subconscious_processors = []

    def add_subconscious_processor(self, processor):
        self.subconscious_processors.append(processor)

    def add_to_memory_active(self, info):
        self.memory_active.append(info)

    def add_to_memory_long_term(self, info):
        self.memory_long_term.append(info)

    def process_global_workspace(self):
        # Processa informações de acordo com o limiar
        for info in self.memory_active:
            if info['score'] >= self.threshold:
                print(f"Processando no Princípio da Realidade: {info['name']} - Pontuação: {info['score']:.2f}")
                self.global_workspace.append(info)
                self.threshold += self.reward_increment  # Incrementa o limiar para preferir processamentos complexos
            else:
                print(f"Processando no Princípio do Prazer: {info['name']} - Pontuação: {info['score']:.2f}")
                self.threshold = max(0.5, self.threshold - self.reward_increment)  # Diminui o limiar para processamentos rápidos

    def subconscious_process(self, input_data, previous_interactions):
        # Processa subconscientemente e adiciona resultados à memória ativa
        for processor in self.subconscious_processors:
            result = processor.process(input_data, previous_interactions)
            if result:
                self.add_to_memory_active(result)

    def cycle(self, input_data, previous_interactions):
        # Executa um ciclo de processamento
        print("\nNovo Ciclo de Processamento:")
        self.subconscious_process(input_data, previous_interactions)  # Processadores subconscientes processam a entrada
        self.process_global_workspace()  # Integra no espaço de trabalho global
        self.memory_long_term.extend(self.memory_active)  # Transfere a memória ativa para a memória de longo prazo
        self.memory_active = []  # Limpa a memória ativa ao final do ciclo

# Inicializa a CTM e os processadores subconscientes
ctm = ConsciousTuringMachine()
ctm.add_subconscious_processor(SubconsciousProcessor(calculate_excitation, "Excitation Processor"))
ctm.add_subconscious_processor(SubconsciousProcessor(calculate_novelty, "Novelty Processor"))

# Simulação com interações e histórico de interações passadas
interactions = [
    "Uma história de aventura em uma selva misteriosa e perigosa.",
    "Uma conversa tranquila sobre o clima.",
    "Uma corrida de carros cheia de emoção e adrenalina.",
    "Uma descrição detalhada de uma biblioteca pacata."
]
previous_interactions = []

# Executa ciclos para cada interação
for interaction in interactions:
    ctm.cycle(interaction, previous_interactions)
    previous_interactions.append(interaction)  # Adiciona ao histórico de interações para calcular a novidade
