from pathlib import Path
import json


def main():
    contents = []
    try:
        for path in sorted(Path(".").glob("*.txt")):
            data = Path(path).read_text(encoding="utf-16")
            file_json = {
                "file_name": path.name,
                "adapters": []
                }
            adapter = {}
            last_key = ""
            has_header = True
            for line in data.splitlines():
                if "adapter" in line:
                    has_header = False
                    if len(adapter) != 0:
                        file_json["adapters"].append(adapter)
                        adapter = {}
                    adapter["adapter_name"] = line.split(":")[0]
                elif line.strip() != "":
                    if ": " in line:
                        last_key = line.split(".")[0].strip().lower().replace(" ", "_")
                        line_data = line.split(":", 1)[1].strip()
                        if has_header:
                            if "header" not in file_json.keys():
                                file_json["header"] = {last_key: line_data}
                            else:
                                file_json["header"].update({last_key: line_data})
                        else:
                            adapter[last_key] = line_data  
                    elif last_key != "":
                        if type(adapter[last_key]) == list:
                            adapter[last_key].append(line.strip())
                        else:
                            adapter[last_key] = [adapter[last_key], line.strip()]
            if len(adapter) != 0:
                file_json["adapters"].append(adapter)
            
            contents.append(file_json)
        print(json.dumps(contents, indent=2, ensure_ascii=False))
        with open("output.json", "w", encoding="utf-8") as f:
            json.dump(contents, f, indent=2, ensure_ascii=False)
    except:
        print("Hiba!")

if __name__ == "__main__":
    main()
