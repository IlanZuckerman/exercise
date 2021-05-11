import pytest


def test_father_procs_mnt(load_actual_and_conf):
    """
    Check that amount of actual 'father' procs equals to expected amount as defined in conf file
    :param load_actual_and_conf (dict of dicts): Consists of two dicts (actual and conf)
    """
    father_procs_mnt = len([x for x in pytest.actual_dict['processes'] if x['ppid'] == '0'])
    assert int(pytest.conf_dict['num_procs']) == father_procs_mnt, "Amount of actual father process isnt equal to expected"


def test_son_procs_mnt(load_actual_and_conf):
    """
    Check that total amount of 'son' procs equals to amount of 'father' procs, regardless of their relationship.
    Assume, that each 'father' process can fork only one 'son'
    :param load_actual_and_conf (dict of dicts): Consists of two dicts (actual and conf)
    """
    actual_son_procs_mnt = len([x for x in pytest.actual_dict['processes'] if x['ppid'] != '0'])
    if 'fork' in pytest.conf_dict['actions']:
        expected_son_procs_mnt = int(pytest.conf_dict['num_procs'])
    else:
        expected_son_procs_mnt = 0
    assert actual_son_procs_mnt == expected_son_procs_mnt, "Actual son process amount not matched to expected."


def test_fother_son_relation(load_actual_and_conf):
    """
    Check that each 'son' proc has its 'father' proc, according its ppid
    :param load_actual_and_conf (dict of dicts): Consists of two dicts (actual and conf)
    """
    actual_son_procs_mnt = len([x for x in pytest.actual_dict['processes'] if x['ppid'] != '0'])
    if actual_son_procs_mnt == 0:
        pytest.skip("No son procs detected")

    son_ppids = [x['ppid'] for x in pytest.actual_dict['processes'] if x['ppid'] != '0']
    father_procs_pids = [x['pid'] for x in pytest.actual_dict['processes'] if x['ppid'] == '0']
    for ppid in son_ppids:
        assert ppid in father_procs_pids, f"Son process pid {ppid} wasnt fond in a list of father pids"
