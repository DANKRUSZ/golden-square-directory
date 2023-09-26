class GrammarStats:
    def __init__(self):
        self.texts_that_passed = 0
        self.num_of_texts = 0
    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        
        self.valid_punc = ["!", ".", "?"]
        if text == text.capitalize() and text[-1] in self.valid_punc:
            self.texts_that_passed += 1
            self.num_of_texts += 1
            return True
        elif len(text) == 0:
            raise Exception("There is no string to check for grammar mistakes.")
        else:
            self.num_of_texts += 1
            return False
    
    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        percentage = self.texts_that_passed / self.num_of_texts  * 100
        rounded = round(percentage)
        return rounded