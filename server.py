import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler
Handler.extensions_map.update({
    '.pdf': 'application/pdf',
})

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Сервер запущен на порту {PORT}")
    print(f"Откройте http://localhost:{PORT} в вашем браузере")
    httpd.serve_forever() 