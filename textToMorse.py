class TextToMorse:
    def __init__(self):
        self.morse_code = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
            'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
            'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
            'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
            'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
            'Z': '--..',

            '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
            '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',

            '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
            '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
            ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
            '"': '.-..-.', '$': '...-..-', '@': '.--.-.', " ": "\\"
        }

    def textMorseEncoder(self, text):
        solution = []
        for i in text.upper():
            if i in self.morse_code:
                solution.append(self.morse_code[i])
            else:
                print(f"{i} not found in database")
                continue
        return "   ".join(solution)

    def morseToTextDecoder(self, morse):
        codes = morse.strip().split("   ")
        value = list(self.morse_code.values())
        keys = list(self.morse_code.keys())
        word = []
        unknown=[]
        for code in codes:
            if code in value:
                word.append(keys[value.index(code)])
            else:
                print(f"{code} is not present in database")
                unknown.append(code)  # Adding a placeholder for unknown Morse code
        return "".join(word)," -u- ".join(unknown)

if __name__ == "__main__":
    morse = TextToMorse()

    while True:
        choice = int(input("1. For encoding text to morse code\n2. for Decoding from morse code to text\n"
                           "3. Stop the application\nInput: "))
        if choice == 1:
            text = input("What text do you need to convert to morse code? ")
            morse_text = morse.textMorseEncoder(text=text)
            print("Here's your morse code:", morse_text, sep="\n")
        elif choice == 2:
            morse_code = input("Enter Morse code to convert to text (separate letters by three spaces): ")
            decoded_text = morse.morseToTextDecoder(morse=morse_code)
            print("Here's your decoded text:", decoded_text[0], sep="\n")
            print("Here's the code which are not present in database:" , decoded_text[1])
        elif choice == 3:
            print("Exiting the application.")
            break
