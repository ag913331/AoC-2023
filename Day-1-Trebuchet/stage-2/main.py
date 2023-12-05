def stage_two():
    WORDS_TO_DIGITS = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    with open("input.txt", "r") as f:
        file_content = f.readlines()
    
    total = 0
    for line in file_content:
        characters = line.strip() # remove newlines \n
        digits = []
        for index, ch in enumerate(characters):
            if ch.isdigit():
                digits.append((ch, index)) # append the digit and its index as a tuple [('2', 0)]
        for str_digit in WORDS_TO_DIGITS.keys():
            indexes = [i for i in range(len(characters)) if characters.startswith(str_digit, i)] # find indexes of all occurrences of a word/digit
            for index in indexes:
                digits.append((str(WORDS_TO_DIGITS[str_digit]), index)) # append the value of the word/digit and its index as a tuple [('9', 4)]
        sorted_digits = sorted(digits, key=lambda x: x[1]) # sort the list by index in the tuples -> [('2', 0), ('1', 3), ('9', 4)]
        string_calibration_value = sorted_digits[0][0] + sorted_digits[-1][0] # concatenate the values, first and last -> '2' + '9' = '29'
        total += int(string_calibration_value)
    print(total)

def main():
    stage_two()

if __name__ == '__main__':
    main()
