with open("c:/Users/MWANGI/Documents/Python Scripts/Data analysis/streamlit/about.py", "rb") as f:
    content = f.read()
    if b"\x00" in content:
        print("Null byte found!")
    else:
        print("No null byte found.")
