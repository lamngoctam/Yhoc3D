"""Local preview server for Yhoc3D. Forces correct MIME types (Windows maps .js to text/plain)."""
import http.server, socketserver, sys
H = http.server.SimpleHTTPRequestHandler
H.extensions_map.update({'.js': 'text/javascript', '.mjs': 'text/javascript', '.json': 'application/json',
                         '.webp': 'image/webp', '.glb': 'model/gltf-binary', '.css': 'text/css'})
port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
print('Open http://localhost:%d' % port)
socketserver.TCPServer(('', port), H).serve_forever()
