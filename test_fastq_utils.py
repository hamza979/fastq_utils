import fastq_utils

def test_sequence_count(capsys):
	fastq_utils.count_sequences("test1.fastq")
	captured=capsys.readouterr()
	assert captured.out.strip() == "Number of sequences: 1000"
