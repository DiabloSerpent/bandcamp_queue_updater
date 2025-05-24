import sys
import json


def update_queue(fn):
    with open(fn, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
    
    for song in data["queue"]["p"]:
        # Missing field
        song["is_visible_in_public_playlist"] = True

        # This used to just be "PLAYLIST"
        song["track_type"] = "OWNED_PLAYLIST"

        # This field was removed
        del song["playlist_id"]

    with open(fn, "w", encoding="utf-8") as json_file:
        # Add "indent=2" to see prettier output.
        # This doesn't change the ability of bandcamp to use the file.
        json.dump(data, json_file, separators=(',', ':'), ensure_ascii=False)


if __name__ == "__main__":
    for fn in sys.argv[1:]:
        update_queue(fn)
