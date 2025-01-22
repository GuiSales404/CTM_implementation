from CTM import CTM
import warnings
warnings.filterwarnings('ignore')
import os


def main():
	os.environ["TOKENIZERS_PARALLELISM"] = "false"

	with open('/Users/guisalesfer/CTM_implementation/ctm_project/emmy_von_r_sum.txt') as f:
		caso = f.read()

	ctm = CTM(2, str(caso))
	print('CTM created')
	ctm.run()

if __name__ == "__main__":
    main()
