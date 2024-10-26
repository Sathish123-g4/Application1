# Application1
Rule Engine Demo
A simple, in-memory rule engine written in Python that allows the creation, storage, combination, and evaluation of rules against data inputs. This rule engine is ideal for scenarios that involve applying business rules or logical conditions to data.

Features
Rule Creation: Define rules as strings for specific conditions (e.g., age, department).
Rule Combination: Combine multiple rules using AND logic to form more complex rules.
Rule Storage: Store and retrieve rules in an in-memory dictionary.
Rule Evaluation: Evaluate a given rule against data inputs to produce a True or False result.
Functions Overview
create_rule(rule_string)
Creates a rule from a provided string. This function is a placeholder in the current setup and simply returns the rule string.

combine_rules(rules)
Combines multiple rules into a single rule using AND logic. The rules are joined together as (rule1) AND (rule2).

evaluate_rule(rule, data)
Evaluates a rule string against the provided data dictionary. For demonstration, this function currently evaluates hardcoded conditions involving age, department, salary, and experience.

In-Memory Storage Functions
store_rule(rule_id, rule): Stores a rule in an in-memory dictionary with a unique rule ID.
load_rule(rule_id): Retrieves a rule from memory using its rule ID.
Example Usage
In the main function, we define two sample rules, combine them, store the result, and evaluate the combined rule against sample data.

python
Copy code
# Example Rule Strings
rule1 = "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"
rule2 = "((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)"

# Combine and Store Rule
combined_rule = combine_rules([rule1, rule2])
store_rule("combined_rule", combined_rule)

# Sample Data for Evaluation
data = {
    "age": 35,
    "department": "Sales",
    "salary": 60000,
    "experience": 3
}

# Load and Evaluate Rule
rule_to_evaluate = load_rule("combined_rule")
result = evaluate_rule(rule_to_evaluate, data)

print(result)  # Outputs: True or False based on rule evaluation
Running the Demo
To run this example, ensure you have Python 3 installed, then execute:

bash
Copy code
python your_script_name.py
License
This project is open-source and can be modified as needed.

This README.md provides an overview of the rule engine’s functionality, sample usage, and setup instructions. Feel free to expand it based on further developments or requirements.
