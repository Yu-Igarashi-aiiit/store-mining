import janome #形態素解析のフレームワーク
from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.tokenfilter import POSKeepFilter
from janome.charfilter import UnicodeNormalizeCharFilter,RegexReplaceCharFilter
# import requests #HTML解析のフレームワーク
# from bs4 import BeautifulSoup

def store_mining(description:str,reject_symbol=[("[,\.\(\)\{\}\[\]\<\>\○]"," ")]):
    #analyzerの前処理フィルタ生成
    char_filters = [UnicodeNormalizeCharFilter()]
    #reject_symbolは正規化し名詞判定されないようにする
    for i in reject_symbol:
        char_filters.append(RegexReplaceCharFilter(*i))

    #tokenizerの初期化、tokenizerインスタンスは使い回す、ループの外で呼び出し初期化
    tokenizer = Tokenizer()
    #品詞取得フィルタ
    token_filters = [POSKeepFilter(['名詞'])]
    #各種フィルタ設定でanalyze
    analyzer = Analyzer(char_filters,tokenizer,token_filters)
    #リストで返却
    return [token.surface for token in analyzer.analyze(description)]
    # for token in analyzer.analyze(description):
    #     print(token.surface)

description='【主な機能と使い方】＜1.今すぐ呼ぶ＞乗車場所は地図上で簡単に設定できます。その後、必要な台数や降車場所(任意)、Google Payなどの決済方法(任意)を設定すれば配車完了です。アプリには到着までの待ち時間 (あと約○○分)と車両番号が表示されるので、乗るタクシーがすぐに分かり安心です。'
store_mining(description)
