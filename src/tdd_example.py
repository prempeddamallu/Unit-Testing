class TDDExample():
    def __init__(self):
        pass

    def reverse_string(self, input_str: str) -> str:
        """
        Reverses order of characters in string input_str.
        """
        return input_str[::-1]

    def find_longest_word(self, sentence: str) -> str:
        """
        Returns the longest word in string sentence.
        In case there are several, return the first.
        """
        words = sentence.split()

        longest_word=""

        for word in words:
            if len(word)>len(longest_word):
                longest_word=word

        return longest_word

    def reverse_list(self, input_list: list) -> list:
        """
        Reverses order of elements in list input_list.
        """
        return input_list[::-1]

    def count_digits(self, input_list: list, number_to_be_counted: int) -> int:
        """
        Return count of digits
        """
         # Convert the digit to count into a string for comparison
        count = 0
        for number in input_list:
            if(number==number_to_be_counted): 
                count +=1
        
        return count
    