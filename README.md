# CAUtils

A utility library for CA. 

## Installation

```bash
pip install .
```

## Usage

```python
from CAUtils import fs

# List files in current directory
fs.ls()

# Create a directory
fs.mkdir('test')

# Copy files or directories
fs.cp('test', 'test_copy')

# Move files or directories
fs.mv('test_copy', 'test_moved')

# Remove files or directories
fs.rm('test_moved', recursive=True)

# Print the current directory
print(fs.pwd())

# Change to a new directory
fs.cd('/path/to/new/directory')

# Print the current directory again to see the change
print(fs.pwd())
```