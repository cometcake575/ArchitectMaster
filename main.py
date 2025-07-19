import uuid
from tkinter import Tk
from tkinter.filedialog import askopenfilenames, askdirectory
from json import loads, dumps
from extra_convert import do_extra

Tk().withdraw()
files = askopenfilenames(filetypes=[('JSON Files', '.json')])
savedir = askdirectory()

architect_data = {}

conversion_info = loads(open("conversion_info.json").read())


def convert_name(decomaster_name: str) -> [str, float]:
    if decomaster_name not in conversion_info:
        return None
    return conversion_info[decomaster_name]

for file in files:
    data = loads(open(file, "r").read())["items"]
    if "$values" in data:
        data = data["$values"]
    for item in data:
        scene = item["sceneName"]
        if scene not in architect_data:
            architect_data[scene] = []

        name = item["pname"]
        conversion = convert_name(name)
        if conversion is None:
            continue

        new_object = {"placement": {"name": conversion[0], "flipped": False}}

        if "angle" in item and item["angle"] != 0:
            new_object["placement"]["rotation"] = float(item["angle"])
        if "size" in item and item["size"] != 1:
            new_object["placement"]["scale"] = item["size"]

        new_object["placement"]["pos"] = {}
        if "Center" in item:
            new_object["placement"]["pos"]["x"] = item["Center"]["x"]
            new_object["placement"]["pos"]["y"] = item["Center"]["y"]
        else:
            new_object["placement"]["pos"]["x"] = item["position"]["x"]
            new_object["placement"]["pos"]["y"] = item["position"]["y"]

        new_object["placement"]["pos"]["z"] = conversion[1]

        new_object["placement"]["id"] = str(uuid.uuid4())[:8]

        extr = do_extra(item, new_object)
        if extr is not None:
            architect_data[scene].append(extr)

        architect_data[scene].append(new_object)

for scene in architect_data.keys():
    open(f"{savedir}/{scene}.architect.json", "w").write(dumps(architect_data[scene], indent=2))
