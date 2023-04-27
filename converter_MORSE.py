class ConverterMorse:

    #using when doing unittest
    #def getInput(userInput):
    #    return userInput.upper()
    def makingList(userInput):
        userInput = userInput.replace(" ", "/")
        userList = userInput.split("/")
        print(userList)
        return ConverterMorse.converter(userList)

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
                           '?': '..--..', '-': '-....-','(': '-.--.',
                           ')': '-.--.-'}

        # list out keys and values separately
        key_list = list(MORSE_CODE_DICT.keys())
        val_list = list(MORSE_CODE_DICT.values())

        for char in output :
            #output = output.replace(output[i],MORSE_CODE_DICT[v])
            if char.upper() in key_list:
                position = key_list.index(char.upper())
                userOutput += val_list[position]
            elif char.upper() in val_list:
                position = val_list.index(char.upper())
                userOutput += key_list[position]
            else:
                return "Invalid input"
            userOutput += " "

        return userOutput.strip()


