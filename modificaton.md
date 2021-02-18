# A Guide On How To Customise Bot Further for Personal Use.

1. [Customising Bot /start Message](https://github.com/iamLiquidX/MirrorX/blob/master/modificaton.md#Customising-Bot-start-Message)
2. [Changing Bot Commands](https://github.com/iamLiquidX/MirrorX/blob/master/modificaton.md#Changing-Bot-Commands)
3. [Changing Max Allowed Downloads & Set Auto Cancel Time If No Seeders Available](https://github.com/iamLiquidX/MirrorX/blob/master/modificaton.md#Changing-Max-Allowed-Downloads-and-Set-Auto-Cancel-Time-If-No-Seeders-Available)
4. [Customising Bot Message When Bot Auto Cancels the Torrent Due to No Seeders are Available](https://github.com/iamLiquidX/MirrorX/blob/master/modificaton.md#Customising-Bot-Message-When-Bot-Auto-Cancels-the-Torrent-Due-to-No-Seeders-are-Available)
5. [Customising Bot Stats Message](https://github.com/iamLiquidX/MirrorX/blob/master/modificaton.md#Customising-Bot-Stats-Message)
6. [Customising Mirror Status](https://github.com/iamLiquidX/MirrorX/blob/master/modificaton.md#Customising-Mirror-Status)
7. [Customising Mirror Progress Bar](https://github.com/iamLiquidX/MirrorX/blob/master/modificaton.md#Customising-Mirror-Progress-Bar)
8. [Customising Bot status Message](https://github.com/iamLiquidX/MirrorX/blob/master/modificaton.md#Customising-Bot-status-Message)
9. [Customising Bot After Download Complete Message](https://github.com/iamLiquidX/MirrorX/blob/master/modificaton.md#Customising-Bot-After-Download-Complete-Message)


# Customising Bot /start Message
:octocat: In Order to Customise Bot Start Message You have to Edit few lines in `__main__.py` file. 

You Can Find `__main__.py` File Here ⬇️
```
MirrorX/bot/__main__.py
or
https://github.com/iamLiquidX/MirrorX/blob/master/bot/__main__.py
```
In Order to Customise the way you want the start Message of Bot,  modify  `line 46` & `line 47` from `__main__.py` file 

🔗 [Line 46 can be Opened from here](https://github.com/iamLiquidX/MirrorX/blob/097a69e3b7aa7e8aad0c91de8b07877933ef6f34/bot/__main__.py#L46)

![start Message](https://i.ibb.co/7QmMWjM/start-message-init.png)



### Example :
Below is the Just an Example of How I Customised start message of my Bot. This is Just to Give you an Idea, You can Customise as You like.

![final start Message](https://i.ibb.co/pxVxbcX/start-message-final.png)


# Changing Bot Commands
:octocat: In Order to Customise Bot Commands, You have to Edit Commands in `bot_commands.py` File.
You Can Find `bot_commands.py` File Here ⬇️
```
MirrorX/bot/helper/telegram_helper/bot_commands.py
or
https://github.com/iamLiquidX/MirrorX/blob/master/bot/helper/telegram_helper/bot_commands.py
```
### Example :
I Changed My Bot Commands Like Following. You Can easily understand by looking at & edit as you want them.

![Bot_Commands](https://i.ibb.co/fHKCLN5/botcommands.png)

# Changing Max Allowed Downloads and Set Auto Cancel Time If No Seeders Available
:octocat: In Order to Change Max Allowable Torrents at a Time & Auto Cancel If No Seeders are Available, You Have to Edit `aria.sh` file

### Max Allowed Downloads
You can limit maximum concurrent downloads by changing the value of `MAX_CONCURRENT_DOWNLOADS` in `aria.sh` file. By default, it's set to 7
### Auto Cancel a Torrent 
You can Set the Bot to Auto Cancel a Torrent, If No Seeders are Available by changing the value of `--bt-stop-timeout` in `aria.sh` file. By default, it's set to 1200. ( It means after 1200 Seconds, Torrent will get Auto Cancelled)
### If You Don't want the Bot To Auto Cancel The Torrent If No Seeders Availabe

You Have to remove  `--bt-stop-timeout=1200` from `Line 17` in `aria.sh` file.

🔗 [Line 17 Can be Opened from Here](https://github.com/iamLiquidX/MirrorX/blob/097a69e3b7aa7e8aad0c91de8b07877933ef6f34/aria.sh#L17)

See the Below Image and Remove the High Lighted Text from `aria.sh`

![no auto cancel](https://i.ibb.co/Pm4kj3F/aria-sh-auto-stop.png)

# Customising Bot Message When Bot Auto Cancels the Torrent Due to No Seeders are Available
:octocat: In Order to edit Bot Auto Cancel Message, You Have to Edit `aria2_download.py` file.

You Can Find the `aria2_download.py` file Here ⬇️

```
MirrorX/bot/helper/mirror_utils/download_utils/aria2_download.py
or
https://github.com/iamLiquidX/MirrorX/blob/master/bot/helper/mirror_utils/download_utils/aria2_download.py
```
The Line Which You Have to Edit is `Line 65` 
🔗 [Line 65 can be opened from here](https://github.com/iamLiquidX/MirrorX/blob/097a69e3b7aa7e8aad0c91de8b07877933ef6f34/bot/helper/mirror_utils/download_utils/aria2_download.py#L65)

### Example: 
This is How I Modified Auto Cancel Message. You Can Modify as You Like.
```
𝐘𝐨𝐮𝐫 𝐓𝐨𝐫𝐫𝐞𝐧𝐭 𝐇𝐚𝐬 𝐍𝐨 𝐒𝐞𝐞𝐝𝐬, ⚠️ 𝐃𝐞𝐚𝐝 𝐓𝐨𝐫𝐫𝐞𝐧𝐭 !
```

![Auto cancel](https://i.ibb.co/qrJmg1p/Auto-Cancel.png)

# Customising Bot Stats Message
:octocat: In Order to Customise stats Message, You have to Edit few lines in `__main__.py` file. 

You Can Find `__main__.py` File Here ⬇️
```
MirrorX/bot/__main__.py
or
https://github.com/iamLiquidX/MirrorX/blob/master/bot/__main__.py
```
The Lines Which You Have to Edit are from  `Line 31` to `Line 39` . You can Customise the emojis and Words .
### Note: Don't Change Anything Which is written in `{ }` , Unless you know what you are doing.
🔗 [Line 31 to 39 can be opened from here](https://github.com/iamLiquidX/MirrorX/blob/097a69e3b7aa7e8aad0c91de8b07877933ef6f34/bot/__main__.py#L31)

![stats message](https://i.ibb.co/f0fMtV9/stats.png)

# Customising Mirror Status
:octocat: In Order To Customise MirrorStatus, You Have to Edit `Line 17` to `Line 23` in `bot_utils.py` file.
You Can Find `bot_utils.py` File Here ⬇️
```
MirrorX/bot/helper/ext_utils/bot_utils.py
or
https://github.com/iamLiquidX/MirrorX/blob/master/bot/helper/ext_utils/bot_utils.py
```
🔗 [Line 17 to 23 can be opened from here](https://github.com/iamLiquidX/MirrorX/blob/097a69e3b7aa7e8aad0c91de8b07877933ef6f34/bot/helper/ext_utils/bot_utils.py#L17)

![MirrorStatus](https://i.ibb.co/pzYSym7/mirrorstatus.png)

# Customising Mirror Progress Bar
:octocat: In Order To Customise Mirror Progress Bar, You Have to Edit `Line 27` ,`Line 84` & `Line 87` in `bot_utils.py` file.
You Can Find `bot_utils.py` File Here ⬇️
```
MirrorX/bot/helper/ext_utils/bot_utils.py
or
https://github.com/iamLiquidX/MirrorX/blob/master/bot/helper/ext_utils/bot_utils.py
```
🔗 [Line 27](https://github.com/iamLiquidX/MirrorX/blob/097a69e3b7aa7e8aad0c91de8b07877933ef6f34/bot/helper/ext_utils/bot_utils.py#L27)
In Line 27 Replace `▓` with the character of your Choice. This Character is Seen When Download Completes.

🔗 [Line 84](https://github.com/iamLiquidX/MirrorX/blob/097a69e3b7aa7e8aad0c91de8b07877933ef6f34/bot/helper/ext_utils/bot_utils.py#L84)
In Line 84 Replace `▓` with the character of your Choice. This Character will Indicate the Downloaded Part.

🔗 [Line 87](https://github.com/iamLiquidX/MirrorX/blob/097a69e3b7aa7e8aad0c91de8b07877933ef6f34/bot/helper/ext_utils/bot_utils.py#L87)
In Line 84 Replace `░` with the character of your Choice. This Character Will Indicate the Incomplete Download Part

![Progress Bar](https://i.ibb.co/CWFLLgS/progress-bar.png)


# Customising Bot status Message
:octocat: In Order To Customise Bot status Message, You Have to Edit `Line 96` to `Line 112` in `bot_utils.py` file.

You Can Find `bot_utils.py` File Here ⬇️
```
MirrorX/bot/helper/ext_utils/bot_utils.py
or
https://github.com/iamLiquidX/MirrorX/blob/master/bot/helper/ext_utils/bot_utils.py
```
### Note: Don't Change Anything Which is written in `{ }` , Unless you know what you are doing.

![Bot Status Message](https://i.ibb.co/QmV34dQ/bot-status-message.png)

### Example : This Is How It Looks ⬇️
![botstatus](https://i.ibb.co/tXfzWH1/bot-status-message-bot.png)


# Customising Bot After Download Complete Message
:octocat: In Order To Customise Bots Message after Downnload Complete, You Have to Edit `Line 149` to `Line 177` in `mirror.py` file.
You Can Find `mirror.py` File Here ⬇️
```
MirrorX/bot/modules/mirror.py
or
https://github.com/iamLiquidX/MirrorX/blob/master/bot/modules/mirror.py
```
🔗 [Line 149](https://github.com/iamLiquidX/MirrorX/blob/097a69e3b7aa7e8aad0c91de8b07877933ef6f34/bot/modules/mirror.py#L149)

![mirror.py](https://i.ibb.co/JtscvmM/mirror-py-init.png)

### This Is an Example, How I Edited Mine ⬇️
![mirror.py edited](https://i.ibb.co/bXrkTRf/mirror-py-edited.png)

### Output of Edited Mirror.py file from Bot Message
![mirror.py output](https://i.ibb.co/NspTKW7/mirror-py-output.png)



### *This is Just a Small Guide using which small small Customisations can be made in Mirror Bot.*
### *I Hope It is Helpful to Beginners.*
### *If I Missed any Part, You can request for that.*
