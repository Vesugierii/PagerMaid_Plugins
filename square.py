from pagermaid.listener import listener
from pagermaid.utils import alias_command

@listener(is_plugin=True, incoming=True, outgoing=True, command=alias_command("square"),
          description="生成文本矩阵，先行后列,后文本")
async def square(context):
    hang = context.parameter[0]
    hang = int(hang)
    lie = context.parameter[1]
    lie = int(lie)
    text = ""
    result = ""
    for n in range(hang+1):
        if n == hang:
            await context.edit(result)
        else:
            for m in range(lie):
                text += context.parameter[2]
            result += text
            result += "\n"
            text = ""
