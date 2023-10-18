import argparse
import string

def convert_line(line):
    result = ''
    for word in line:
        word, punc = strip_punctuation(word)
        if punc is not None:
            result += f"({'    ' * len(word)}){punc} "
        else:
            result += f"({'    ' * len(word)}) "
    return result

def strip_punctuation(input_string):
    # Create a translation table to remove all punctuation
    translator = str.maketrans('', '', string.punctuation)
    
    # Use the translation table to remove punctuation from the string
    stripped_string = input_string.translate(translator)
    
    # Create a string containing only the removed punctuation
    removed_punctuation = ''.join(char for char in input_string if char in string.punctuation)

    if removed_punctuation == "'":
        return stripped_string, None
    else:
        return stripped_string, removed_punctuation

def main():
    parser = argparse.ArgumentParser(description="Process a text file with punctuation removal.")
    parser.add_argument("input_file", help="Input text file name")

    args = parser.parse_args()

    input_file_name = args.input_file
    output_file_name = f"{input_file_name}_output.txt"

    try:
        with open(input_file_name, "r") as input_file:
            with open(output_file_name, "w") as output_file:
                for line in input_file:
                    if line.strip():
                        words = line.split()
                        first_word = words[0]
                        output_line = f"{first_word} {convert_line(words[1:])}\n"
                        output_file.write(output_line)
                    else:
                        output_file.write('\n')

        print(f"Processing of '{input_file_name}' completed. Output saved as '{output_file_name}'.")

    except FileNotFoundError:
        print(f"Input file '{input_file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
