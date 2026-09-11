#!/usr/bin/env python3
"""
Parse SEMrush Keyword Magic Tool HTML snapshots into a structured CSV.
Usage: python3 parse_semrush_html.py <output_csv_path> <seed_keyword_1> [seed_keyword_2 ...]
"""
import sys, re, csv, glob, os
from bs4 import BeautifulSoup

def parse_file(path, seed_label):
    with open(path, encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    rows = soup.find_all(attrs={"role": "row"})
    out = []
    for row in rows:
        cells = row.find_all(attrs={"role": "cell"})
        if len(cells) < 14: continue
        t = [c.get_text(" ", strip=True) for c in cells]
        kw = t[0]
        intent = t[2]
        vol = t[4].replace(",", "")
        kd = t[8]
        cpc = t[9]
        comp = t[10]
        sf = t[11]
        results = t[12]
        try: vol_n = int(vol) if vol.isdigit() else 0
        except: vol_n = 0
        try: kd_n = int(kd) if kd.isdigit() else None
        except: kd_n = None
        out.append({
            "seed": seed_label, "keyword": kw, "intent": intent,
            "volume": vol_n, "kd": kd_n, "cpc": cpc, "competition": comp,
            "sf": sf, "results": results
        })
    return out

def kd_tier(kd):
    if kd is None: return "N/A"
    if kd <= 14: return "Very Easy"
    if kd <= 29: return "Easy"
    if kd <= 49: return "Possible"
    if kd <= 69: return "Difficult"
    if kd <= 84: return "Hard"
    return "Very Hard"

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 parse_semrush_html.py <output_csv_path> <seed_keyword_1> [seed_keyword_2 ...]")
        sys.exit(1)
        
    out_path = sys.argv[1]
    seeds = sys.argv[2:]
    
    all_rows = []
    for seed in seeds:
        q = seed.replace(" ", "_")
        # Look for HTML files saved by browser_view in /home/ubuntu/upload/
        files = sorted(glob.glob(f"/home/ubuntu/upload/sem*keywordmagic*q_{q}_db_us_*.html"),
                       key=lambda x: -int(re.search(r'_(\d+)\.html', x).group(1)) if re.search(r'_(\d+)\.html', x) else 0)
        files = [f for f in files if 'domain_' not in f]
        if not files: 
            print(f"Warning: No HTML snapshots found for seed '{seed}' in /home/ubuntu/upload/")
            continue
        print(f"Parsing {files[0]} for seed '{seed}'...")
        rows = parse_file(files[0], seed)
        all_rows.extend(rows)

    if not all_rows:
        print("No data extracted. Exiting.")
        sys.exit(1)

    # Deduplicate by keyword (keep entry with higher volume)
    dedup = {}
    for r in all_rows:
        k = r["keyword"].lower().strip()
        if k not in dedup or r["volume"] > dedup[k]["volume"]:
            dedup[k] = r

    # Add KD tier
    for r in dedup.values():
        r["kd_tier"] = kd_tier(r["kd"])

    # Sort by KD (ascending) then Volume (descending)
    final_rows = sorted(dedup.values(), key=lambda x: (x["kd"] if x["kd"] is not None else 999, -x["volume"]))

    os.makedirs(os.path.dirname(os.path.abspath(out_path)) or '.', exist_ok=True)
    with open(out_path, "w", newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=["seed","keyword","intent","volume","kd","kd_tier","cpc","competition","sf","results"])
        w.writeheader()
        for r in final_rows: w.writerow(r)
        
    print(f"Successfully extracted {len(final_rows)} unique keywords to {out_path}")

if __name__ == "__main__":
    main()
