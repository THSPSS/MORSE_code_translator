class ConverterMorse:

    #using when doing unittest
    #def getInput(userInput):
    #    return userInput.upper()
    def converter(output):
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

        for char in output :
            #output = output.replace(output[i],MORSE_CODE_DICT[v])
            if char.upper() in MORSE_CODE_DICT:
                userOutput += MORSE_CODE_DICT[char.upper()]
            elif char == " ":
                userOutput = " "
            else:
                return "Invalid input"

        return userOutput.strip()


