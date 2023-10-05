import yaml

def generate_markdown(documentation):
    markdown = []
    
    for item in documentation:
        section = item['section']
        content = item['content']
        
        markdown.append(f"## {section}\n")
        
        if isinstance(content, list):
            for line in content:
                markdown.append(f"- {line}\n")
        elif isinstance(content, dict):
            for key, value in content.items():
                markdown.append(f"### {key}\n")
                for line in value:
                    markdown.append(f"- {line}\n")
    
    return "\n".join(markdown)

if __name__ == "__main__":
    with open("documentation.yaml", "r") as yaml_file:
        documentation_data = yaml.safe_load(yaml_file)
    
    markdown_documentation = generate_markdown(documentation_data)
    
    with open("generated_documentation.md", "w") as md_file:
        md_file.write(markdown_documentation)
