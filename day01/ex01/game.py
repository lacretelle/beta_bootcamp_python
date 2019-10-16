class GotCharacter:
    """A class representing the GOT character with their name and if they are alive or not
    """
    def __init__(self, first_name, is_alive=True):
        try:
            if not first_name:
                self.first_name = None
            elif isinstance(first_name, str):
                self.first_name = first_name
            self.is_alive = is_alive
        except Exception as err:
            print (err)

class Stark(GotCharacter):
    """ A class representing the Stark family. Not bad people but a lot of bad luck. """
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words(self):
        """ prints to screen the House words """
        print (self.house_words)

    def die(self):
        if self.is_alive:
            self.is_alive = False
