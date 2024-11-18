## Perplexity-ai-API 这是什么？

一个在互联网进行搜索的插件，[Perplexity](https://www.perplexity.ai/hub/blog/introducing-pplx-api)(以下简称pplx)，使用Python API调用，具体方法查看[perplexity ai文档](https://docs.perplexity.ai/home)

## 安装方法

对机器人输入指令`!plugin get https://github.com/LittleLicy/QchatGPT-perplexity-ai-api.git`安装

## 使用

- 你需要在`config/config.py`中填入你的pplx API Key，[点击此处](https://www.perplexity.ai/hub/blog/introducing-pplx-api)注册pplx账号并在这里[查看你的API](https://www.perplexity.ai/settings/api)，需要账户里有余额才能获取pplx apikey

- 默认的模型`llama-3.1-sonar-small-128k-online`价格为**百万token/0.2刀**

- 计费详细请看[文档](https://docs.perplexity.ai/guides/pricing)

```python

# config.py
# API_KEY获取：https://www.perplexity.ai/hub/blog/introducing-pplx-api

API_KEY = "<your_pplx_api>"  # 替换为你的实际API密钥
API_URL = "https://api.perplexity.ai/chat/completions"

```

- 模型切换：支持多个llama模型，具体查看[这里](https://docs.perplexity.ai/guides/model-cards)

- 修正：近期的更新，API可以返回搜索来源，具体请看[这里](https://docs.perplexity.ai)，去掉了`"return_citations"`的参数，现在搜索默认返回引用url。

## 展示

默认`llama-3.1-sonar-small-128k-online`模型调用pplx api进行搜索并总结你提问的内容

群聊`@机器人#<你要搜索的内容>`，或者私聊发送机器人`#<你要搜索的内容>`，可以在不使用自己的模型下进行pplx搜索。

![image](https://github.com/user-attachments/assets/00cbc2dc-ba6f-4f02-97f5-f773854712a7)
![image](https://github.com/user-attachments/assets/53a5bf8f-e570-48fc-a52f-b92e05590984)
![image](https://github.com/user-attachments/assets/44a1c9c2-7fca-4eaa-a671-4013e2fc16e4)

## PPLX AI网页版效果

https://www.perplexity.ai/    

![image](https://github.com/user-attachments/assets/deef97b0-58f9-4a34-89b8-614653410910)

## API回答参数修改

你可以在`main.py`修改API回答的参数

```python

#参数参考：https://docs.perplexity.ai/api-reference/chat-completions

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
        "search_domain_filter": ["perplexity.ai"],
        "return_images": False, #确定对在线模型的请求是否应返回图像,需要你的API有pplx的测试资格
        "return_related_questions": False, #同上
        "search_recency_filter": "month", #值包括 month、week、day、hour
        "top_k": 0,
        "stream": False, #API文档的流式输出，不推荐使用，除非你的机器人是官方QQ私聊机器人
        "presence_penalty": 0,
        "frequency_penalty": 1
    }
```

## 其他

- [API仪表盘](https://www.perplexity.ai/settings/api)


