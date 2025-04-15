from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExZDh2ajd5bDlyZ2RtejZ0NndwcjQwb2dyeGl4bXN0M2NldjQzbjY3MyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/CjmvTCZf2U3p09Cn0h/giphy.gif",
    "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExcjljdTk3eTF1dzMwd2Y0cWtlbmtiOGRkNnFqNXF1eG5jZHZ2dzJyNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/MDJ9IbxxvDUQM/giphy.gif",
    "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYWdxN3gxbXF1cGh1dXVrZWJrbXBreG1yZGk3ZGpqYncwNzIzMHhlYSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/mlvseq9yvZhba/giphy.gif",
    "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYWdxN3gxbXF1cGh1dXVrZWJrbXBreG1yZGk3ZGpqYncwNzIzMHhlYSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/lJNoBCvQYp7nq/giphy.gif",
    "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYWdxN3gxbXF1cGh1dXVrZWJrbXBreG1yZGk3ZGpqYncwNzIzMHhlYSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/8vQSQ3cNXuDGo/giphy.gif",
    "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYWdxN3gxbXF1cGh1dXVrZWJrbXBreG1yZGk3ZGpqYncwNzIzMHhlYSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/BBNYBoYa5VwtO/giphy.gif",
    "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYWdxN3gxbXF1cGh1dXVrZWJrbXBreG1yZGk3ZGpqYncwNzIzMHhlYSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/13CoXDiaCcCoyk/giphy.gif",
    "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYWdxN3gxbXF1cGh1dXVrZWJrbXBreG1yZGk3ZGpqYncwNzIzMHhlYSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/q1MeAPDDMb43K/giphy.gif",
    "https://media.giphy.com/media/B7ppUExX92PjW/giphy.gif?cid=ecf05e47yox8c8s6viab2979vbw8kkt7ddvkapjat3a04tt8&ep=v1_gifs_search&rid=giphy.gif&ct=g",
    "https://media.giphy.com/media/12PA1eI8FBqEBa/giphy.gif?cid=ecf05e47ee89hrgzb5f5ow6hpf3jv3ochvowwrg0tkz2yh69&ep=v1_gifs_search&rid=giphy.gif&ct=g",
    "https://media.giphy.com/media/CqVNwrLt9KEDK/giphy.gif?cid=ecf05e47ee89hrgzb5f5ow6hpf3jv3ochvowwrg0tkz2yh69&ep=v1_gifs_search&rid=giphy.gif&ct=g",
    "https://media.giphy.com/media/6C4y1oxC6182MsyjvK/giphy.gif?cid=ecf05e477p2kt2x6egjhx7nxs7wa4thplqvfi90xqriwzx12&ep=v1_gifs_search&rid=giphy.gif&ct=g"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
