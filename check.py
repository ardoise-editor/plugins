"""Checks registry.json: what the editor would refuse must not be listed."""
import json
import re
import sys

ID = re.compile(r"^ardoise(\.[a-z0-9][a-z0-9-]*)+$")
# The organization is Ardoise Editor's now. The entries keep its former name
# (ardoise-editor): the versions of the editor from before the rename only
# list repositories under it, and GitHub sends them to the new name.
REPO = re.compile(r"^ardoise-editor/[A-Za-z0-9._-]+$")

with open(sys.argv[1] if len(sys.argv) > 1 else "registry.json", encoding="utf-8") as f:
    registry = json.load(f)
errors = []
if registry.get("version") != 1:
    errors.append("version must be 1")
seen = set()
for i, plugin in enumerate(registry.get("plugins", [])):
    where = f"plugins[{i}]"
    pid = plugin.get("id", "")
    if not ID.match(pid) or len(pid) > 64:
        errors.append(f"{where}: id {pid!r} must be ardoise.<name>")
    if pid in seen:
        errors.append(f"{where}: id {pid!r} is listed twice")
    seen.add(pid)
    if not REPO.match(plugin.get("repository", "")):
        errors.append(f"{where}: repository must be ardoise-editor/<name>")
    name = plugin.get("name")
    if not (isinstance(name, str) and name.strip()) and not (
        isinstance(name, dict) and name.get("en", "").strip()
    ):
        errors.append(f"{where}: name must be a text, or have an \"en\" text")
for e in errors:
    print(e)
sys.exit(1 if errors else 0)
