import pymongo
import json
from bson import ObjectId

# MongoDB setup
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["rule_engine"]
rules_collection = db["rules"]

# Define a Node class for AST
class Node:
    def __init__(self, node_type, value=None):
        self.type = node_type
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node(type={self.type}, value={self.value})"

# Function to store the rule and its AST in the database
def store_rule(rule_string, ast_node):
    """Stores a rule and its AST in the database."""
    ast_json = json.dumps(ast_node, default=lambda o: o.__dict__)  # Serialize AST
    rules_collection.insert_one({"rule_string": rule_string, "ast_json": ast_json})

# Function to load the rule and its AST from the database
def load_rule(rule_id):
    """Loads a rule and its AST from the database."""
    rule_data = rules_collection.find_one({"_id": ObjectId(rule_id)})
    if rule_data:
        ast_dict = json.loads(rule_data["ast_json"])
        return build_ast_from_dict(ast_dict)
    return None

# Recursively build AST from dictionary
def build_ast_from_dict(ast_dict):
    """Recursively builds an AST from a dictionary."""
    node = Node(ast_dict["type"], value=ast_dict.get("value"))
    if "left" in ast_dict:
        node.left = build_ast_from_dict(ast_dict["left"])
    if "right" in ast_dict:
        node.right = build_ast_from_dict(ast_dict["right"])
    return node

# Example usage:
if __name__ == "__main__":
    # Step 1: Create an example AST for a rule
    root = Node("AND")
    root.left = Node("age", value="> 30")
    root.right = Node("department", value="Sales")
    
    # Step 2: Store the rule and its AST in MongoDB
    store_rule("age > 30 AND department = 'Sales'", root)

    # Step 3: Load the rule from MongoDB
    # Replace this with an actual ObjectId from your MongoDB after inserting the rule
    rule_id = "put_valid_object_id_here"  # Replace with actual MongoDB ObjectId string

    loaded_rule = load_rule(rule_id)
    
    # Step 4: Print the loaded rule's AST
    print(loaded_rule)
