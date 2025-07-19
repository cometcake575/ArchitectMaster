import copy


def do_extra(original: dict, new: dict):
    old_name = original["pname"]

    if old_name == "edge":
        new["config"] = {"collision": "2", "height": "0.015", "width": "3"}

    if old_name == "HK_infinte_soul":
        if "scale" not in new["placement"]:
            new["placement"]["scale"] = 1
        new["placement"]["scale"] *= 1.2245897624
        new["placement"]["pos"]["y"] += 0.66 - new["placement"]["scale"]

    if old_name == "HK_soul_totem":
        if "scale" not in new["placement"]:
            new["placement"]["scale"] = 1
        new["placement"]["scale"] *= 1.3329778726

    if old_name == "lazer_bug":
        if "rotation" not in new["placement"]:
            new["placement"]["rotation"] = 0
        new["placement"]["rotation"] += 90

        new["placement"]["pos"]["y"] += 0.29

    if old_name == "HK_bounce_shroom":
        new["placement"]["flipped"] = True

    if old_name == "HK_crystal_barrel":
        new["placement"]["scale"] = 0.6191183754

    if old_name == "HK_stomper":
        new["listeners"] = [{"type": "stopinstant", "name": "slever"},
                            {"type": "start", "name": "slever", "times": "2"}]

    if old_name == "stomper_switch":
        new["events"] = [{"type": "onpull", "name": "slever"}]

    if old_name == "HK_lore_tablet_1":
        if "scale" not in new["placement"]:
            new["placement"]["scale"] = 1
        new["placement"]["scale"] *= 0.7892307692
        new["placement"]["pos"]["y"] += 1.5
        new["placement"]["flipped"] = True

        new["config"] = {"lore_tabet_content": original["Text"]}

    if old_name == "simple_conveyor":
        on = copy.deepcopy(new)
        new["placement"]["pos"]["x"] -= 2.39
        on["placement"]["pos"]["x"] += 2.39
        return [on]

    if old_name == "white_thorn":
        if "scale" not in new["placement"]:
            new["placement"]["scale"] = 1
        new["placement"]["scale"] *= 0.64

    if old_name == "white_spike":
        if "scale" not in new["placement"]:
            new["placement"]["scale"] = 1
        new["placement"]["scale"] *= 0.622

    if old_name == "back_colorfull_fill":
        if "scale" not in new["placement"]:
            new["placement"]["scale"] = 1
        new["placement"]["scale"] *= 1.2

        new["config"] = {
            "width": original["size_x"],
            "height": original["size_y"],
            "layer": original["Order"],
            "r": original["R"],
            "g": original["G"],
            "b": original["B"]
        }

    if old_name in ("HK_saw", "mary_move_platform", "move_flip_platform"):
        offset = original["offset"]
        speed = original["speed"]
        if speed < 0:
            offset += original["span"]
            speed = -speed
        new["config"] = {
            "mo_track_dist": original["span"],
            "mo_speed": speed * 5,
            "mo_offset": offset,
            "mo_rotation": original["angle"]
        }

    if old_name == "HK_saw":
        if "scale" not in new["placement"]:
            new["placement"]["scale"] = 1
        new["placement"]["scale"] *= 0.75

    if old_name == "zote_wall":
        if "scale" not in new["placement"]:
            new["placement"]["scale"] = 1
        new["placement"]["scale"] *= 0.75

        new["listeners"] = [{"type": "open", "name": "zhead"}]

    if old_name == "zote_detection":
        new["config"] = {"height": "0.2", "width": "1.2", "g": "0", "r": "0", "shape_collision": "2"}
        new["listeners"] = [{"type": "disable", "name": "zhead"}]

        placex = new["placement"]["pos"]["x"]
        placey = new["placement"]["pos"]["y"] + 0.3

        return [{"placement": {"name": "Trigger Zone", "pos": {"x": placex, "y": placey, "z": 0.0}, "flipped": False},
                 "events": [{"type": "zoneenter", "name": "zhead"}],
                 "config": {"height": "0.1", "width": "1.2", "trigger_mode": "3"}}]

    if old_name == "mary_move_platform":
        new["config"]["width"] = 0.625
        new["config"]["height"] = 0.03
        new["config"]["r"] = 0.7
        new["config"]["g"] = 0.5
        new["config"]["b"] = 0.4
        new["config"]["shape_collision"] = 2

    if old_name == "HK_crystal_dropping":
        new["config"] = {
            "falling_crystals_damage": "True",
            "falling_crystals_lifetime": "4",
            "falling_crystals_rate": "1"
        }

    if old_name == "HK_break_wall":
        if "scale" not in new["placement"]:
            new["placement"]["scale"] = 1
        new["placement"]["scale"] *= 1.15

    if old_name == "HK_unbreak_wall":
        if "scale" not in new["placement"]:
            new["placement"]["scale"] = 1
        new["placement"]["scale"] *= 1.15

        new["config"] = {"can_be_broken": "False"}

    if old_name == "HK_lever":
        if "scale" not in new["placement"]:
            new["placement"]["scale"] = 1
        new["placement"]["scale"] *= 0.775

        new["events"] = [{"type": "OnPull", "name": "PullLever" + str(original["Number"])}]
        new["config"] = {"levers_stay_active": "0"}

    if old_name == "HK_gate":
        new["placement"]["flipped"] = True
        new["listeners"] = [{"type": "open", "name": "PullLever" + str(original["Number"])}]

    if old_name == "IMG_Lantern":
        placex = new["placement"]["pos"]["x"]
        placey = new["placement"]["pos"]["y"]

        return [{"placement": {"name": "Lantern Binding", "pos": {"x": placex, "y": placey, "z": 0.0}, "flipped": False}}]

    return None
