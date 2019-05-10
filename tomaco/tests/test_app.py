class TestStatic:
    def test_css_file_should_return_valid(self, app):
        assert app.get("/static/css/main.css").status == "200 OK"


class TestIndex:
    def test_index_should_return_valid(self, app):
        assert app.get("/").status == "200 OK"

    def test_index_should_contain_the_app_name(self, app):
        result = app.get("/")
        result.mustcontain("Tomaco")
