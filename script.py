
import os

def create_project_structure(base_path, structure):
    """Create project directory structure and files."""
    for name, contents in structure.items():
        current_path = os.path.join(base_path, name)
        
        if contents is None:
            # Create empty file if it doesn't exist
            if not os.path.exists(current_path):
                open(current_path, 'w').close()
                print(f"File created: {current_path}")
            else:
                print(f"File already exists: {current_path}")
        elif isinstance(contents, dict):
            # Create directory and recurse
            os.makedirs(current_path, exist_ok=True)
            print(f"Directory created: {current_path}")
            create_project_structure(current_path, contents)

# Project configuration
BASE_PATH = "/home/dci-student/Projects/InventoryManagemntSystem"
PROJECT_STRUCTURE = {
    "InventoryManagementSystem": {
        "__init__.py": None,
        "asgi.py": None,
        "settings.py": None
    },
    "inventory": {
        "__init__.py": None,
        "admin.py": None,
        "apps.py": None,
        "forms.py": None,
        "models.py": None,
        "tests.py": None,
    },
    "tests": {
        "__init__.py": None,
        "test_inventory_manager.py": None,
    },
    "LICENSE": None,
    "README.md": None,
    "requirements.txt": None,
    "manage.py": None,
}

# Create project structure
create_project_structure(BASE_PATH, PROJECT_STRUCTURE)

# Add requirements
requirements = """
stripe==5.1.0
Pillow==9.3.0
"""
with open(os.path.join(BASE_PATH, "requirements.txt"), 'w') as req_file:
    req_file.write(requirements)

print("Project structure created successfully!")
