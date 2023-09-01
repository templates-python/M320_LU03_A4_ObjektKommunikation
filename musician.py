import instrument

class Musician:
    """
    Beschreibt einen Musiker, der ein Instrument spielt und auf diesem Töne erzeugt.
    """

    def __init__(self, name, instrument):
        """
        Erzeugt ein Musiker-Objekt.
        :param name: Name des Musikers
        :param instrument: Referenz zum Instrument des Musikers
        """
        self._name       = name
        self._instrument = instrument

    @property
    def name(self):
        """
        Liefert den Namen des Musikers
        :return: Name des Musikers
        """
        return self._name

    def play_tone(self, the_tone):
        """
        Spielt den angegeben Ton
        :param the_tone: der gespielte Ton
        """
        print(f'{self._name} spielt mit {self._instrument.play_tone(the_tone)}')
