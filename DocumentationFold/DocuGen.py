import yaml

def generate_documentation(data):
    documentation = []

    for item in data:
        section_name = item['section']
        section_content = item['content']

        if section_name and section_content:
            documentation.append(f"## {section_name}\n")
            if isinstance(section_content, list):
                for content in section_content:
                    if isinstance(content, dict):
                        for key, value in content.items():
                            documentation.append(f"### {key}\n")
                            for subitem in value:
                                documentation.append(f"- {subitem}\n")
                    else:
                        documentation.append(f"- {content}\n")
            else:
                documentation.append(f"- {section_content}\n")

    return '\n'.join(documentation)

if __name__ == '__main__':
    with open("documentation.yaml", 'r') as yaml_file:
        data = yaml.safe_load(yaml_file)

    documentation_text = generate_documentation(data)

    with open('generated_documentation.md', 'w') as output_file:
        output_file.write(documentation_text)
