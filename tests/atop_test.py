import pytest
from atop import Ton_retriever

@pytest.fixture
def domains_ens_test():
    return ["vitalik.eth", "ahahahahahjdhassjkgsdajkhsdga.eth"]

def test_ipf2ens_ok(domains_ens_test):
    ipfs = Ton_retriever.ipf_ens(domains_ens_test[0])
    assert ipfs != ""

def test_ipf2ens_no(domains_ens_test):
    ipfs = Ton_retriever.ipf_ens(domains_ens_test[1])
    assert ipfs == ""
