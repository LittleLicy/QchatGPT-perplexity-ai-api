## Perplexity-API

一个在互联网进行搜索的插件，使用Perplexity API(以下简称pplx)，具体方法查看[perplexity文档](https://docs.perplexity.ai/home)

[API调用](https://docs.perplexity.ai/api-reference/chat-completions) 基于llama的联网功能

## 安装方法

对机器人输入指令`!plugin get https://github.com/LittleLicy/QchatGPT-perplexity-api.git`安装

## 使用

- 你需要在`config/config.py`中填入你的pplx API Key，[点击此处](https://www.perplexity.ai/hub/blog/introducing-pplx-api)注册pplx账号并在这里[查看你的API](https://www.perplexity.ai/settings/api)，每天5次免费搜索，需要账户里有余额才能获取pplx apikey


- 模型切换：支持多个llama模型，具体查看[这里](https://docs.perplexity.ai/guides/model-cards)


- 私聊带`#<你要搜索的内容>`或群聊艾特机器人输入`#<你要搜索的内容>`

## 展示

聊天默认模型`gpt-4o-mini`，使用的是默认`llama-3.1-sonar-small-128k-online`模型调用pplx api进行搜索

![image](https://github.com/user-attachments/assets/306ff091-f333-4140-b35a-9015de1b47e7)
![image](https://github.com/user-attachments/assets/62ed34d4-4e84-4184-a2ea-85ebc3c1ad70)


## PPLX网页版效果

https://www.perplexity.ai/

![image](https://github.com/user-attachments/assets/d81ec0db-c60b-43b0-9165-35ef92b9a08d)




