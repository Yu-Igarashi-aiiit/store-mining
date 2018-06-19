import janome #形態素解析のフレームワーク
from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.tokenfilter import POSKeepFilter
from janome.charfilter import UnicodeNormalizeCharFilter,RegexReplaceCharFilter
import requests #HTML解析のフレームワーク
from bs4 import BeautifulSoup

#文章中から名詞をリストで取得する
def get_keyword(description:str,reject_symbol=[("[,\.\(\)\{\}\[\]\<\>\○]"," ")]):
    #analyzerの前処理フィルタ生成
    char_filters = [UnicodeNormalizeCharFilter()]
    #reject_symbolは正規化し名詞判定されないようにする
    for i in reject_symbol:
        char_filters.append(RegexReplaceCharFilter(*i))

    #tokenizerの初期化、tokenizerインスタンスは使い回す、ループの外で呼び出し初期化
    tokenizer = Tokenizer(mmap=True)
    #品詞取得フィルタ
    token_filters = [POSKeepFilter(['名詞'])]
    #各種フィルタ設定でanalyze
    analyzer = Analyzer(char_filters,tokenizer,token_filters)
    #リストで返却
    return [token.surface for token in analyzer.analyze(description)]
    # for token in analyzer.analyze(description):
    #     print(token.surface)

#対象を示す表現をリストで取得する
def get_attribute(word_list):
    list=[]
    word_list.sort()
    for i in range(0,len(word_list)):
        if ((i == 0) | ((word_list[i] != word_list[i-1])&(i>=1))):
            if((len(word_list[i]) >= 2) & (word_list.count(word_list[i]) >= 2)):
                #print("{h1} = {h2}".format(h1=word_list[i], h2=word_list.count(word_list[i])))
                list += [wordlist[i]]
    return list


description = requests.get("https://ja.wikipedia.org/wiki/マイメロディ")
content = description.content
soup = BeautifulSoup(content,'html.parser')
article = soup.find_all("p")
#find_allはリスト形式を返すため、リストを文字列に変換する
bun=""
for i in range(0,len(article)):
    bun += article[i].getText()
wordlist = get_keyword(bun)
AttributeList = get_attribute(wordlist)
print(AttributeList)
