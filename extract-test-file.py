#!/usr/bin/env python3
"""
Unicode Character Extraction and Testing Utility

This script extracts Unicode character declarations from a LaTeX style file
and creates test documents to verify their compatibility with pdflatex.

Features:
- Extracts all Unicode characters declared using \DeclareUnicodeCharacter in the .sty file
- Creates LaTeX test files with the extracted characters
- Performs individual compilation tests to identify successfully supported characters
- Generates a consolidated report of compatible characters

Usage:
    python extract-test-file.py

Dependencies:
    - pdflatex must be installed and in the PATH
    - The DeclareUnicodeCharacter.sty file must be in the same directory
"""
import re
import os


def extract_unicode_chars(filename):
    """
    Extract all unicode characters declared in the .sty file.
    
    Args:
        filename (str): Path to the LaTeX style file containing \DeclareUnicodeCharacter declarations
        
    Returns:
        list: A list of tuples containing (hex_code, character) pairs
    """
    chars = []
    pattern = r'\\DeclareUnicodeCharacter\{([0-9A-F]{4})\}\{.*?\}'
    
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        matches = re.findall(pattern, content)
        
        for match in matches:
            try:
                # Convert hex code to actual unicode character
                char = chr(int(match, 16))
                chars.append((match, char))
            except ValueError:
                print(f"Warning: Could not convert {match} to a Unicode character")
    
    return chars

def create_test_file(chars, output_filename):
    """
    Create a LaTeX test file with all extracted characters.
    
    Args:
        chars (list): List of (hex_code, character) tuples
        output_filename (str): Name of the output LaTeX file
    """
    with open(output_filename, 'w', encoding='utf-8') as file:
        file.write("\\documentclass{article}\n")
        file.write("\\usepackage[utf8]{inputenc}\n")
        file.write("\\usepackage{DeclareUnicodeCharacter}\n\n")
        file.write("\\usepackage{longtable}\n\n")
        file.write("\\begin{document}\n\n")
        
        file.write("\\section*{Unicode Characters Test}\n\n")
        file.write(f"{len(chars)} characters supported, no more LaTeX Error: Unicode character ... not set up for use with LaTeX.\n\n")
        file.write("\\begin{longtable}{ll}\n")
        file.write("Hex Code & Character \\\\\n\\hline\n")
        
        for hex_code, char in chars:
            if char == "&": continue
            if char == "%": char="\\%"
            file.write(f"U+{hex_code} & {char} \\\\\n")
        
        file.write("\\end{longtable}\n\n")
        file.write("\\end{document}\n")

def extract_all_unicode_chars(filename):
    """
    Extract all unicode characters from the specified file and create a test document.
    
    Args:
        filename (str): Path to the LaTeX style file to process
    """
    sty_file = "DeclareUnicodeCharacter.sty"
    output_file = "test-file.tex"
    chars = extract_unicode_chars(sty_file)
    create_test_file(chars, output_file)
    print(f"Successfully extracted {len(chars)} Unicode characters to {output_file}")

def process_unicode_chars_individually():
    """
    Extract all characters and try to compile the LaTeX file one by one.
    Only characters that compile successfully are included in the final output.
    
    Returns:
        list: A list of tuples containing successfully compiled (hex_code, character) pairs
    """
    sty_file = "DeclareUnicodeCharacter.sty"
    output_dir = "test_results"
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Extract all unicode characters
    chars = extract_unicode_chars(sty_file)
    successful_chars = []
    
    for i, char_tuple in enumerate(chars):
        output_file = f"{output_dir}/test-char-{char_tuple[0]}.tex"
        create_test_file([char_tuple], output_file)
        
        # Try to compile the LaTeX file
        compile_result = os.system(f"pdflatex -interaction=nonstopmode -output-directory={output_dir} {output_file}")
        
        # If compilation was successful (exit code 0), add to successful chars
        if compile_result == 0:
            successful_chars.append(char_tuple)
            print(f"Character U+{char_tuple[0]} ({char_tuple[1]}) compiled successfully")
        else:
            print(f"Character U+{char_tuple[0]} ({char_tuple[1]}) failed to compile")
    
    # Create a final file with all successful characters
    if successful_chars:
        final_output = "successful-chars.tex"
        create_test_file(successful_chars, final_output)
        print(f"Created {final_output} with {len(successful_chars)} successfully compiled characters")
    
    return successful_chars

def main():
    """
    Main function that initiates the character extraction and testing process.
    """
    process_unicode_chars_individually()

if __name__ == "__main__":
    main()
