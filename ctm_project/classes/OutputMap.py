"""
Is responsible for converting the machine's internal representations into signals or commands that can be sent to actuators or external systems,
allowing the CTM to interact with the environment.
They translate CTM intentions, decisions, or responses into physical actions, verbal expressions, or other forms of output that impact the external world.
"""
from DiscreteClock import DiscreteClock 
class OutputMap:
    _instance = None  

    def __new__(cls, *args, **kwargs):
        
        if cls._instance is None:
            cls._instance = super(OutputMap, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'outputs'):  
            self.outputs = []
            self.conscious_contents = []
            self.clock = DiscreteClock()
            self.processors = None
            self.qa_list = []
            
    def output(self, Chunk):
        self.outputs.append(Chunk)
        # print(f"\n💭Pensamento Gerado no tempo {self.clock.get_actual_time()}:", Chunk.gist)

    def conscious_content(self, Chunk):
        self.conscious_contents.append(Chunk)
        # print(f"\n💭Conteúdo Consciente no tempo {self.clock.get_actual_time()}:", Chunk.gist)
        
    def competition(run, competitors, winners, file_name="uptree_competition.txt"):
        """
        Prints the competition results and saves them to a file.

        Args:
            run (int): The competition round number.
            competitors (list): List of competitors (objects with a 'gist' attribute).
            winners (list): List of winners (objects with a 'gist' attribute).
            file_name (str): Name of the file to save the competition results. Default: 'uptree_competition.txt'.
        """
        # Print to terminal
        print(f"\n🏆 Competition {run}:")
        print("-" * 40)
        for i, winner in enumerate(winners):
            print(f"Winner {i}: {winner.gist}")
        print("-" * 40)
        print("\n🏆 Competitors:")
        print("-" * 40)
        for i, competitor in enumerate(competitors):
            print(f"Competitor {i}: {competitor.gist}")
        print("-" * 40)

        # Save to file
        with open(file_name, "a", encoding="utf-8") as file:
            file.write(f"\n🏆 Competition {run}:\n")
            file.write("-" * 40 + "\n")
            for i, winner in enumerate(winners):
                file.write(f"Winner {i}: {winner.gist}\n")
            file.write("-" * 40 + "\n")
            file.write("\n🏆 Competitors:\n")
            file.write("-" * 40 + "\n")
            for i, competitor in enumerate(competitors):
                file.write(f"Competitor {i}: {competitor.gist}\n")
            file.write("-" * 40 + "\n")

        
    def generate_report(self, file_name="output_report.txt"):
        """
        Gera um relatório com os outputs e conteúdos conscientes e salva em um arquivo .txt.

        Args:
            file_name (str): Nome do arquivo onde o relatório será salvo. Padrão: 'output_report.txt'.
        """
        
        with open(file_name, "w", encoding="utf-8") as file:
            file.write("Processadores:\n")
            file.write("-" * 40 + "\n")
            for processor in self.processors:
                file.write(f"\t- {processor.name}\n")
            file.write("-" * 40 + "\n")
            file.write("\n📜 Conteúdo Consciente:\n")
            file.write("-" * 40 + "\n")
            for i, content in enumerate(self.conscious_contents):
                file.write(f"Conteúdo Consciente {i}: {content.gist}\n")
            file.write("-" * 40 + "\n")
            file.write("\n📜 Perguntas e Respostas:\n")
            file.write("-" * 40 + "\n")
            answers =[]
            for i, qa in enumerate(self.qa_list):
                file.write(f"Pergunta {i+1}:\n")
                for key, value in enumerate(qa[0].split('.')):
                    file.write(f"\t{key+1}: {value}\n")
                file.write(f"Resposta: {qa[1]}\n")
                answers.append(qa[1])
                file.write("-" * 10 + "\n")
            file.write("-" * 40 + "\n")
            file.write(f"### Respostas Completas: {answers[-1]}\n")
            
        # print(f"\n✅ Relatório salvo em: {file_name}")

    def print_question(self, question):
        # print(f"\n🤔 Pergunta:")
        # for key, value in enumerate(question.split('.')):
        #     print(f"\t{key+1}: {value}")
        pass

            
    def qa(self, question, answer):
        self.qa_list.append((question, answer))
