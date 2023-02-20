import argparse

def count_sequences(filename):
    """Count the number of non-blank lines in a FASTQ file"""
    with open(filename, "r") as file:
        count = 0
        for line in file:
            if line.strip():
                count += 1
    count=count // 4
    print(f"Number of sequences: {count}")

def main():
    parser = argparse.ArgumentParser(description="Utility functions for FASTQ files")
    parser.add_argument("filename", help="FASTQ file to process")
    parser.add_argument("-n", "--count-sequences", action="store_true", help="Count the number of sequences in the file")
    args = parser.parse_args()

    if args.count_sequences:
        count_sequences(args.filename)
    else:
        # Perform other operations here
        pass

if __name__ == "__main__":
    main()
