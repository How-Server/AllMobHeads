import os
import json
import csv

#-----------------------------------
# all = '.' 
# versions-16-44 = 'versions-16-44'
# versions-33-44 = 'versions-33-44'
# versions-45- = 'versions-45-'

base_path = '.'
#-----------------------------------
def extract_json_value(text):
    if isinstance(text, str):
        text = text.strip('"')
        if text.startswith('"') and text.endswith('"'):
            text = text[1:-1]
    return str(text)

def process_json_file(file_path):
    translation_items = []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    def process_dict(d):
        for k, v in d.items():
            if k in ['title', 'description', 'minecraft:custom_name']:
                item = {
                    'Type': k,
                    'Source': file_path,
                    'Original': extract_json_value(v),
                    'Translation': ''
                }
                translation_items.append(item)
                # print(f"Found translation item:")
                # print(f"Type: {item['Type']}")
                # print(f"Source: {item['Source']}")
                # print(f"Original: {item['Original']}")
                # print("-" * 50) # Uncomment if you need.
            elif isinstance(v, dict):
                process_dict(v)
            elif isinstance(v, list):
                for item in v:
                    if isinstance(item, dict):
                        process_dict(item)
                        
    process_dict(data)
    return translation_items

def main():
    all_translations = []
    
    print("\nStarting JSON files search...")
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                # print(f"\nProcessing file: {file_path}") # Uncomment if you need.
                translations = process_json_file(file_path)
                all_translations.extend(translations)
    
    with open('translations.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['Type', 'Source', 'Original', 'Translation'])
        writer.writeheader()
        writer.writerows(all_translations)
    
    print(f"\nComplete! Found {len(all_translations)} items to translate")
    print(f"Results saved to translations.csv")

if __name__ == '__main__':
    main()