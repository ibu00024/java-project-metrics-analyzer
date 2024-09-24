import requests
from flask import Flask, render_template, request, redirect, url_for
import os
import uuid
import shutil
from git import Repo
import logging

logging.basicConfig(level=logging.ERROR)

app = Flask(__name__)

JAVA_ANALYZER_URL = os.getenv('JAVA_ANALYZER_URL')

SHARED_VOLUME_PATH = "/shared"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        repo_url = request.form.get('repo_url')
        if not repo_url:
            return render_template('index.html', error="リポジトリのURLを入力してください。")

        # TODO: this is a simple check
        if not repo_url.startswith("https://github.com/"):
            return render_template('index.html', error="有効なGitHubリポジトリのURLを入力してください。")

        try:
            repo_id = str(uuid.uuid4())
            repo_path = os.path.join(SHARED_VOLUME_PATH, repo_id)
            os.makedirs(repo_path, exist_ok=True)

            Repo.clone_from(repo_url, repo_path)

            data = {'repo_path': repo_path}
            response = requests.post(JAVA_ANALYZER_URL, data=data)

            if response.status_code != 200:
                return render_template('index.html', error="解析に失敗しました。")

            metrics = parse_metrics(response.text)

            return render_template('results.html', metrics=metrics, repo_url=repo_url)

        except Exception as e:
            logging.error(f"エラーが発生しました: {str(e)}")
            return render_template('index.html', error="エラーが発生しました。もう一度お試しください。")

    return render_template('index.html')

def parse_metrics(output):
    metrics = {}
    for line in output.splitlines():
        if "Metric" in line or "----" in line:
            continue
        if line.strip():
            parts = line.split()
            metric_name = " ".join(parts[:-1])
            count = parts[-1]
            metrics[metric_name] = count
    return metrics

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
