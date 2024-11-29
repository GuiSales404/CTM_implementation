# from UpTree import UpTree

# uptree = UpTree(['sentiment', 'ner', 'summarization', 'qa', 'llm', 'llama', 'syntatic-stanza', 'syntatic-spacy'])
# uptree.compete()

from InputMap import InputMap

a = InputMap("""Fazem 128 anos desde a publicação dos estudos sobre histeria (1893), de Breuer e Freud, onde o caso de Anna O. foi apresentado. Esta foi atendida por Breuer quando tinha 21 anos, e por mais que Freud não a atendeu, acabou por tornar o caso crucial para invenção da psicanálise. Ela apresentava sintomas histéricos, dentre eles, tosse, paralisias diversas, analgesias, distúrbios e alucinações visuais, desorganização da linguagem, mistura das línguas que falava, por vezes mutismo. Havia dois estados de consciência inteiramente distintos, que se alternavam. Num desses estados ela reconhecia seu ambiente, ficava melancólica e angustiada, mas relativamente normal, no outro tinha “alucinações”, e ficava agressiva. Com a morte do pai, precisou mudar, ficou no campo, Breuer a visitava a tardezinha, quando ela se encontrava no estado hipnótico, e não conseguia ir todos os dias. Então, quando ia ela descarregava os produtos imaginativos que ela tinha acumulado desde a última visita. No dia seguinte da visita ela ficava calma, mas no segundo dia já ficava irritada e assim por diante. Anna mesmo descrevia o método como “talking cure”, ou seja, cura pela fala, e se referia a ele como “chimney-sweeping, que quer dizer limpeza de chaminé.""").partition()

for sentence in a:
    print()
    print('-', sentence)