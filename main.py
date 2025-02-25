import subprocess
import argparse

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Open a Jupyter Notebook with a specified filename.")
    parser.add_argument("notebook", help="The name of the Jupyter Notebook file to open (e.g., chapter_2.ipynb)")

    args = parser.parse_args()

    # Open the specified Jupyter Notebook
    subprocess.run(["jupyter", "notebook", args.notebook])


if __name__ == "__main__":
    main()
