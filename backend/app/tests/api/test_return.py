from fastapi.testclient import TestClient


class TestClass:
    def test_access_token(self, client: TestClient) -> None:

        r = client.get("/")

        assert r.json() == {"message": "Hello World"}
