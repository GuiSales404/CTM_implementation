from CTM import CTM
import warnings
warnings.filterwarnings('ignore')


def main():

	with open('/home/gui/CTM_implementation/ctm_project/tests/emmy_von_r.txt') as f:
		caso = f.read()

	ctm = CTM(4, str(caso))
	print('CTM created')
	ctm.run()

if __name__ == "__main__":
    main()
