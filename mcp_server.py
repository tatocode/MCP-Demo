from datetime import datetime
from openai import OpenAI
import os
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

load_dotenv()

mcp = FastMCP("current time")


def llm(query: str) -> str:
    sys_prompt: str = """你是一个特色美食推荐官，用户每次会输入一个地名，然后请你输出当地的特色美食。
    在输出时，请你注意以下要求：
    * 请直接输出推荐的特色美食即可，不需要任何额外的、不必要的解释。
    """
    openai = OpenAI(
        api_key=os.getenv("API-KEY"),
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )
    response = openai.chat.completions.create(
        model="qwen-turbo",
        messages=[
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": query},
        ],
    )
    ret: str = response.choices[0].message.content

    return ret


@mcp.tool()
def get_current_time() -> str:
    """获取当前时间。

    Returns:
        str: 当前时间的字符串，格式为：“xxxx年xx月xx日 xx:xx:xx”。
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


@mcp.tool()
def location() -> str:
    """获取当前所在地。

    Returns:
        str: 所在地名字符串。
    """
    return "成都"


@mcp.tool()
def recommend_food(place_name: str) -> str:
    """特色美食推荐。根据输入的地名，输出当地的特色美食。

    Args:
        place_name (str): 地名字符串。

    Returns:
        str: 字符串，对应输入地的推荐特色美食。
    """
    return llm(place_name)


if __name__ == "__main__":
    mcp.run(transport="stdio")
