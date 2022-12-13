# first space finder lesson
def upper_first_word(aString):
    upperFirst = aString.upper()
    for i in range(len(aString)):
        charChecker = aString[i]
        if charChecker == " ":
            full = upperFirst[:i] + aString[i:]
            return full

        elif aString[i] == aString[-1]:
            return upperFirst

def main ():
    print(upper_first_word("Testing String"))

main()

"""def upper_first_word(aString):
    firstSpace= aString.find (" ")
    if firstSpace!= -1:
        upperFirst = aString.upper()
        lastWord= upperFirst [:firstSpace]+ aString [firstSpace:]

    else:
        upperFirst = aString.upper()
        lastWord= upperFirst

    return lastWord"""