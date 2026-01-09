import sys
from CompilationEngine import CompilationEngine

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 JackCompiler.py inputfile.jack")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = input_file.replace(".jack", ".vm")
    CompilationEngine(input_file, output_file)
    print(f"Compiled {input_file} to {output_file}")
