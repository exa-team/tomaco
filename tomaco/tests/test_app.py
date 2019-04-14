def test_index_should_return_valid(app):
    assert app.get("/").status == "200 OK"


def test_index_should_return_a_hello_world(app):
    result = app.get("/")
    result.mustcontain("Hello world!")
