import requests
from pkg.plugin.context import register, handler, BasePlugin, APIHost, EventContext
from pkg.plugin.events import *  # 导入事件类
from .config import config  # 导入配置文件

# PPLX API调用函数
# 支持的模型如下：https://docs.perplexity.ai/guides/model-cards
# Sonar模型 搜索互联网
# llama-3.1-sonar-small-128k-online 127,072
# llama-3.1-sonar-large-128k-online 127,072
# llama-3.1-sonar-huge-128k-online 127,072
# 聊天模型
# llama-3.1-sonar-small-128k-chat 127,072
# llama-3.1-sonar-large-128k-chat 127,072
# 开源模型
# llama-3.1-8b-instruct 131,072
# llama-3.1-70b-instruct 131,072
async def call_pplx_api(query: str) -> str:
    url = config.API_URL  # 从配置文件获取API URL
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
        "max_tokens": 4000,  #参数参考：https://docs.perplexity.ai/api-reference/chat-completions
        "temperature": 0.2,
        "top_p": 0.9,
        "return_citations": True,
        "search_domain_filter": ["perplexity.ai"],
        "return_images": False,
        "return_related_questions": False,
        "search_recency_filter": "month",
        "top_k": 0,
        "stream": False, #流式输出，不推荐使用
        "presence_penalty": 0,
        "frequency_penalty": 1
    }
    headers = {
        "Authorization": f"Bearer {config.API_KEY}",  # 从配置文件获取API密钥
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        response.raise_for_status()  # 如果响应状态码不是200，将引发HTTPError

        # 在控制台输出响应内容
        # print(response.json()) # 如果插件有问题，尝试取消注释掉这一行
        
        return response.json().get('choices', [{}])[0].get('message', {}).get('content', 'No content')
    except requests.exceptions.HTTPError as e:
        error_code = e.response.status_code
        print(f"HTTP error: {error_code}, Response: {e.response.text}")
        return f"你的API_KEY无效或者不正确，请查看控制台报错代码，错误代码: {error_code}"
    except Timeout:
        print("请求超时")
        return "请求超时，可能是网络连接或者是perplexity.ai出现了问题，请稍后重试"
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return "你的API_KEY无效或者不正确，请查看控制台报错代码，错误代码: 500"

# 注册插件
@register(name="PPLXSearchPlugin", description="使用perplexity.ai搜索互联网的插件", version="0.1", author="Licy12138")
class PPLXSearchPlugin(BasePlugin):

    def __init__(self, host: APIHost):
        self.host = host  

    async def initialize(self):
        pass

    async def handle_message(self, ctx: EventContext):
        msg = ctx.event.text_message
        if msg.startswith("#"):
            if not config.API_KEY:
                ctx.add_return("reply", ["你的API_KEY为空，请在config配置你的API_KEY"])
                ctx.prevent_default()
                return
            
            query = msg[1:]  # 去掉#
            result = await call_pplx_api(query)
            ctx.add_return("reply", [result])
            ctx.prevent_default()

    @handler(PersonNormalMessageReceived)
    async def person_normal_message_received(self, ctx: EventContext):
        await self.handle_message(ctx)

    @handler(GroupNormalMessageReceived)
    async def group_normal_message_received(self, ctx: EventContext):
        await self.handle_message(ctx)

    def __del__(self):
        pass
