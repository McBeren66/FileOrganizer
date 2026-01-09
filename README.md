# File Organizer

This repository contains a Python script that organizes files in a given directory by their extension categories. The script scans the chosen folder and moves files into subfolders named after categories such as images (.jpg, .jpeg, .png), documents (.pdf, .docx, .doc), software (.exe, .msi) and archives (.zip). If a file with the same name exists in the target folder, the script renames the incoming file by adding a number suffix.

To run the script, update the `directory_path` variable with the path to the directory you want to tidy and execute the script with Python 3. The script will create the necessary subfolders and move the files accordingly. When it finishes, it prints a summary of how many files were moved.
