import requests

def translate_text(text, target_lang="en"):
    url = "https://translate.googleapis.com/translate_a/single"
    params = {"client":"gtx","sl":"auto","tl":target_lang,"dt":"t","q":text}
    try:
        res = requests.get(url, params=params, timeout=10)
        res.raise_for_status()
        return res.json()[0][0][0]
    except Exception as e:
        print(f"Translation error: {e}")
        return "⚠️ অনুবাদ করতে ব্যর্থ।"
