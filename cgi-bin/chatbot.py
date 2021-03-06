#!/usr/bin/env python3
import cgi
from botengine import make_reply
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

form = cgi.FieldStorage()

def main():
    m = form.getvalue("m", default="")
    if   m == "": show_form()
    elif m == "say": api_say()

def api_say():
    print("Content-type: text/plain; charset=utf-8")
    print("")
    txt = form.getvalue("txt", default="")
    if txt == "": return
    res = make_reply(txt)
    print(res)

def show_form():
    print("Content-Type: text/html; charset=UTF-8")
    print("")
    print("""
        <html><meta charset="UTF-8"><body>
        <script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>
        <style>
            h1 { background-color: #ffe0e0; }
            div { padding:10px; }
            span { border-radius: 10px; background-color: #ffe0e0; padding: 8px; }
            .bot { text-align: left; }
            .usr { text-align: right; }
        </style>
        <h1>チャットボットと会話しよう</h1>
        <div id="chat"></div>
        <div class='usr'><input id="txt" size="40">
        <button onclick="say()">発言</button></div>
        <script>
        var url = "./chatbot.py";
        function say() {
            var txt = $('#txt').val();
            $.get(url, {"m": "say", "txt": txt},
            function(res) {
                var html = "<div class='usr'><span>" + esc(txt) +
                "</span>:あなた</div><div class='bot'>ボット:<span>" +
                esc(res) + "</span></div>";
                $('#chat').html($('#chat').html()+html);
                $('#txt').val('').focus();
            });
        }
        function esc(s) {
            return s.replace('&', '&amp;').replace('<', '&lt;')
                    .replace('>', '&gt;');
        }
        </script></body></html>
        """)

main()

