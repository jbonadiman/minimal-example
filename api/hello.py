from datetime import datetime
from blacksheep import Application


app = Application()


@app.route("/api/hello")
def home():
    return f"Hello, World! It's {datetime.utcnow().isoformat()}"
