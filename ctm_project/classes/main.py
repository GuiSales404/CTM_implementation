from CTM import CTM
import warnings
warnings.filterwarnings('ignore')
import os

def main():
	os.environ["TOKENIZERS_PARALLELISM"] = "false"

	file1 = "output_report.txt"
	file2 = "uptree_competition.txt"
	files_to_check = [file1, file2]
	for file in files_to_check:
		if os.path.exists(file):
			os.remove(file)

	with open('/Users/guisalesfer/CTM_implementation/ctm_project/emmy_von_r_sum.txt') as f:
		caso = f.read()

	ctm = CTM(2, str(caso))
	print('\nCTM created')
	ctm.run()

if __name__ == "__main__":
    main()
