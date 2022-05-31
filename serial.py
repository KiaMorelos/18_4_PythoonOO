"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()
    'Serial Generator count has been reset'

    >>> serial.generate()
    100
    """
    
    incrementer = 0 #this keeps track of how many instances have been made.

    def __init__(self, start):
        """Start count at user provided number"""
        self.start = start

    def __repr__(self):
        """representation of serial generator class"""
        return f"<SerialGenerator start={self.start} next={self.start + SerialGenerator.incrementer}>"

    def generate(self):
        """Use start number given and generate serial plus the incrementer,
        which starts the counting at 0, 
        update the incrementer count by 1, return the serial"""
        serial = self.start + SerialGenerator.incrementer
        SerialGenerator.incrementer += 1
        return serial

    def reset(self):
        """Reset the incrementer count to 0, inform user the count was reset"""
        SerialGenerator.incrementer = 0
        return 'Serial Generator count has been reset'




