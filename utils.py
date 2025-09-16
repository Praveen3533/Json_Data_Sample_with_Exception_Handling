import os
import pandas as pd
import json

def load_data(path_list):
    dfs = []
    prefix_path = "Json_data"
    for file_path in path_list:
        full_path = os.path.join(prefix_path, file_path)
        try:
            with open(full_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            df = pd.json_normalize(data)
            dfs.append(df)
        except FileNotFoundError:
            print(f"[FileNotFoundError] File not found! path: {full_path}")
        except Exception as e:
            print(f"[Error] Failed to load {file_path}: {e}")
    
    if dfs:
        return pd.concat(dfs, ignore_index=True)
    else:
        print("[Warning] No valid DataFrames to concatenate.")
        return pd.DataFrame()

def add_cols(df):
    """Add string length columns with exception handling"""
    try:
        df["name_length"] = df["user.name"].astype(str).str.len()
        df["department_length"] = df["user.department"].astype(str).str.len()
        df["email_length"] = df["user.email"].astype(str).str.len()
        return df
    except Exception as e:
        print(f"[Error] Failed to add columns: {e}")
        return df


