class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_letters = {}
        for letter in t:
            t_letters[letter] = t_letters.get(letter, 0) + 1

        unmet = 0
        met = len(t_letters)

        window = {}
        left_pointer = 0
        minimum = float ('inf')
        right_pointer = 0
        start_index = left_pointer
        end_index = right_pointer

        for num in range(len(s)):
            letter = s[num]

            if letter in t_letters:
                window[letter] = window.get(letter, 0) + 1
                if window[letter] == t_letters[letter]:
                    unmet += 1

            while unmet == met:
                if (num - left_pointer) < minimum:
                    minimum = (num - left_pointer)
                    start_index = left_pointer
                    end_index = num 

                leftmost_letter = s[left_pointer]

                if leftmost_letter in t_letters:
                    window[leftmost_letter] -= 1
                    if window[leftmost_letter] < t_letters[leftmost_letter]:
                        unmet -= 1

                left_pointer += 1


        if minimum < float ('inf'):
            return s[start_index:end_index + 1]   
        else:
            return ""
