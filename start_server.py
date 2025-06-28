#!/usr/bin/env python3
import http.server
import socketserver
import webbrowser
import threading
import time
import os

PORT = 9090
os.chdir('/mnt/c/Users/millz/vib34d-editor-dashboard-2025-06-26')

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass  # Quiet

def open_browser():
    time.sleep(2)
    try:
        print("🌐 Opening modular dashboard...")
        webbrowser.open(f'http://localhost:{PORT}/VIB34D_EDITOR_DASHBOARD_MODULAR.html')
    except:
        pass

if __name__ == "__main__":
    try:
        with socketserver.TCPServer(('', PORT), Handler) as httpd:
            print(f"🚀 VIB34D Dashboard Server LIVE!")
            print(f"📍 Modular Dashboard: http://localhost:{PORT}/VIB34D_EDITOR_DASHBOARD_MODULAR.html")
            print(f"📍 Original Dashboard: http://localhost:{PORT}/VIB34D_EDITOR_DASHBOARD.html") 
            print(f"📍 Test Page: http://localhost:{PORT}/test_editor_dashboard.html")
            print("")
            print("✅ Modular version should work without syntax errors!")
            
            browser_thread = threading.Thread(target=open_browser)
            browser_thread.daemon = True
            browser_thread.start()
            
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n✅ Server stopped")
    except Exception as e:
        print(f"❌ Error: {e}")