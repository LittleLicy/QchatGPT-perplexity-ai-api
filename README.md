## Perplexity-ai-API

一个在互联网进行搜索的插件，使用Perplexity ai(以下简称pplx)，具体方法查看[perplexity ai文档](https://docs.perplexity.ai/home)

[API调用](https://docs.perplexity.ai/api-reference/chat-completions) 基于llama的联网功能

## 安装方法

对机器人输入指令`!plugin get https://github.com/LittleLicy/QchatGPT-perplexity-ai-api.git`安装

## 使用

- 你需要在`config/config.py`中填入你的pplx API Key，[点击此处](https://www.perplexity.ai/hub/blog/introducing-pplx-api)注册pplx账号并在这里[查看你的API](https://www.perplexity.ai/settings/api)，每天5次免费搜索，需要账户里有余额才能获取pplx apikey


- 模型切换：支持多个llama模型，具体查看[这里](https://docs.perplexity.ai/guides/model-cards)


- 私聊带`#<你要搜索的内容>`或群聊艾特机器人输入`#<你要搜索的内容>`

## 展示

聊天默认模型`gpt-4o-mini`，使用的是默认`llama-3.1-sonar-small-128k-online`模型调用pplx api进行搜索

![image](https://github.com/user-attachments/assets/ab880688-87e2-4a47-b4bc-3aa9fa8500bd)
![image](https://github.com/user-attachments/assets/306ff091-f333-4140-b35a-9015de1b47e7)
![image](https://github.com/user-attachments/assets/62ed34d4-4e84-4184-a2ea-85ebc3c1ad70)


## PPLX AI网页版效果

https://www.perplexity.ai/    

~网页可以显示其查询来源，API貌似不行:<~

![image](https://github.com/user-attachments/assets/deef97b0-58f9-4a34-89b8-614653410910)

## API回答参数修改

你可以在`main.py`修改API回答的参数

```python

async def call_pplx_api(query: str) -> str:
    url = config.API_URL
    payload = {
        "model": "llama-3.1-sonar-small-128k-online",
        "messages": [
            {
                "role": "system",
                "content": "你的回答简洁而精确。"
            },
            {
                "role": "user",
                "content": query
            }
        ],
        "max_tokens": 4000,  # 默认4000
        "temperature": 0.2,
        "top_p": 0.9,
        "return_citations": True,
        "search_domain_filter": ["perplexity.ai"],
        "return_images": False,
        "return_related_questions": False,
        "search_recency_filter": "month",
        "top_k": 0,
        "stream": False, #API文档的流式输出，不推荐使用，除非你的机器人是官方QQ私聊机器人
        "presence_penalty": 0,
        "frequency_penalty": 1
    }
```

![image](https://github.com/user-attachments/assets/d81ec0db-c60b-43b0-9165-35ef92b9a08d)




