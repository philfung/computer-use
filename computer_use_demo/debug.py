import json

def debug_msg(s:str):
    print(s)

def dump_obj(obj: object) -> str:
    MAX_LEN = 100
    s = json.dumps(obj, indent=2)
    lines_out = []
    lines = s.split("\n")
    for line in lines:
        if len(line) > MAX_LEN:
            lines_out.append(line[:MAX_LEN] + "...")
        else:
            lines_out.append(line)
    return "\n".join(lines_out)