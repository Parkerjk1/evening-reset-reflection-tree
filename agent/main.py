import json

with open("../tree/reflection-tree.json", "r", encoding="utf-8") as f:
    data = json.load(f)

nodes = {node["id"]: node for node in data["nodes"]}
current = data["start"]

answers = {}

while True:
    node = nodes[current]
    ntype = node["type"]

    print("\n" + node["text"])

    if ntype == "end":
        break

    elif ntype == "question":
        options = node["options"]

        for i, opt in enumerate(options, 1):
            print(f"{i}. {opt}")

        choice = int(input("Choose option number: "))
        selected = options[choice - 1]
        answers[current] = selected

        if "nextMap" in node:
            current = node["nextMap"][selected]
        else:
            current = node["next"]

    else:
        input("Press Enter to continue...")
        current = node["next"]
