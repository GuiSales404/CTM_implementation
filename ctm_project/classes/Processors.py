import torch
import spacy
import stanza
from pysentimiento import create_analyzer
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers import T5Tokenizer, T5ForConditionalGeneration

class sentiment_analysis:
    def __init__(self):
        self.sentiment_analysis = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment", device=0)

    def process(self, text):
        return self.sentiment_analysis(text)
    
    
class ner:
    def __init__(self):
        self.ner = pipeline("token-classification", model="pierreguillou/ner-bert-base-cased-pt-lenerbr", device=0)
    
    def process(self, text):
        return self.ner(text)
    
    def group_tokens(self, tokens):
        for pos, item in enumerate(tokens):
            if 'B' in item['entity']:
                new_group = []
                new_group.append(item)
                i = 1
                while 'I' in tokens[tokens.index(item)+i]['entity']:
                    if pos+i+1 < len(tokens):
                        new_group.append(tokens[tokens.index(item)+i])
                        i += 1
                    else:
                        new_group.append(tokens[tokens.index(item)+i])
                        break
            if 'I' in item['entity']:
                continue
            print(new_group)
            
class summarization:
    def __init__(self):
        self.tokenizer = T5Tokenizer.from_pretrained("PamelaBorelli/flan-t5-base-summarization-pt-br")
        self.model = T5ForConditionalGeneration.from_pretrained("PamelaBorelli/flan-t5-base-summarization-pt-br")

    def process(self, input_text):
        input_ids = self.tokenizer(input_text, return_tensors="pt").input_ids
        outputs = self.model.generate(input_ids, max_new_tokens=250, min_length=25)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
class llm_processor:
    #"zhengr/MixTAO-7Bx2-MoE-Instruct-v7.0"
    #"mistralai/Mistral-7B-v0.1"
    #"stabilityai/stablelm-zephyr-3b"
    #"HuggingFaceH4/zephyr-7b-beta"
    #"stabilityai/stablelm-2-zephyr-1_6b"
    def __init__(self, model_path="stabilityai/stablelm-2-zephyr-1_6b"):
        self.model_path = model_path
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_path, trust_remote_code=True)
        model = AutoModelForCausalLM.from_pretrained(self.model_path, trust_remote_code=True).to(self.device)

        if self.device.type == 'cuda':
            torch.set_default_tensor_type(torch.cuda.BFloat16Tensor)

        if self.tokenizer.pad_token_id is None:
            self.tokenizer.pad_token_id = self.tokenizer.eos_token_id
            
    def process(self, input):
        input_ids = self.tokenizer(input, return_tensors="pt", truncation=True, max_length=16).to(self.device)
        max_length = input_ids.shape[1] + 10 
        attention_mask = torch.ones(input_ids.shape, dtype=torch.long, device=self.device)
        resumos = self.model.generate(
                                input_ids=input_ids,
                                attention_mask=attention_mask,
                                max_length=max_length,
                                do_sample=True,
                                temperature=0.1,
                                num_return_sequences=1,
                                eos_token_id=self.tokenizer.eos_token_id,
                                pad_token_id=self.tokenizer.pad_token_id
                                )
        return self.tokenizer.decode(resumos[0], skip_special_tokens=True)

class llama_processor:
    def __init__(self): 
        self.pipe = pipeline(
            "text-generation",
            model="meta-llama/Llama-3.2-3B-Instruct",
            torch_dtype=torch.bfloat16,
            device_map="auto",
        )
    
    def process(self, input):
        messages = [
                    {"role": "system", "content": "Você deve responder perguntas de inferência lógica corretamente. Retorne apenas a resposta final."},
                    {"role": "user", "content": "Maria foi ao banheiro. João foi para o corredor. Maria foi para o escritório. Onde está Maria?"},
                    ]
        outputs = self.pipe(
            messages,
            max_new_tokens=256,
        )
        print(outputs[0]["generated_text"][-1])
        
class syntatic_tree_stanza_processor:
    def __init__(self) -> None:
        stanza.download('pt')
        self.nlp = stanza.Pipeline('pt')
        
    def process(self, input):
        doc = self.nlp(input)
        
        result = []
        for sentence in doc.sentences:
            for word in sentence.words:
                result.append(f"{word.text} -> {word.deprel} -> {sentence.words[word.head - 1].text if word.head > 0 else 'ROOT'}")
                
        return result
    
class syntatic_tree_spacy_processor:
    def __init__(self) -> None:
        self.nlp = spacy.load("pt_core_news_sm")
        
    def process(self, input):
        doc = self.nlp(input)
        
        result = []
        for token in doc:
            result.append(f"{token.text} -> {token.dep_} -> {token.head.text}")
            
        return result
    
class irony_detection_processor:
    def __init__(self):
        self.analyzer = create_analyzer(task='irony', lang='pt')
        
    def process(self, input):
        return self.analyzer.predict(input).output
    
class hate_speech_detection_processor:
    def __init__(self):
        self.analyzer = create_analyzer(task='hate_speech', lang='pt')
        
    def process(self, input):
        return self.analyzer.predict(input).output
    
class emotion_detection_processor:
    def __init__(self):
        self.analyzer = create_analyzer(task='emotion', lang='pt')
        
    def process(self, input):
        return self.analyzer.predict(input).output