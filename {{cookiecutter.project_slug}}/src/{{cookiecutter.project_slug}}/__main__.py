import sys

@app.command()
def main():
    """Console script for {{cookiecutter.project_slug}}."""
    print("Edit src/{{cookiecutter.project_slug}}/__main__.py to extend CLI.")
    return 0

if __name__ == "__main__":
    sys.exit(main)
