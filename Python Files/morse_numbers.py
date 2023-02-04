#  Enter a number to translate it into morse code
translate = input("Enter a number: ")

translate = translate.replace(" ", "_")
translate = translate.replace("0", "----- ")
translate = translate.replace("1", ".---- ")
translate = translate.replace("2", "..--- ")
translate = translate.replace("3", "...-- ")
translate = translate.replace("4", "....- ")
translate = translate.replace("5", "..... ")
translate = translate.replace("6", "-.... ")
translate = translate.replace("7", "--... ")
translate = translate.replace("8", "---.. ")
translate = translate.replace("9", "----. ")

print(translate)
