# System Info Tool

Quick CLI tool that shows system information. First thing I reach for when troubleshooting someone's computer remotely.

## What it does

Run it and you get:
- OS and version
- Machine architecture  
- Processor
- Python version
- Current user and hostname

## Usage

```bash
python3 system_info.py
```

That's it. No options, no config. Just the info you need.

## Example

```
=== System Information ===

OS: Linux 5.15.0
Version: #92-Ubuntu SMP
Machine: x86_64
Processor: Intel(R) Core(TM) i7-9750H
Python Version: 3.10.4
Username: adrian
Computer Name: adrian-laptop

==============================
```

## Why this exists

I got tired of running `uname -a`, `lsb_release -a`, and other commands every time I need to check someone's system. This gives me everything in one shot.

It's really basic but super practical. Sometimes the simplest tools are the most useful.

## Technical stuff

Uses Python's `platform` and `os` modules. About 25 lines total. No external dependencies.

The `platform` module is pretty handy - has functions like `platform.system()`, `platform.release()`, etc. Didn't know about it until I needed it for this.

## Things I might add later

- RAM and disk info (probably using `psutil`)
- Network interfaces
- Option to save output to file

But honestly it works fine as is for what I need.

## Requirements

Python 3.6+

---

Adrián Domínguez Fernández
