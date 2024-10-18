import pytest
from httpx import AsyncClient

@pytest.mark.anyio
async def test_get_unique_item(client: AsyncClient):
    name = "vipermagi"
    response = await client.get(f"/uniqueitems/{name}")
    assert response.status_code == 200
