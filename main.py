from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import cgi

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()

            images = [img for img in os.listdir(UPLOAD_DIR) if img != ".gitignore"]
            image_tags = ''.join([f'<div class="image-container"><img src="/uploads/{img}"></div>' for img in images])

            html_content = f'''
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Image Upload</title>
                <style>
                    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
                    body {{ font-family: Arial, sans-serif; background-color: #f0f0f5; display: flex; align-items: center; justify-content: center; flex-direction: column; }}
                    .container {{ max-width: 800px; width: 100%; padding: 1em; background: #fff; border-radius: 8px; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15); }}
                    h2 {{ text-align: center; margin-bottom: 1em; }}
                    form {{ display: flex; justify-content: center; margin-bottom: 20px; }}
                    input[type="file"] {{ margin-right: 10px; }}
                    button {{ padding: 8px 16px; background-color: #007bff; color: #fff; border: none; border-radius: 4px; cursor: pointer; }}
                    button:hover {{ background-color: #0056b3; }}
                    .gallery {{ display: flex; flex-wrap: wrap; gap: 10px; justify-content: center; }}
                    .image-container {{ width: 150px; height: 150px; overflow: hidden; border-radius: 8px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); }}
                    .image-container img {{ width: 100%; height: 100%; object-fit: cover; }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h2>Image Upload Gallery</h2>
                    <form enctype="multipart/form-data" method="post" action="/upload">
                        <input type="file" name="file" accept="image/*" required>
                        <button type="submit">Upload Image</button>
                    </form>
                    <div class="gallery">
                        {image_tags}
                    </div>
                </div>
            </body>
            </html>
            '''
            self.wfile.write(html_content.encode())
        elif self.path.startswith("/uploads/"):

            image_path = self.path.lstrip("/")
            if os.path.exists(image_path):
                self.send_response(200)
                self.send_header("Content-Type", "image/jpeg")
                self.end_headers()
                with open(image_path, "rb") as f:
                    self.wfile.write(f.read())
            else:
                self.send_response(404)
                self.end_headers()

    def do_POST(self):
        if self.path == "/upload":
            content_type = self.headers['Content-Type']
            if "multipart/form-data" in content_type:
                form = cgi.FieldStorage(fp=self.rfile, headers=self.headers, environ={'REQUEST_METHOD': 'POST'})
                file_item = form['file']

                if file_item.filename:
                    file_path = os.path.join(UPLOAD_DIR, file_item.filename)
                    with open(file_path, "wb") as output_file:
                        output_file.write(file_item.file.read())

                    self.send_response(303)
                    self.send_header("Location", "/")
                    self.end_headers()
                else:
                    self.send_response(400)
                    self.end_headers()
                    self.wfile.write(b"File upload failed.")

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print("Server running on port 8000...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
