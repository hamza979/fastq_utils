
# fastq_utils 

fastq_utils is a command-line utility for processing FASTQ files. It includes functions for counting the number of sequences and nucleotides in a FASTQ file.

## Installation

fastq_utils is written in Python and can be run on any machine with Python 3 installed.

To use fastq_utils, simply download the fastq_utils.py file from this repository and save it to your local machine.

## Usage
To use fastq_utils, open a command prompt or terminal and navigate to the directory where you saved fastq_utils.py. Then, run the script with the following command:
```
python fastq_utils.py <filename> [options]
```
Replace <filename> with the path to the FASTQ file you want to process.

The following options are available:

    --count-sequences: Count the number of sequences in the file
    --count-nucleotides: Count the total number of nucleotides in the file

The tool also supports gzip compressed FASTQ files. If the filename ends with ".gz", the tool will automatically detect and handle it.

For example, to count the number of sequences in a gzip compressed FASTQ file named example.fastq.gz, run the following command:


```python fastq_utils.py example.fastq.gz --count-sequences```

## Workflow
This repository is configured to automatically check tests (see test_fastq_utils.py) before allowing any pushes to the main branch.


## License

[MIT](https://choosealicense.com/licenses/mit/)

