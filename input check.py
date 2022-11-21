def main():
    x = print(getInt("Please insert a number: "))
    y = print(getFloat("Please insert a float: "))
    z = print(getText("Please insert text: "))

def getInt(question):
    while True:
        try:
            x = int(input(question))
            return x
        except ValueError:
            print("Please insert a full number.")

def getFloat(question):
    while True:
        try:
            y = float(input(question))
            return y
        except ValueError:
            print("Please insert a full OR decimal number.")

def getText(question):
    while True:
        z = input(question)
        if z.isalpha() == True:
            return z
        else:
            print("Please insert just text with no numbers or symbols")


main()