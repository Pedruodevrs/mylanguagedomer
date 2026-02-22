import sys
import os

def run():
    file = sys.argv[1] if len(sys.argv) > 1 else "script.dom"
    if not os.path.exists(file):
        return

    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            l = line.strip()
            if not l or l.startswith("#"): continue
            
            if l.startswith("falar"):
                try:
                    print(l.split('"')[1])
                except:
                    pass
            elif l.startswith("calcular"):
                try:
                    print(eval(l.replace("calcular", "").strip()))
                except:
                    pass

if __name__ == "__main__":
    run()
    
