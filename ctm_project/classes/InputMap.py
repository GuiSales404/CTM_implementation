"""""
The input maps in the CTM are responsible for transforming external sensory information into internal representations that the machine can process.
They convert the data captured by the sensors into an internal language called Brainish (which will not be used in this work),
encapsulate this information into chunks and send it to the LTM processors.
"""""

import spacy
from Processors import *

class InputMap:
    def __init__(self, content, process=True, test_content=False):
        """
        Inicializa o InputMap com o conteúdo fornecido.
        
        :param content: Texto a ser particionado.
        """
        self.nlp = spacy.load("pt_core_news_sm")
        
        # self.stanza_tree = syntatic_tree_stanza_processor()
        # self.spacy_tree = syntatic_tree_spacy_processor()
        self.irony = irony_detection_processor()
        self.hate_speech = hate_speech_detection_processor()
        self.emotion_detection = emotion_detection_processor()
        self.sentiment_anaysis = sentiment_analysis()
        # self.ner = ner()
        # self.summarization = summarization()
        
        if process == True:
            self.content = content
            self.partitioned = self.partition()
        
        if test_content == True:
            self.partitioned = content
            
        self.input_gist = []
        self.generate_input_content()

    def partition(self):
        doc = self.nlp(self.content)
        sentences = [sent.text.strip() for sent in doc.sents]
        return sentences
    
    def generate_input_content(self):
        input_gist = []
        for sentence in self.partitioned:
            input_gist.append(str({
                "sentence": sentence,
                # "syntatic_tree_stanza": self.stanza_tree.process(sentence),
                # "syntatic_tree_spacy": self.spacy_tree.process(sentence),
                "irony": self.irony.process(sentence),
                "hate_speech": self.hate_speech.process(sentence),
                "emotion_detection": self.emotion_detection.process(sentence),
                "sentiment_analysis": self.sentiment_anaysis.process(sentence),
                # "ner": self.ner.process(sentence)
            }))

        self.input_gist = input_gist