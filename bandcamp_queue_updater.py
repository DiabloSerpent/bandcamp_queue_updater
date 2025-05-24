import sys
import json


def update_queue(fn):
    with open(fn, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
    
    for song in data["queue"]["p"]:
        song["is_visible_in_public_playlist"] = True
        song["track_type"] = "OWNED_PLAYLIST"
        del song["playlist_id"]

    with open(fn, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, separators=(',', ':'), ensure_ascii=False)
        # Add "indent=2" to see prettier output in file


if __name__ == "__main__":
    for fn in sys.argv[1:]:
        update_queue(fn)
