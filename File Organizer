#!/usr/bin/env python3
"""
File Organizer
Organizes files in a directory by type (extension).
"""

import os
import shutil
from pathlib import Path


def organize_files(directory):
    """
    Organize files in the specified directory by their extensions.
    
    Args:
        directory (str): Path to the directory to organize
    """
    # Define file categories
    categories = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt'],
        'Spreadsheets': ['.xlsx', '.xls', '.csv', '.ods'],
        'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv'],
        'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a'],
        'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
        'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.sh'],
        'Others': []  # Everything else
    }
    
    # Convert to Path object
    dir_path = Path(directory)
    
    if not dir_path.exists():
        print(f"Error: Directory '{directory}' does not exist.")
        return
    
    # Count files moved
    files_moved = 0
    
    # Process each file in the directory
    for item in dir_path.iterdir():
        # Skip if it's a directory
        if item.is_dir():
            continue
        
        # Get file extension
        extension = item.suffix.lower()
        
        # Find the appropriate category
        category = 'Others'
        for cat_name, extensions in categories.items():
            if extension in extensions:
                category = cat_name
                break
        
        # Create category folder if it doesn't exist
        category_path = dir_path / category
        category_path.mkdir(exist_ok=True)
        
        # Move the file
        destination = category_path / item.name
        
        # Handle duplicate filenames
        counter = 1
        while destination.exists():
            name = item.stem
            destination = category_path / f"{name}_{counter}{extension}"
            counter += 1
        
        shutil.move(str(item), str(destination))
        files_moved += 1
        print(f"Moved: {item.name} → {category}/")
    
    print(f"\nDone! Organized {files_moved} files into categories.")


def main():
    """Main function to run the file organizer."""
    print("=== File Organizer ===\n")
    
    # Get directory from user
    directory = input("Enter directory path to organize (or press Enter for current directory): ").strip()
    
    if not directory:
        directory = os.getcwd()
    
    print(f"\nOrganizing files in: {directory}\n")
    
    # Confirm before proceeding
    confirm = input("This will move files into category folders. Continue? (y/n): ").strip().lower()
    
    if confirm == 'y':
        organize_files(directory)
    else:
        print("Operation cancelled.")


if __name__ == "__main__":
    main()
