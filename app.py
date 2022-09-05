import os
from flask import Flask, request,render_template
# from deta import Deta
import webbrowser
from nlp import Search_NLP # 自作モジュール

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    # POST処理
    if request.method == 'POST':
        # 自然言語処理で指定した品詞を抽出
        search_NLP = Search_NLP(str(request.form['search']))
        # print(search_NLP)
        
        # url = 'https://www.google.com/search?q=赤い+AND+丸い+AND+食べ物' # 確認用
        url = 'https://www.google.com/search?q=' + search_NLP
        
        # ローカルのみ動作
        # ブラウザーOpen
        '''
        new・・・0(デフォルト):今までと同じウインドウで開く
        　　　　　1:新しいウインドウ、.open_new()メソッドと同じ動作
        　　　　　2:新しいタブ、.open_new_tab()メソッドと同じ動作
        '''
        # webbrowser.open(url, new=1)
        
        return render_template('jump.html', url=url)
    # GET処理
    else:
        return render_template('form.html')

# アプリケーションを動かすためのおまじない
if __name__ == "__main__":
    # port番号が取得できたら、その番号を使用。取得できなければ、5000とする。
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))