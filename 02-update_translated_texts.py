import json
import os

def update_json_value(text, type_key):
    if type_key == 'minecraft:custom_name':
        if isinstance(text, str) and text.startswith('"') and text.endswith('"'):
            return text
        return f'"{text}"'
    return text

def update_json_file(file_path, type_key, original, translation):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    def process_dict(d):
        updated = False
        for k, v in d.items():
            if k == type_key and str(v).strip('"') == original:
                d[k] = update_json_value(translation, type_key)
                updated = True
            elif isinstance(v, dict):
                if process_dict(v):
                    updated = True
            elif isinstance(v, list):
                for item in v:
                    if isinstance(item, dict):
                        if process_dict(item):
                            updated = True
        return updated

    if process_dict(data):
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            # print(f"Updated {file_path}")
            # print(f"Type: {type_key}")
            # print(f"Original: {original}")
            # print(f"Translation: {translation}")
            # print("-" * 50) # Uncomment if you need.
        return True
    return False

def main():
    translations_file = 'translations.csv'
    if not os.path.exists(translations_file):
        print(f"Error: {translations_file} not found")
        return

    import csv
    with open(translations_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        translations = list(reader)

    total_items = len(translations)
    items_with_translation = sum(1 for item in translations if item['Translation'])
    updated_count = 0
    skipped_count = 0

    print(f"\nTotal items in CSV: {total_items}")
    print(f"Items with translation: {items_with_translation}")
    print(f"Items without translation: {total_items - items_with_translation}")
    print("-" * 50)

    for item in translations:
        if not item['Translation']:
            continue
            
        source_file = item['Source']
        if not os.path.exists(source_file):
            print(f"Warning: Source file not found: {source_file}")
            skipped_count += 1
            continue

        if update_json_file(
            source_file,
            item['Type'],
            item['Original'],
            item['Translation']
        ):
            updated_count += 1

    print("\nUpdate Summary:")
    print(f"Successfully updated: {updated_count} items")
    print(f"Skipped (file not found): {skipped_count} items")
    print(f"Remaining untranslated: {total_items - items_with_translation} items")
    print("\nUpdate complete!")

if __name__ == '__main__':
    main()