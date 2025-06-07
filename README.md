# Screenshot-to-Latex
Convert any screenshot to Latex code! 
**Vibe coded**

## Features

- 📸 Converts clipboard images to LaTeX math code
- 🤖 Uses Google's Gemini AI for accurate recognition
- 📋 Automatically copies result to clipboard
- 💾 Optional file output
- 🎯 Focused on math content - no document structure tags

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Get Google API Key

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the Generative AI API
4. Go to "APIs & Services" > "Credentials"
5. Click "Create Credentials" > "API Key"
6. Copy the API key

### 3. Set Environment Variable

```bash
export GOOGLE_API_KEY='your-api-key-here'
```

To make it permanent, add to your `~/.zshrc`:
```bash
echo 'export GOOGLE_API_KEY="your-api-key-here"' >> ~/.zshrc
source ~/.zshrc
```

### 4. Verify Setup

```bash
./setup.sh
```

## Usage

- For Apple devices, you can simply create a shortcut in the shotcuts app that takes a screenshot (interactive) -> copies it to clipboard -> runs the python file -> stores the output in your clipboard.
- You can run the run_ssToLatex.sh file in the `run Script` block of the Shortcut. Also, set a keybinding for the shortcut or add it to Dock for easier access.
- Alternatively, you can run the python file directly, which is platform-agnostic.
- I am sure, similar setup can be done on any other platform



## Notes

- The script specifically targets mathematical content and wraps output in `$$` delimiters
- No document structure tags are included (no `\documentclass`, `\begin{document}`, etc.)
- Works best with clear, high-contrast mathematical expressions
- Supports complex equations, matrices, integrals, and other mathematical notation

## Troubleshooting

- **"No image found in clipboard"**: Make sure you've copied an image to your clipboard
- **"GOOGLE_API_KEY environment variable not set"**: Follow setup step 3

