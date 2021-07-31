from pagermaid.listener import listener
from pagermaid.utils import alias_command

@listener(is_plugin=True, incoming=True, outgoing=True, command=alias_command("square"),
          description="生成文本矩阵")
async def square(context):
    num = context.parameter[0]
    num = int(num)
    text = ""
    result = ""
    for n in range(num+1):
        if n == num:
            await context.edit(result)
        else:
            for m in range(num):
                text += context.parameter[1]
            result += text
            result += "\n"
            text = ""
