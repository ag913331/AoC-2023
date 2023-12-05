def stage_one():
    with open("input.txt", "r") as f:
        file_content = f.readlines()
    
    total = 0
    for line in file_content:
        characters = line.strip() # remove newlines \n
        digits = []
        for ch in characters:
            if ch.isdigit():
                digits.append(ch)
        string_calibration_value = digits[0] + digits[-1] # concatenate first and last digits in the line
        total += int(string_calibration_value)
    print(total)

def main():
    stage_one()

if __name__ == '__main__':
    main()
