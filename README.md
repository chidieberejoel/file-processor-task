# file-processor-task

## Prerequisites

Python should be installed. Get Python [here](https://www.python.org/downloads/).\
Navigate to a directory of your choice using a CLI and run the following commands in the order:

```
git clone https://github.com/chidieberejoel/file-processor-task.git
cd file-processor-task
```
Create sample files with ".data" extension.\
Then, in your CLI run the following command:

```
python file-processor.py
```
Then, enter a directory path.

## Guidelines
This single Python 3.8.5 script consumes all of the .data files in a specified directory for processing\
\
It starts off by reversing the order of each line in the file, and for each line in the file, it reverses the order of each character.\
Then It creates an output written directly to a file of the same name, but with the additional ".reversed" extension.