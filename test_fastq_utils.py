import fastq_utils

def test_sequence_count(capsys):
	fastq_utils.count_sequences("test1.fastq")
	captured=capsys.readouterr()
	assert captured.out.strip() == "Number of sequences: 1000"
	
def test_nucleotide_count(capsys):
	fastq_utils.count_nucleotides("test1.fastq")
	captured=capsys.readouterr()
	assert captured.out.strip() == "Number of nucleotides: 100000"
	
def test_sequence_count_gz(capsys):
	fastq_utils.count_sequences("test2.fastq.gz")
	captured=capsys.readouterr()
	assert captured.out.strip() == "Number of sequences: 755"
	
def test_nucleotide_count_gz(capsys):
	fastq_utils.count_nucleotides("test2.fastq.gz")
	captured=capsys.readouterr()
	assert captured.out.strip() == "Number of nucleotides: 75500"
