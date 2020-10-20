

def readTextInput(input):
    text = str(input.replace('.', ' '))
    text = text.lower()
    text = list(text.split(" "))
    return text

sampleText = "The birch canoe slid on the smooth planks.\
Glue the sheet to the dark blue background.\
It's easy to tell the depth of a well.\
These days a chicken leg is a rare dish.\
Rice is often served in round bowls.\
The juice of lemons makes fine punch.\
The box was thrown beside the parked truck.\
The hogs were fed chopped corn and garbage.\
Four hours of steady work faced us.\
Large size in stockings is hard to sell."

#formattedText = readTextInput(sampleText)
#print(formattedText)
#print(len(formattedText))
