import pytest
from httpx import AsyncClient

@pytest.mark.anyio
async def test_get_runeword_item(client: AsyncClient):
    name = "enigma"
    response = await client.get(f"/runeworditems/{name}")
    assert response.status_code == 200