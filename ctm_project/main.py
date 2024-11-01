from ctm_project.classes.CTM import CTM
from ctm_project.classes.Chunk import Chunk


def main():
    num_processors = 10
    total_time = 100

    ctm = CTM(num_processors)

    # Adicionando entradas de exemplo
    for t in range(total_time):
        input_chunk = Chunk(address=-1, time=t, gist=f"Input at time {t}", weight=1.0, intensity=1.0, mood=1.0)
        ctm.add_input(input_chunk)

    # Executando a CTM
    ctm.run(total_time)

    # Obtendo e imprimindo as saídas
    for t in range(total_time):
        output = ctm.get_output(t)
        print(f"Output at time {t}: {output}")

if __name__ == "__main__":
    main()
