# RSON Character Recipe Tool

This tool allows you to convert serialized character information from Skate 3 into a readable JSON format and inject edited recipes back into the game. It features a PyQt-based GUI for easy use.

## Features

- **Extract**: Reads character recipe data from the running RPCS3 process and saves it as a readable JSON file (`output.json`).
- **Inject**: Loads a JSON or RSON file and writes it back into the game's memory.
- **GUI**: User-friendly interface built with PyQt5.

## Requirements

- Python 3.8+
- [PyQt5](https://pypi.org/project/PyQt5/)
- [pymem](https://pypi.org/project/pymem/)
- [S3RecipeHandler](https://pypi.org/project/S3RecipeHandler/) (for parsing and serializing Skate 3 recipes)
- RPCS3 emulator running `rpcs3.exe`
- Skate 3 running in RPCS3

## Setup

1. Install dependencies:
    ```sh
    pip install PyQt5 pymem S3RecipeHandler
    ```
2. Make sure `rpcs3.exe` is running with Skate 3 loaded.
3. Run the tool:
    ```sh
    python main.py
    ```

## Usage

- **Attach**: The tool will attempt to connect to the running RPCS3 process automatically.
- **Extract**: Click the "extract" button to dump the current character recipe to `output.json`.
- **Inject**: Click the "inject" button and select a `.json` or `.rson` file to inject it into the game.

## File Structure

- `main.py` - Main application logic and GUI.
- `mainui.py` - PyQt5 UI code (auto-generated from `ui/main.ui`).
- `rpcs3_handle.py` - Handles memory reading/writing with RPCS3.
- `output.json` - Output file for extracted recipes.
- `ui/main.ui` - Qt Designer UI file.
- `ui/ui.bat` - Batch script to regenerate `mainui.py` from `main.ui`.

## Notes

- Editing the output JSON and injecting it back allows for custom character modifications.
- The tool is intended for use with Skate 3 modding and research.

## Disclaimer

This tool is provided for educational and research purposes. Use at your own risk. The author is not responsible for any damage or loss caused by the use of this tool.