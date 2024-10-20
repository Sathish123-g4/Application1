# Placeholder functions for rule engine
def create_rule(rule_string):
    """Creates a rule (just returns the string here as a placeholder)."""
    return rule_string

def combine_rules(rules):
    """Combines multiple rules into one rule using AND logic."""
    return f"({') AND ('.join(rules)})"  # Combine rules with AND logic

def evaluate_rule(rule, data):
    """Evaluates the rule against the provided data. Simplified for demonstration."""
    age = data.get("age")
    department = data.get("department")
    salary = data.get("salary")
    experience = data.get("experience")
    
    # Simplified evaluation logic based on the example rule structure
    # This is hardcoded and assumes the structure of the rule you're working with
    return (age > 30 and department == "Sales" and (salary > 50000 or experience > 5)) or \
           (age < 25 and department == "Marketing" and (salary > 50000 or experience > 5)) or \
           (age > 30 and department == "Marketing" and (salary > 20000 or experience > 5))

# Placeholder functions for in-memory data storage
rules_store = {}

def store_rule(rule_id, rule):
    """Stores a rule in an in-memory dictionary."""
    rules_store[rule_id] = rule

def load_rule(rule_id):
    """Loads a rule from the in-memory dictionary."""
    return rules_store.get(rule_id)

# Main function to define, store, and evaluate rules
def main():
    # Step 1: Define the rules as strings
    rule1 = "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"
    rule2 = "((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)"
    
    # Step 2: Combine the two rules using AND logic
    combined_rule = combine_rules([rule1, rule2])
    
    # Step 3: Store the combined rule in memory
    store_rule("combined_rule", combined_rule)

    # Step 4: Define the data to evaluate against the combined rule
    data = {
        "age": 35,
        "department": "Sales",
        "salary": 60000,
        "experience": 3
    }
    
    # Step 5: Load the stored combined rule and evaluate it against the data
    rule_to_evaluate = load_rule("combined_rule")
    result = evaluate_rule(rule_to_evaluate, data)
    
    # Step 6: Output the result of the evaluation
    print(result)  # Outputs: True or False based on rule evaluation

if __name__ == "__main__":
    main()
