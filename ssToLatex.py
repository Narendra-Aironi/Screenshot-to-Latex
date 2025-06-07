#!/usr/bin/env python3
"""
Script to convert clipboard images containing mathematical content to LaTeX code
using Google's Gemini AI model.
"""

import os
import sys
import io
from PIL import Image, ImageGrab
import google.generativeai as genai
from typing import Optional

def setup_gemini_api() -> genai.GenerativeModel:
    """
    Setup and configure the Gemini API.
    Requires GOOGLE_API_KEY environment variable to be set.
    """
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        print("Error: GOOGLE_API_KEY environment variable not set.")
        print("Please set it with: export GOOGLE_API_KEY='your-api-key'")
        sys.exit(1)
    
    genai.configure(api_key=api_key)
    
    # Use Gemini Pro Vision model for image analysis
    model = genai.GenerativeModel('gemini-1.5-flash')
    return model

def get_clipboard_image() -> Optional[Image.Image]:
    """
    Get image from clipboard.
    Returns None if no image is found in clipboard.
    """
    try:
        image = ImageGrab.grabclipboard()
        if isinstance(image, Image.Image):
            return image
        else:
            print("No image found in clipboard.")
            return None
    except Exception as e:
        print(f"Error accessing clipboard: {e}")
        return None

def image_to_latex(model: genai.GenerativeModel, image: Image.Image) -> str:
    """
    Convert image containing mathematical content to LaTeX code.
    """
    prompt = """
    Please analyze this image which contains mathematical content and convert it to LaTeX code.
    
    Requirements:
    - Only output the LaTeX math code, no document structure
    - Do not include \\documentclass, \\begin{document}, \\section, etc.
    - Wrap the math content in $$ delimiters for display math
    - If there are multiple equations, separate them appropriately
    - Use proper LaTeX math notation and symbols
    - Be as accurate as possible in reproducing the mathematical expressions
    
    Output only the LaTeX code, nothing else.
    """
    
    try:
        response = model.generate_content([prompt, image])
        return response.text.strip()
    except Exception as e:
        print(f"Error generating LaTeX from image: {e}")
        return ""

def copy_to_clipboard(text: str) -> None:
    """
    Copy text to clipboard using pbcopy on macOS.
    """
    try:
        import subprocess
        process = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE, text=True)
        process.communicate(input=text)
        print("LaTeX code copied to clipboard!")
    except Exception as e:
        print(f"Error copying to clipboard: {e}")

def save_to_file(latex_code: str, filename: str = "output.tex") -> None:
    """
    Save LaTeX code to a file.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(latex_code)
        print(f"LaTeX code saved to {filename}")
    except Exception as e:
        print(f"Error saving to file: {e}")

def main():
    """
    Main function to orchestrate the image to LaTeX conversion.
    """
    print("Screenshot to LaTeX Converter")
    print("=" * 40)
    
    # Setup Gemini API
    print("Setting up Gemini API...")
    model = setup_gemini_api()
    
    # Get image from clipboard
    print("Getting image from clipboard...")
    image = get_clipboard_image()
    if not image:
        sys.exit(1)
    
    print(f"Image found: {image.size[0]}x{image.size[1]} pixels")
    
    # Convert image to LaTeX
    print("Converting image to LaTeX...")
    latex_code = image_to_latex(model, image)
    
    if latex_code:
        print("\nGenerated LaTeX code:")
        print("-" * 40)
        print(latex_code)
        print("-" * 40)
        
        # Copy to clipboard
        copy_to_clipboard(latex_code)
        
        # Optionally save to file (for command line use)
        if len(sys.argv) > 1 and sys.argv[1] == "--save":
            filename = sys.argv[2] if len(sys.argv) > 2 else "output.tex"
            save_to_file(latex_code, filename)
    else:
        print("Failed to generate LaTeX code.")
        sys.exit(1)

if __name__ == "__main__":
    main()



