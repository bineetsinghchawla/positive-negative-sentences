import os
import requests


def load_env():
    if os.path.exists(".env"):
        with open(".env", "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def classify(text: str) -> dict:
    key = os.getenv("MLFK_API_KEY")
    if not key:
        raise ValueError("Missing MLFK_API_KEY. Create a .env file (see README).")

    url = f"https://machinelearningforkids.co.uk/api/scratch/{key}/classify"
    r = requests.get(url, params={"data": text}, timeout=15)
    r.raise_for_status()
    return r.json()[0]


if __name__ == "__main__":
    load_env()
    text = input("Enter text: ").strip()
    result = classify(text)
    print(f'{result["class_name"]} ({result["confidence"]:.2f})')
