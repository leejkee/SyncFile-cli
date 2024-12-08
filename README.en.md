# Sync Files CLI Tool

A Python tool to synchronize files from a `ResourceDir` to a `DestinationDir`.

## How it works?
Copy files from `ResourceDir` to `DestinationDir`, however, all existing files will be skipped.

## Features

- Sync files from `ResourceDir` to `DestinationDir`.
- Default `ResourceDir` is `~\Pictures\icon`.
- Default `DestinationDir` is the current directory.
- Use `-h` or `--help` to display help information.
- Use `-t` to test how it works actually.


### Basic Usage

#### Linux
```bash
python main.py
```

#### Windows

```ps1
python.exe .\main.py
```

#### Test mode
Use `-t` to test