import pytest
from django.urls import reverse

@pytest.fixture
def index_response(client):
    return client.get(reverse('core:index'))

def test_index_status_code(index_response):
    assert index_response.status_code == 200