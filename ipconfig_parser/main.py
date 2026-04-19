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
        last_key = ""
        has_config = True
        for line in data.splitlines():
            if "adapter" in line:
                has_config = False
                if len(adapter) != 0:
                    file_json["adapters"].append(adapter)
                    adapter = {}
                adapter["adapter_name"] = line.split(":")[0]
            elif not line.isspace():
                if ":" in line and line.split(":", 1)[1].strip() != "":
                    last_key = line.split(".")[0].strip().lower().replace(" ", "_")
                    line_data = line.split(":", 1)[1].strip()
                    if has_config:
                        if "config" not in file_json.keys():
                            file_json["config"] = {last_key: line_data}
                        else:
                            file_json["config"].update({last_key: line_data})
                    else:
                        adapter[last_key] = line_data  
                elif len(adapter) != 0 and last_key != "" and ":" not in line and line.strip() != "":
                    if type(adapter[last_key]) == list:
                        adapter[last_key].append(line.strip())
                    else:
                        adapter[last_key] = [adapter[last_key], line.strip()]
        if len(adapter) != 0:
            file_json["adapters"].append(adapter)
        
        contents.append(file_json)
    print(json.dumps(contents, indent=2))



if __name__ == "__main__":
    main()
