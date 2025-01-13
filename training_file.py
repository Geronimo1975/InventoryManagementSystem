import argparse

def generate_report(name):
    return f"Report generated for {name}"

def main():
    parser = argparse.ArgumentParser(description="Prompt Interface Example")
    parser.add_argument("--name", type=str, help="Enter your name", required=True)
    
    args = parser.parse_args()
    print(generate_report(args.name))

if __name__ == "__main__":
    main()