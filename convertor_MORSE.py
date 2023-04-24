class ConvertorMorse:

    def getInput(userInput):
        if len(userInput) == 0:
            return "Please enter your message"
        return userInput.upper()


    def convertor(output):
        userOutput = ""
        MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                           'C': '-.-.', 'D': '-..', 'E': '.',
                           'F': '..-.', 'G': '--.', 'H': '....',
                           'I': '..', 'J': '.---', 'K': '-.-',
                           'L': '.-..', 'M': '--', 'N': '-.',
                           'O': '---', 'P': '.--.', 'Q': '--.-',
                           'R': '.-.', 'S': '...', 'T': '-',
                           'U': '..-', 'V': '...-', 'W': '.--',
                           'X': '-..-', 'Y': '-.--', 'Z': '--..',
                           '1': '.----', '2': '..---', '3': '...--',
                           '4': '....-', '5': '.....', '6': '-....',
                           '7': '--...', '8': '---..', '9': '----.',
                           '0': '-----', ', ': '--..--', '.': '.-.-.-',
                           '?': '..--..', '/': '-..-.', '-': '-....-',
                           '(': '-.--.', ')': '-.--.-'}

        for index, char in enumerate(output) :
            #output = output.replace(output[i],MORSE_CODE_DICT[v])
            try:
                MORSE_CODE_DICT[char]
            except KeyError :
                userOutput += "n"
            else:
                userOutput += MORSE_CODE_DICT[char]

        return userOutput


