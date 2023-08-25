from instrument import Instrument
from musician import Musician


#   main.py dien t der Ausführung der Applikation.
#   Es werden die benötigen Objekte erzeugt und die
#   Methoden gemäss Vorgabe aufgerufen.

def main():
    guitar = Instrument('Gitarre')
    piano = Instrument('Klavier')
    max = Musician('Max', guitar)
    moritz = Musician('Moritz', piano)

    max.play_tone('a')
    moritz.play_tone('f')

if __name__ == "__main__":
    main()
