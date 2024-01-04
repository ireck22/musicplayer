# musicplayer
python寫的聲控點歌音樂播放系統

<h1>系統流程:</h1>
<ul>
    <li>1說ok音樂</li>
    <li>2語音辨識ok音樂 </li>
    <li>3去雲端抓連結</li>
        <ol>
            <li>去youtube抓</li>
            <li>重組網址</li>
        </ol>    
    <li>4把網址放到程式中</li>
        <ol>
            <li>把url傳到omxplayer</li>    
            <li>當歌曲找到後就會說出歌曲以找到了</li>    
        </ol>
    <li>5播放過程中</li>
        <ol>
            <li>講我要切歌就會觸發執行緒，就會清除omxplayer的執行緒和主程式</li>
            <li>重新跑一次主程式</li>
        </ol>   
</ul>