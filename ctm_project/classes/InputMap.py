"""""
The input maps in the CTM are responsible for transforming external sensory information into internal representations that the machine can process.
They convert the data captured by the sensors into an internal language called Brainish (which will not be used in this work),
encapsulate this information into chunks and send it to the LTM processors.
"""""

import spacy

class InputMap:
    def __init__(self, content):
        """
        Inicializa o InputMap com o conteúdo fornecido.
        
        :param content: Texto a ser particionado.
        """
        self.content = content
        self.nlp = spacy.load("pt_core_news_sm")  # Modelo de português

    def partition(self):
        """
        Divide o conteúdo em sentenças respeitando regras gramaticais.
        
        :return: Lista de sentenças particionadas.
        """
        doc = self.nlp(self.content)
        sentences = [sent.text.strip() for sent in doc.sents]
        return sentences