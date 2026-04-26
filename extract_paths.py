import re

def extract_paths(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract src="..." or src='...'
    src_matches = re.findall(r'src=["\'](.*?)["\']', content, re.IGNORECASE)
    # Extract url(...)
    url_matches = re.findall(r'url\([\'"]?(.*?)[\'"]?\)', content, re.IGNORECASE)
    # Extract poster="..." or poster='...'
    poster_matches = re.findall(r'poster=["\'](.*?)["\']', content, re.IGNORECASE)
    
    with open('paths_utf8.txt', 'w', encoding='utf-8') as out:
        out.write("--- SRC PATHS ---\n")
        for path in src_matches:
            out.write(path + "\n")
        
        out.write("\n--- URL PATHS ---\n")
        for path in url_matches:
            out.write(path + "\n")

        out.write("\n--- POSTER PATHS ---\n")
        for path in poster_matches:
            out.write(path + "\n")

if __name__ == "__main__":
    extract_paths('INDEX.HTML')

