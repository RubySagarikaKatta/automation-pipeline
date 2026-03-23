from modules.cleaner import clean_data
from modules.validator import validate_data

def run_pipeline():
    file_path = "data/input.csv"
    
    data = clean_data(file_path)
    validated_data = validate_data(data)
    
    print("Pipeline executed successfully")

if __name__ == "__main__":
    run_pipeline()