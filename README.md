# VRChat-status-update-by-toggl
このリポジトリーはTogglから作業中のプロジェクトを持ってきて，作業中の場合はVRChatのステータスを変更します.  

#### 作業時  
format : 作業名 25分後の時間(作業の終了時間予測)  

#### 休憩時  
format : Rest-休憩中  

![image](https://user-images.githubusercontent.com/41544743/91630814-ad3bae00-ea0f-11ea-9566-92922f729cdf.png)　　



## 使用するにはVRChatとTogglが必要です．　　

　　
## 必要な情報  
### 1.VRChat: email, password, apiKey, usr-id  
apiKeyの入手の仕方  
https://qiita.com/y23586/items/484c8465b7a966d237c0  
VRC-APIの使用がヨツミさんのやり方だとできなかったのでUA(User-agent)偽装したらできた．

### 2.Toggl: api-token  
API token  
https://toggl.com/app/profile  

##  必要な情報を編集してください  
vrc_toggl_work_update.pyの 「#Modify:」 を探して変更していってください

## VRChat-endpoint  
Update Info  
https://vrchatapi.github.io/#/UserAPI/UpdateInfo?id=endpoint

## UTCを合わせる(協定世界時)  
vrc_toggl_work_update.pyの 「#UTC+?」 を探して 9(日本) から自国の数字にしてください


