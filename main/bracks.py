import re


# Define a function to process the custom syntax
def process_custom_syntax(input_text, context={}):

    # Split input into tokens
    tokens = input_text.split()  

    # Initialize output
    output = ""

    # Loop through tokens
    for token in tokens:

        # Check if placeholder
        if token.startswith("{{") and token.endswith("}}"):
            key = token[2:-2]  
        if key in context:
            output += context[key]
        else:
            output += token
    else:
        output += token
        # Add space after token  
        output += " "
# Remove trailing space    
    return output.strip()


# Example usage
custom_syntax = "This is a {{key1}} example {{key2}} with some {{key3}}."
context = {
  "key1": "custom",
  "key2": "text", 
  "key3": "placeholders"
}

result = process_custom_syntax(custom_syntax, context)
print(result)


class BracksRenderer:
    def __init__(self, template, variables=None):
        """
        Initializes the Bracks renderer with the template and optional variables.

        :param template: The Bracks template string
        :param variables: Dictionary of variables to be used in rendering the template
        """
        self.template = template
        self.variables = variables or {}

    def render(self):
        """
        Renders the Bracks template with the given variables.

        :return: The rendered template
        """
        return self._render_template()

    def _render_template(self):
        """
        Renders the Bracks template with the given variables.

        :return: The rendered template
        """
        rendered = self.template
        for key, value in self.variables.items():
            rendered = rendered.replace("[[" + key + "]]", value)

        rendered = self._extract_and_evaluate(rendered)

        return rendered

    def _extract_and_evaluate(self, template):
        """
        Extracts and evaluates Bracks expressions in the given template.

        :param template: The Bracks template string
        :return: The template with expressions evaluated
        """
        pos = 0
        while pos < len(template):
            match = re.match(r"\[\[(.*?)\]\]", template[pos:])
            if match:
                expression = match.group(1)
                evaluated = self._evaluate_expression(expression)
                template = template.replace(match.group(0), evaluated, 1)  # Replace only once
                pos += len(evaluated)
            else:
                pos += 1

        return template

    def _evaluate_expression(self, expression):
        """
        Evaluates the given Bracks expression.

        :param expression: The Bracks expression
        :return: The evaluated expression result as a string
        """
        # TODO: Implement expression evaluation logic here
        return expression  # For now, just return the expression


# Example usage
template_string = "Hello, [[name]]! Your age is [[age]]."
variables = {"name": "Alice", "age": "30"}
bracks_renderer = BracksRenderer(template_string, variables)
rendered_output = bracks_renderer.render()
print(rendered_output)  # Output: "Hello, Alice! Your age is 30."


def _process_key(self, content):
    # Implement key rule processing
    # Example:
    pattern = r'key{{(.*?)}}'
    matches = re.findall(pattern, content)
    for match in matches:
        # Replace with actual content based on match
        replacement = self.variables.get(match, '')
        content = content.replace(f'key{{{match}}}', replacement)
    return content


def _process_tilde(self, content):
    # Implement tilde rule processing
    # Example:
    pattern = r'~{{(.*?)}}'
    matches = re.findall(pattern, content)
    for match in matches:
        # Replace with approximate value
        value = self.variables.get(match)
        if value is not None:
            approximate_value = len(value)  # For simplicity, assuming it's a string
            content = content.replace(f'~{{{match}}}', str(approximate_value))
    return content


def render(self):
    # Renders the Bracks template with the given variables.
    rendered = self.template
    for key, value in self.variables.items():
        rendered = rendered.replace("[[" + key + "]]", value)

    rendered = self._extract_and_evaluate(rendered)
    rendered = self._process_key(rendered)
    rendered = self._process_tilde(rendered)

    return rendered

"""
// Variables 
{{key}} // Placeholder
${key} // Declared

// Modifiers
~ {{key}} // Approximate
+ {{key}} // Concatenate
= {{key}} // Exact match 
! {{key}} // Exclude
- {{key}} // Subtract
* {{key}} // Repeat
>, <, <=, >= {{key}} // Comparisons

// Conditionals  
? {{key1}} : {{key2}} // If key1 then key2

// Keywords
ANY, ALWAYS, NEVER, WITH, AND, ONLY, NOT, UNIQUE

// Functions
between({{key1}}, {{key2}}) // Range
random({{key1}}, ...) // Random
mixed({{key1}}, ...) // Combination
contains({{key}}) // Must contain  
optimize({{key}}) // Optimize
limit({{key}}, {{value}}) // Limit

// Function Arguments
fn(-{{key}}) // Remove 
fn(*{{key}}) // Repeat
fn(?{{key1}}:{{key2}}) // Conditional

// Comments 
// This is a comment

// Includes
include({{filename}})
  
// Math
{{key1}} + {{key2}}  
{{key1}} - {{key2}}
{{key1}} * {{key2}}
{{key1}} / {{key2}}

// Nesting
{{outerKey {{innerKey}}}}

// Default values
${key=defaultValue}

// Data types  
${key=123} // Number
${flag=true} // Boolean
${text="Hello"} // String

// Object properties  
{{person.name}}  
{{person.age}}

// JSON import
import_json({{filename}})

// Looping
for {{i}} in {{array}} {
  // loop body 
}
"""


