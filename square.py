from pagermaid.listener import listener
from pagermaid.utils import alias_command

@listener(is_plugin=True, incoming=True, outgoing=True, command=alias_command("square"),
          description="生成文本矩形，任意值填东西就带空格分隔",
          parameters="<行> <列> <文本> <任意值>")
async def square(context):
    hang = context.parameter[0]
    hang = int(hang)
    lie = context.parameter[1]
    lie = int(lie)
    desp = ""
    result = ""
    text = context.parameter[2]
    if len(context.parameter) == 4:
        text += " "
    else:
        pass
    for n in range(hang+1):
        if n == hang:
            await context.edit(result)
        else:
            for m in range(lie):
                desp += text
            result += desp
            result += "\n"
            desp = ""
