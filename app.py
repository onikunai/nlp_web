from flask import Flask, request,render_template
# from deta import Deta
import webbrowser
from nlp import Search_NLP # 自作モジュール

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    # POST処理
    if request.method == 'POST':
        # print("POSTされたIDは？" + str(request.form['id']))
        # print("POSTされたPASSWORDは？" + str(request.form['pwd']))
        # return render_template('form.html')
        search_NLP = Search_NLP(str(request.form['search']))
        print(search_NLP)
        
        # url = 'https://www.google.com/search?q=赤い+AND+丸い+AND+食べ物' # 確認用
        url = 'https://www.google.com/search?q=' + search_NLP
        
        # ブラウザーOpen
        '''
        new・・・0(デフォルト):今までと同じウインドウで開く
        　　　　　1:新しいウインドウ、.open_new()メソッドと同じ動作
        　　　　　2:新しいタブ、.open_new_tab()メソッドと同じ動作
        '''
        webbrowser.open(url, new=2, autoraise=True)
        
        return render_template('form.html')
    # GET処理
    else:
        return render_template('form.html')

# アプリケーションを動かすためのおまじない
if __name__ == "__main__":
    # app.run(port = 8000, debug=True)
    app.run(debug=True,  host='0.0.0.0', port=9999) # ポートの変更