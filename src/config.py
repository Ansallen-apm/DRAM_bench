import json
import os

def load_config(filepath):
    """
    Loads timing configuration from a JSON file.
    從 JSON 檔案讀取時序設定。
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Config file not found: {filepath}")
    with open(filepath, 'r') as f:
        return json.load(f)

def load_mapping(filepath):
    """
    Loads address mapping from a JSON file.
    從 JSON 檔案讀取位址映射規則。
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Mapping file not found: {filepath}")
    with open(filepath, 'r') as f:
        data = json.load(f)

    # Normalize mapping to list of lists format: [[msb, lsb]]
    # 將映射規則統一為列表格式：[[msb, lsb]]
    # If user provided [msb, lsb], convert to [[msb, lsb]]
    # 如果使用者僅提供單一區段 [msb, lsb]，則轉換為 [[msb, lsb]]
    normalized = {}
    for key, value in data.items():
        if isinstance(value[0], int):
            normalized[key] = [value]
        else:
            normalized[key] = value
    return normalized
