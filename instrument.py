class Instrument:
    '''
    Beschreibt ein Musikinstrument, das einen Ton spielen kann.
    '''


    def __init__(self, designation):
        '''
        Erstellt ein Instrument mit einer Bezeichnung
        :param designation: Bezeichnung des Instruments, z.B. Posaune
        '''
        self._designation = designation


    @property
    def designation(self):
        '''
        liefert die Instrumentenbezeichnung
        :return: Instrumentenbezeichnung
        '''
        return self._designation

    def play_tone(self, the_tone):
        '''
        Liefert den gespielten Ton
        :param the_tone:
        :return: Aussage zum gespielten Ton
        '''
        return str(f'{self._designation} den Ton {the_tone}')
