# 保存为 server.py
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(f"请求URL: {self.path}")
        query = urllib.parse.urlparse(self.path).query
        params = urllib.parse.parse_qs(query)
        print(f"解析参数: {params}")
        
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'OK')
    
    def log_message(self, format, *args):
        pass  # 禁用默认日志

print("服务器启动在 http://0.0.0.0:8000")
HTTPServer(('0.0.0.0', 8000), Handler).serve_forever()