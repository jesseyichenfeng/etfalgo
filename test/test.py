from experiment.function import pull_data

def test_pull_data():
    data = pull_data('UPRO','2018-01-01')
    assert len(data)!=0