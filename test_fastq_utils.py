import fastq_utils

def test_addition(capsys):
	fastq_utils.add(2,3)
	captured=capsys.readouterr()
	assert captured.out.strip() == "2 + 3 = 5"
