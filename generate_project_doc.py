import os
import ast

class ProjectScanner:
    def __init__(self, project_root):
        self.project_root = project_root
        self.documentation = ""
        self.exclude_dirs = {"env", "venv", "__pycache__"}

    def scan_directory(self):
        self.documentation += "## Project Structure\n\n```plaintext\n"
        for root, dirs, files in os.walk(self.project_root):
            dirs[:] = [d for d in dirs if d not in self.exclude_dirs]
            level = root.replace(self.project_root, "").count(os.sep)
            indent = " " * 4 * level
            self.documentation += f"{indent}{os.path.basename(root)}/\n"
            sub_indent = " " * 4 * (level + 1)
            for file in files:
                if file.endswith(".py"):
                    self.documentation += f"{sub_indent}{file}\n"
        self.documentation += "```\n\n"

    def extract_classes_and_functions(self, file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            tree = ast.parse(f.read())
        classes = [node for node in tree.body if isinstance(node, ast.ClassDef)]
        functions = [node for node in tree.body if isinstance(node, ast.FunctionDef)]
        return classes, functions

    def generate_doc(self):
        self.documentation = "# Inventory Management System Documentation\n\n"
        self.documentation += "## Table of Contents\n"
        self.documentation += "1. [Project Overview](#project-overview)\n"
        self.documentation += "2. [Key Components](#key-components)\n"
        self.documentation += "3. [Project Structure](#project-structure)\n"
        self.documentation += "4. [Setup and Installation](#setup-and-installation)\n"
        self.documentation += "5. [Usage Guide](#usage-guide)\n"
        self.documentation += "6. [Technical Details](#technical-details)\n"
        self.documentation += "7. [Future Enhancements](#future-enhancements)\n\n"
        
        self.documentation += "## Project Overview\n\n"
        self.documentation += "The Inventory Management System is designed for efficient product tracking and business operations management.\n\n"
        
        self.documentation += "## Key Components\n\n"
        for root, _, files in os.walk(self.project_root):
            if any(excl in root for excl in self.exclude_dirs):
                continue
            for file in files:
                if file.endswith(".py"):
                    file_path = os.path.join(root, file)
                    relative_path = os.path.relpath(file_path, self.project_root)
                    
                    self.documentation += f"### {relative_path}\n\n"
                    classes, functions = self.extract_classes_and_functions(file_path)
                    
                    for cls in classes:
                        self.documentation += f"#### Class: `{cls.name}`\n\n"
                        self.documentation += f"{ast.get_docstring(cls) or 'No description available'}\n\n"
                        for method in cls.body:
                            if isinstance(method, ast.FunctionDef):
                                self.documentation += f"- Method `{method.name}()`\n"
                                self.documentation += f"  - {ast.get_docstring(method) or 'No description available'}\n"

                    for func in functions:
                        self.documentation += f"#### Function: `{func.name}()`\n\n"
                        self.documentation += f"{ast.get_docstring(func) or 'No description available'}\n\n"
        
        self.scan_directory()
        
        self.documentation += "## Setup and Installation\n\n"
        self.documentation += "### Prerequisites\n\n"
        self.documentation += "- Python 3.11 or higher\n"
        self.documentation += "- PostgreSQL database\n\n"
        self.documentation += "### Installation Steps\n\n"
        self.documentation += "1. Clone the repository\n"
        self.documentation += "2. Install dependencies:\n"
        self.documentation += "```bash\npip install -r requirements.txt\n```\n\n"
        self.documentation += "3. Set up the database:\n"
        self.documentation += "```bash\npython init_db.py\n```\n\n"
        self.documentation += "## Usage Guide\n\n"
        self.documentation += "Run the application:\n"
        self.documentation += "```bash\npython -m streamlit run streamlit_app.py\n```\n\n"
        self.documentation += "Access the app at `http://localhost:8501`\n\n"
        self.documentation += "## Technical Details\n\n"
        self.documentation += "- Uses PostgreSQL for data persistence\n"
        self.documentation += "- Integrates RESTful APIs for external product synchronization\n"
        self.documentation += "- Implements role-based access control\n\n"
        self.documentation += "## Future Enhancements\n\n"
        self.documentation += "- Add analytics dashboard\n"
        self.documentation += "- Implement real-time alerts\n"
        self.documentation += "- Enhance caching for performance\n\n"
        
        with open(os.path.join(self.project_root, "PROJECT_DOCUMENTATION.md"), "w", encoding="utf-8") as f:
            f.write(self.documentation)
        print("📄 Documentation generated: PROJECT_DOCUMENTATION.md")

if __name__ == "__main__":
    project_root = os.path.dirname(os.path.abspath(__file__))
    scanner = ProjectScanner(project_root)
    scanner.generate_doc()