#!/usr/bin/env python3
"""
System Info Tool
Displays basic system information useful for troubleshooting.
"""

import platform
import os

def main():
    print("=== System Information ===\n")
    
    # Operating System
    print(f"OS: {platform.system()} {platform.release()}")
    print(f"Version: {platform.version()}")
    
    # Machine info
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}")
    
    # Python info
    print(f"Python Version: {platform.python_version()}")
    
    # User and hostname
    print(f"Username: {os.getlogin()}")
    print(f"Computer Name: {platform.node()}")
    
    print("\n" + "="*30)

if __name__ == "__main__":
    main()
