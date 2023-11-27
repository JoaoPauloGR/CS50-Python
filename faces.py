def main():
    # ask the user for a input
    stringVar = input()
    stringVar = convert(stringVar)
    print(stringVar)

def convert(var):
    # replace the given text with emoji
    var = var.replace(":)","🙂")
    var = var.replace(":(","🙁")

    return var

main()