import sys
import json


def get_data(fn):
    with open(fn, "r", encoding="utf-8") as json_file:
        return json.load(json_file)

def set_data(data, fn):
    with open(fn, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, separators=(',', ':'))


def update_queue_3_1_4_to_3_2_0(fn):
    data = get_data(fn)
    
    for song in data["queue"]["p"]:
        # Missing field
        song["is_visible_in_public_playlist"] = True

        # This used to just be "PLAYLIST"
        song["track_type"] = "OWNED_PLAYLIST"

        # This field was removed
        del song["playlist_id"]

    set_data(data, fn)

def pretty_reformat(fn):
    with open(fn, "r+", encoding="utf-8") as json_file:
        data = json.load(json_file)

        json_file.truncate(0)
        # I don't know why python needs this to be here.
        # Why isnt it handled by the truncate method?
        json_file.seek(0)

        json.dump(data, json_file, indent=4)

def update_queue_3_2_2_to_3_2_4(fn):
    data = get_data(fn)

    # Kinda curious about if the app needs this to be correct or not
    data["ref_queue"]["a"] = "DOWNLOADS"
    data["queue"]["u"] = data["queue"]["t"]

    for s in ["queue", "ref_queue"]:
        o = data[s]

        o["q"] = o["p"]
        o["p"] = o["o"]
        del o["o"]
        o["t"] = o["s"]
        del o["s"]
        o["x"] = o["w"]
        o["w"] = o["v"]
        del o["v"]

    set_data(data, fn)


update_queue = update_queue_3_2_2_to_3_2_4

if __name__ == "__main__":
    for fn in sys.argv[1:]:
        update_queue(fn)
