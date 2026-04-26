import base64

def embed_logo():
    try:
        with open('images/homy-logo.webp', 'rb') as f:
            logo_data = f.read()
        b64 = base64.b64encode(logo_data).decode()
        
        with open('INDEX.HTML', 'r', encoding='utf-8') as f:
            html = f.read()
        
        target = 'src="images/homy-logo.webp"'
        replacement = f'src="data:image/webp;base64,{b64}"'
        
        new_html = html.replace(target, replacement)
        
        with open('INDEX.HTML', 'w', encoding='utf-8') as f:
            f.write(new_html)
        
        print("Logo embedded successfully.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    embed_logo()
