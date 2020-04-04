import re
import matplotlib.pyplot as plt
from collections import Counter
from retrying import retry


@retry
def user_shift_input():
    shift_input = input("Enter the shift parameter (0-25): ")
    shift_match = re.search(r"(1\d)|(2[0-5])|(\d)", shift_input)
    if shift_match is None:
        raise ValueError("Cannot determinate valid shift parameter")
    print("Entered shift parameter is " + shift_match.group(0))
    return int(shift_match.group(0))


@retry
def user_file_input():
    file_input = input("Enter filename located in script's directory: ")
    with open(file_input, 'r') as file:
        text = file.read()
    return text


def encode(shift, char, offset):
    encoded_char_offset = (ord(char) - offset + shift) % 26
    return chr(offset + encoded_char_offset)


def decode(shift, char, offset):
    encoded_char_offset = (ord(char) - offset - shift) % 26
    return chr(offset + encoded_char_offset)


def cipher(shift, input_text, code):
    output_text = [None] * len(input_text)
    lower_case_offset = ord('a')
    upper_case_offset = ord('A')
    for index, char in enumerate(input_text):
        if re.match(r"[a-z]", char):
            output_text[index] = code(shift, char, lower_case_offset)
        elif re.match(r"[A-Z]", char):
            output_text[index] = code(shift, char, upper_case_offset)
        else:
            output_text[index] = char
    return ''.join(output_text)


def plot_histogram(text, color):
    hist = Counter(text)
    plt.bar(list(map(ord, hist.keys())), hist.values(), color=color)


def main():
    shift = user_shift_input()
    text = user_file_input()
    print(text)
    encoded_text = cipher(shift, text, encode)
    print(encoded_text)
    decoded_text = cipher(shift, encoded_text, decode)
    print(decoded_text)
    plot_histogram(encoded_text, 'r')
    plot_histogram(decoded_text, 'b')
    plt.show()


if __name__ == "__main__":
    main()
