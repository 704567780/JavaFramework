import threading

from flask import Flask, render_template_string, jsonify

import wyyx
from wyyx import update_clipboard
app = Flask(__name__)

@app.route('/')
def index():
    # 渲染一个带有JavaScript的HTML页面
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Auto Refresh Based on Text Change</title>
    </head>
    <body>
        <h1 id="text-container" style="font-size: 16px;">{{ initial_text }}</h1>
        <script type="text/javascript">
            function pollServerForTextChanges() {
                // 使用fetch API轮询服务器以获取最新的文本
                fetch('/get_text')
                    .then(response => response.json())
                    .then(data => {
                        // 使用最新的文本更新DOM
                        document.getElementById('text-container').innerText = data.text;
                    })
                    .catch(error => console.error('Error:', error));
                // 每5秒钟轮询一次
                setTimeout(pollServerForTextChanges, 5000);
            }
            // 页面加载后立即开始轮询
            window.onload = pollServerForTextChanges;
        </script>
    </body>
    </html>
"""
    # 这里我们将initial_text作为模板变量传递，以便在页面加载时显示
    return render_template_string(html, initial_text=wyyx.text)

@app.route('/get_text')
def get_text():
    # 这个API端点返回当前的text值
    return jsonify({'text': wyyx.text})

# 创建线程对象，但此时线程还没有启动
clipboard_thread = threading.Thread(target=update_clipboard)

if __name__ == '__main__':
    # 创建一个线程来执行update_clipboard函数
    # 启动update_clipboard函数所在的线程
    clipboard_thread.start()
    app.run(debug=True)