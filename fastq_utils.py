import argparse

def count_sequences(filename):
    """Count the number of non-blank lines in a FASTQ file and divide by 4"""
    with open(filename, "r") as file:
        count = 0
        for line in file:
            if line.strip():
                count += 1
    count=count // 4
    print(f"Number of sequences: {count}")
    
    
def count_nucleotides(filename):
    """Sum the len of each field 2 line"""
    count = 0
    with open(filename, "r") as file:
        for i, line in enumerate(file):
            if i % 4 == 1:
                count += len(line.strip())
    print(f"Number of nucleotides: {count}")


def main():
    parser = argparse.ArgumentParser(description="Utility functions for FASTQ files")
    parser.add_argument("filename", help="FASTQ file to process")
    parser.add_argument("--count-sequences", action="store_true", help="Count the number of sequences in the file")
    parser.add_argument("--count-nucleotides", action="store_true", help="Count the total number of nucleotides in the file")
    args = parser.parse_args()

    if args.count_sequences:
        count_sequences(args.filename)
    elif args.count_nucleotides:
        count_nucleotides(args.filename)


if __name__ == "__main__":
    main()
