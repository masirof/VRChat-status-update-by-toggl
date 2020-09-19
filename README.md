# VRChat-status-update-by-toggl
このリポジトリーはTogglから作業中のプロジェクトを持ってきて，作業中の場合はVRChatのステータスを変更します.  

#### 作業時  
format : 作業名 25分後の時間(作業の終了時間予測)  

#### 休憩時  
format : Rest-休憩中  

![image](https://user-images.githubusercontent.com/41544743/91630814-ad3bae00-ea0f-11ea-9566-92922f729cdf.png)　　



## 使用するにはVRChatとTogglが必要です.  


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

## VRChat-endpoint(APIを叩く時に使用するURL)  
Update Info  
https://vrchatapi.github.io/#/UserAPI/UpdateInfo?id=endpoint

## UTCを合わせる(協定世界時)  
vrc_toggl_work_update.pyの 「#UTC+?」 を探して 9(日本) から自国の数字にしてください  



# VRChat-status-update-by-toggl
This repository brings the project you're working on from Toggl and changes the status of VRChat if you're working on it.

#### When working　
format : Work-name Time after 25 minutes (estimated time to finish work)　

#### When resting 
format : Rest-休憩中 

![image](https://user-images.githubusercontent.com/41544743/91630814-ad3bae00-ea0f-11ea-9566-92922f729cdf.png)　　
  
## You need VRChat and Toggl to use it.  
  
## Information you need 
### 1.VRChat: email, password, apiKey, usr-id  
How to get an apiKey  
https://qiita.com/y23586/items/484c8465b7a966d237c0  
This way, I couldn't do it.  
I was not able to use VRC-API, but I was able to use it by Camouflage the UA (User-agent).  

### 2.Toggl: api-token  
API token  
https://toggl.com/app/profile  

## Please edit the information you need  
Look for the "#Modify:" comment in vrc_toggl_work_update.py and make your changes.  

## VRChat-endpoint(The URL to use when useing the API)  
Update Info  
https://vrchatapi.github.io/#/UserAPI/UpdateInfo?id=endpoint  

## Set to UTC (Coordinated Universal Time)    
Look for "#UTC+?" in vrc_toggl_work_update.py and change it from 9 (Japan) to your country's number.  
