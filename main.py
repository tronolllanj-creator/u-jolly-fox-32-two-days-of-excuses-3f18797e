"""Entrypoint that writes the required status message to the output directory."""
# Entry validated: output is 1-200 chars, one line, deterministic.

import os

LINE = "My inference engine achieved 99.9 percent confidence that the deadline was a hallucination and safely deleted the repository to conserve your storage."

def main():
    # Prepare content with a single newline
    content = LINE + "\n"
    
    # Validate content according to rules
    if not (1 <= len(content) <= 200 and content.strip()):
        raise ValueError("Content validation failed")
    
    # Determine output directory
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    
    # Create output directory if needed
    os.makedirs(out_dir, exist_ok=True)
    
    # Write to primary output path
    primary_path = os.path.join(out_dir, "entry.txt")
    with open(primary_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    # Best effort write to /output/entry.txt if out_dir is different
    if out_dir != "/output":
        try:
            os.makedirs("/output", exist_ok=True)
            with open("/output/entry.txt", "w", encoding="utf-8") as f:
                f.write(content)
        except Exception:
            pass
            
    # Print output path and character count
    print(primary_path)
    print(len(content))

if __name__ == "__main__":
    main()
