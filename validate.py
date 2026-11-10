import datetime as dt
import json
import re
from pathlib import Path

catalog = json.loads(Path(__file__).with_name("codes.json").read_text())
assert catalog["schema_version"] == 1
dt.datetime.fromisoformat(catalog["updated_at"].replace("Z", "+00:00"))
assert isinstance(catalog["offers"], list)

seen = set()
for offer in catalog["offers"]:
    assert offer["service"] in {"uberRide", "uberEats", "waymo"}
    assert offer["source"] == "dots_app"
    assert re.fullmatch(r"[A-Z0-9-]{4,24}", offer["code"])
    assert isinstance(offer["source_title"], str) and offer["source_title"]
    assert offer.get("source_url") is None or offer["source_url"].startswith("https://")
    observed = dt.datetime.fromisoformat(offer["observed_at"].replace("Z", "+00:00"))
    expires = offer.get("expires_at")
    if expires:
        assert dt.datetime.fromisoformat(expires.replace("Z", "+00:00")) > observed
    assert isinstance(offer.get("eligibility", ""), str)
    identity = (offer["service"], offer["code"])
    assert identity not in seen, f"duplicate {identity}"
    seen.add(identity)

print(f"validated {len(catalog['offers'])} offers")
