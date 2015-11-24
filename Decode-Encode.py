import base64

def main():

	def Menu():
		print 'SECRET DECODER MENU \n 0) Quit \n 1) Encode \n 2) Decode \n';
		return

	def encode():
		global TextToEncode
		TextToEncode = raw_input("text to be encoded: ")
		global encodedText
		encodedText = base64.b64encode(TextToEncode, Alpha);
		global UpperTextEn
		UpperTextEn = ''.join(encodedText.upper())
		print UpperTextEn + '\n';

	def decode():
		TextToDecode = raw_input("code to be decyphered: " +UpperTextEn)
		DecodedText = base64.b64decode(encodedText, Key);
		NoSpecialCharsDecode = ''.join([char for char in DecodedText.upper() if char in Alpha])
		print NoSpecialCharsDecode;

	Alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
	Key = 'ALRUSELQWPWOEIRSNUCOROEJMDSZC';

	Menu()

	Option = raw_input("What do you want to do?: \n")
	OptionInt = int(Option);

	Loop = True;

	while Loop:
		Menu()
		if OptionInt == 1:
			encode()
			Option = raw_input('what do you want to do?: ')
			OptionInt = int(Option);

		elif OptionInt == 2:
			decode()
			print 'option 2 is being used';
			Option = raw_input('what do you want to do?: ')
			OptionInt = int(Option);

		elif OptionInt == 0:
			print 'Thanks for doing secret spy stuff with me.';
			Loop = False;

		else:
			print 'Not a valid choice, exiting program.';


			return

main()
