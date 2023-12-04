import streamlit as st
import pandas as pd
import os
import streamlit as st

st.title('あなたにおすすめのお城紹介します')

st.write('あなたの出身県はどこですか？昔の国名に変換します。')

df = pd.read_excel('旧国名　変換.xlsx')

# df = pd.read_excel(file_path, header=None, names=['都道府県', '昔の国名'])

# 都道府県の選択
selected_prefecture = st.selectbox('都道府県を選択してください', df['都道府県'])

# 選択された都道府県の昔の国名を表示
old_country_name = df[df['都道府県'] == selected_prefecture]['昔の国名'].values[0]

st.write(f'{selected_prefecture}の昔の国名は {old_country_name} です。')

st.write('あなたは'+(old_country_name)+'出身なんですね！それではおすすめの城をお教えしましょう。下の選択肢を選んでいってください')




def main():
   
    st.subheader("城の好みアンケート")

    # 白色と黒色のボタン
    
    color = st.radio("Q.あなたは何色が好きですか", ["白色", "黒色"])

    # 大きな城が好きかどうかの質問
    
    big_castle_choice = st.radio("Q.城は大きければ大きいほどいいと思いますか？", ["はい", "いいえ"])

    # どちらの武将が好きかの質問
 
    daimyo_name = st.radio("Q.あなたはどちらの戦国武将が好きですか", ["豊臣秀吉", "徳川家康"])



# ユーザーの選択に基づいて最終的なコメントと城を提案

    if color == "白色":
        if big_castle_choice == "はい":
            if daimyo_name == "徳川家康":
                st.write("あなたには姫路城がおすすめです！")
                st.write("姫路城は白鷺(しろさぎ)城と言われ、世界遺産にもなっています。以前、改修工事が行われた時には「白過ぎ城」と呼ばれ、少しお城界隈では話題になりました。今は少し汚れてきて、若干灰色です。ちなみに豊臣秀吉の城というイメージが強いですが実は白色になったのは、徳川家康の時代になってからです。姫路駅から歩く際は、30分以上歩く羽目になるので注意してくださいね")
                st.image("himeji.jpg", caption='姫路城', use_column_width=True)
    if color == "白色":
        if big_castle_choice == "はい":
            if daimyo_name == "豊臣秀吉":
                st.write("あなたには大阪城がおすすめです！")
                st.write("豊臣秀吉と言ったら大阪城ですよね！でも残っている大阪城は、大坂夏の陣の後に徳川家康が立て直したものなんです。今でも大阪城はとても大きいですが、さらに大きかったらしいですよ～")
                st.write("ちなみに大阪城か大坂城２つの漢字がありますよね。「坂」という字には土にかえるという意味があるらしくて、明治の時代に縁起が悪いということで、「阪」の字に変えられたみたいです。")
                st.image("oosaka_yoki.jpg", caption='大阪城', use_column_width=True)
    if color =="黒色":
        if big_castle_choice == "はい":
            if daimyo_name == "豊臣秀吉":
                st.write("あなたには熊本城がおすすめです")
                st.write("熊本城は豊臣秀吉の家臣　加藤清正によって造られた城です。加藤清正は朝鮮出兵で活躍しましたが、食糧が乏しくとても苦労しました。そのため、この熊本城を建築する際には、畳をイモで作り、薪になる木をたくさん植えるなど籠城しても大丈夫なように工夫しました。")
                st.write("熊本城は戦国時代には戦場になりませんでしたが実は幕末に戦場になっています。この熊本城を西郷隆盛が攻めています。大砲などを使って攻撃しましたが、熊本城は全く動じず、50日間籠城して西郷隆盛軍が京都に到着するのを遅らせました。")
                st.image("kumamoto.jpg", caption='熊本城', use_column_width=True)
    if color =="黒色":
        if big_castle_choice == "はい":
            if daimyo_name == "徳川家康":
                st.write("あなたには松山城がおすすめです")
                st.write("松山城は愛媛県にあります。松山城は山の上にあり、少し安定感の悪いリフトで上ることが出来ます。攻められたときに守りやすいようにたくさんの機能が用意されていて、木造などでとても美しい城です。")
                st.write("近くには、日本最古の温泉と言われる道後温泉や「柿食えば　鐘がなるなり　法隆寺」で有名な正岡子規の記念館など１日中回ることが出来ます。ちなみにおすすめの夕食は鯛めしです")
                st.image("matuyama.jpg", caption='松山城', use_column_width=True)
    if color == "白色":
        if big_castle_choice == "いいえ":
            if daimyo_name == "徳川家康":
                st.write("あなたには彦根城がおすすめです")
                st.write("彦根城は滋賀県にあります。松本城や姫路城と同じように国宝に指定されています。城にはひこにゃんというキャラクターが居て、よく城の前でショーを披露しています。めちゃめちゃかわいいんです")
                st.write("彦根城は徳川四天王　井伊の赤鬼で有名な井伊家が築城した城です。彦根城は徳川幕府の重臣である井伊家が治め続け、桜田門外の変で有名な井伊直弼もこの城に居ました。階段はとても急なので、足腰や服装には注意してくださいね" )  
                st.image("hikone_sinn.jpg", caption='彦根城', use_column_width=True)
    if color == "白色":
        if big_castle_choice == "いいえ":
            if daimyo_name == "豊臣秀吉":
                st.write("あなたには長浜城がおすすめです")
                st.write("長浜城は滋賀県の琵琶湖の近くにあります。長浜城は豊臣秀吉が織田信長から初めてもらった城です。ここから豊臣秀吉は出世し始めたので、出世城という縁起のいい城なんです")
                st.write("近くには黒壁スクエアというアーケード街の観光地があって、食べ歩きなどができます。友達とや恋人との旅行の際には行ってみてくださいね。ちなみに長浜城では昔、猿を飼ってました（）")
                st.image("nagahama.jpg", caption='長浜城', use_column_width=True)
    if color =="黒色":
        if big_castle_choice == "いいえ":
            if daimyo_name == "徳川家康":
                st.write("あなたには福山城がおすすめです")
                st.write("福山城は広島県のJR福山駅の新幹線ホームから見ることができます。でも、駅のホームから見ると白色の城なんです。でも、裏から見ると鉄板が貼ってあり、黒色の城なんです。大砲や鉄砲の弾をに負けないように貼り付けたらしいです。")
                st.write ("実は徳川家康の時代の城で黒色はないんです。豊臣秀吉は派手好きだったので、金色が映える黒色が好きだったんですが、徳川家康は現実的で、風雨や火に強い白漆喰を使った城しか作りませんでした。黒色だった城もほとんど白色に塗り替えられています")
                st.image("hukuyama_yoki.jpg", caption='福山城　表', use_column_width=True)        
                st.image("hukuyama.jpg", caption='福山城　裏', use_column_width=True)          
    if color =="黒色":
        if big_castle_choice == "いいえ":
            if daimyo_name == "豊臣秀吉":
                st.write("あなたには松本城がおすすめです")
                st.write("松本城は長野県にある国宝の城です。黒色の城というとまず松本城が出てきますよね。この城を作った人は石川数正という武将で、徳川家康の家臣で、とても大事な役職を任せられていました。でも60歳ぐらいで急に豊臣家に転職した少し変わった武将です。何があったんでしょうね～")
                st.write("ちなみに松本城の水掘りには白鳥が泳いでいます。朝早く行くと出会えることも多いですよ。水掘りには柵がないので落ちないように、あと階段も急なので服装には気を付けてくださいね")
                st.image("matumoto.jpg", caption='松本城', use_column_width=True)
if __name__ == "__main__":
    main()      