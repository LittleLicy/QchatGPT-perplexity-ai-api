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
                "content": "Be precise and concise."
            },
            {
                "role": "user",
                "content": query
            }
        ],
        "max_tokens": 4000,  # 可根据需要调整
        "temperature": 0.2,
        "top_p": 0.9,
        "return_citations": True,
        "search_domain_filter": ["perplexity.ai"],
        "return_images": False,
        "return_related_questions": False,
        "search_recency_filter": "month",
        "top_k": 0,
        "stream": False,
        "presence_penalty": 0,
        "frequency_penalty": 1
    }
    headers = {
        "Authorization": f"Bearer {config.API_KEY}",  # 从配置文件获取API密钥
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # 如果响应状态码不是200，将引发HTTPError
        return response.json().get('choices', [{}])[0].get('message', {}).get('content', 'No content')
    except requests.exceptions.HTTPError as e:
        return f"HTTP error: {e.response.status_code}, Response: {e.response.text}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

# 注册插件
@register(name="PPLXSearchPlugin", description="Plugin to search using PPLX API", version="0.1", author="Licy12138")
class PPLXSearchPlugin(BasePlugin):

    def __init__(self, host: APIHost):
        self.host = host  # 保存主机实例

    async def initialize(self):
        pass

    async def handle_message(self, ctx: EventContext):
        msg = ctx.event.text_message
        if msg.startswith("#"):
            if not config.API_KEY:
                ctx.add_return("reply", ["错误：请填写你的API_KEY"])
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
