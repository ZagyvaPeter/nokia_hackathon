from pathlib import Path
import json


def main():
    contents = []
    for path in sorted(Path(".").glob("*.txt")):
        data = Path(path).read_text(encoding="utf-16")
        file_json = {
            "file_name": path.name,
            "adapters": []
            }
        adapter = {}
        for line in data.splitlines():
            if "adapter" in line:
                if len(adapter) != 0:
                    file_json["adapters"].append(adapter)
                    adapter = {}
                adapter["adapter_name"] = line.split(":")[0]
            elif not line.isspace() and ":" in line and line.split(":", 1)[1].strip() != "":
                adapter[line.split(".")[0].strip().lower().replace(" ", "_")] = line.split(":", 1)[1].strip()
        contents.append(file_json)
    

        print(json.dumps(file_json, indent=2))



if __name__ == "__main__":
    main()
