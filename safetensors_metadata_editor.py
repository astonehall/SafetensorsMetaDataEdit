#!/usr/bin/env python3
import argparse
from safetensors import safe_open
from safetensors.torch import save_file

def read_metadata(filename):
    with safe_open(filename, framework="pt", device="cpu") as f:
        metadata = f.metadata()
    return metadata

def rewrite_with_metadata(infile, outfile, new_metadata):
    tensors = {}
    with safe_open(infile, framework="pt", device="cpu") as f:
        for k in f.keys():
            tensors[k] = f.get_tensor(k)
    save_file(tensors, outfile, metadata=new_metadata)

def main():
    parser = argparse.ArgumentParser(description="Read or edit safetensors metadata")
    parser.add_argument("file", help="Input .safetensors file")
    parser.add_argument("--out", help="Output file (if editing). Default: overwrite input")
    parser.add_argument("--set", action="append", default=[], metavar="KEY=VALUE",
                        help="Set metadata key=value (can be repeated)")
    parser.add_argument("--delete", action="append", default=[], metavar="KEY",
                        help="Delete metadata key (can be repeated)")
    parser.add_argument("--print", action="store_true", help="Print metadata and exit")

    args = parser.parse_args()

    infile = args.file
    outfile = args.out or infile

    metadata = read_metadata(infile)

    if args.print and not args.set and not args.delete:
        print("Metadata:")
        if metadata:
            for k, v in metadata.items():
                print(f"  {k}: {v}")
        else:
            print("  (no metadata found)")
        return

    # Apply edits
    new_metadata = dict(metadata)
    for kv in args.set:
        try:
            k, v = kv.split("=", 1)
        except ValueError:
            print(f"Invalid format for --set: {kv}, must be KEY=VALUE")
            return
        new_metadata[k] = v
    for k in args.delete:
        new_metadata.pop(k, None)

    rewrite_with_metadata(infile, outfile, new_metadata)
    print(f"Metadata updated and saved to {outfile}")

if __name__ == "__main__":
    main()

