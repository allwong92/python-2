class TaxMan:

    # Constructor
    def __init__(self, array, percent):
        self.array = array
        self.percent = percent
        self.__total = 0

    # Methods
    def calc_total(self):

        # Loop through each item in array
        for item in self.array:
            self.__total += item['price']
        
        percent = int(self.percent[:len(self.percent) - 1])
        percentage = 1 + (percent/100)
        self.__total *= percentage

    def get_total(self):
        return round(self.__total, 1)