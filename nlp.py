import spacy

def Search_NLP(search):
    # ＜GiNZAモデルをロード＞
    # Languageクラス 変数名をnlpで宣言するのが一般的（spaCy推奨）
    nlp: spacy.Language = spacy.load('ja_ginza')

    # ＜Text文からDocクラスを生成＞
    # text を Doc クラスに変換する
    text: str = search
    doc: spacy.tokens.doc.Doc = nlp(text)

    # 品詞タグから指定した形式の単語を抽出する
    search_NLP = ''
    for token in doc:
        if token.pos_ in ['NOUN', 'PROPN', 'ADJ']: # NOUNが名詞、PROPNが固有名詞、ADJが形容詞、
            print(token.text, token.tag_, type(token))
            if not search_NLP:
                search_NLP = token.text
            else:
                search_NLP += ' AND ' + token.text
                
    return search_NLP