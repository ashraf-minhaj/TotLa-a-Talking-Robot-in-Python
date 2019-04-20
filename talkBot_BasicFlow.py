"""
Making of a talking robot v1.
Speech TO Text - google api (*Online) - Takes a bit time
Text To Speech - Offline - Fast.

by  : Ashraf Minhaj
mail: ashraf_minhaj@yahoo.com
blog: ashrafminhajfb.blogspot.com
"""

"""
Basic flow:
1. Listen - speech to text function
2. Decide - Decision function
3. Respond - Text to speech function
"""

# Import necessary Libraries

def Listen():
    command = input("Say it baby: ")

    return command

def Decide(listen):
    print(f" Command = {listen}.")

    if listen == "hi there":
        return "Hello"


def Respond(t):
    print(f"Talking the {t}")
    # Returns nothing so you'll get a None at the End,
    # Ignore it

while True:
    comm = Listen()

    decision = Decide(comm)

    print(Respond(decision))