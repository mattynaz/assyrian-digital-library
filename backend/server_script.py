import modal
from utils import parse_texts, search_texts

app = modal.App(name="assyrian-digital-library")

@app.cls(mounts=[modal.Mount.from_local_dir("./texts", remote_path="/texts")])
class WebApp:
    @modal.enter()
    def startup(self):
        self.texts = parse_texts("/texts")  
        print(f"Loaded {len(self.texts)} texts")
        for text in self.texts:
            print(text)

    @modal.web_endpoint(method="POST")
    def web(self, data: dict) -> str:
        query = data.get("query", "")
        return search_texts(query, self.texts)
