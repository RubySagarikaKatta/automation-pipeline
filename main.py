from modules.cleaner import clean_data
from modules.validator import validate_data
from modules.processor import calculate_rolling_avg
from modules.health import apply_health
from modules.logger import setup_logger
import logging
setup_logger()
logging.info("Pipeline started")

def run_pipeline():
    file_path = "data/input.csv"
    
    data = clean_data(file_path)
    validated_data = validate_data(data)
    
    processed_data = calculate_rolling_avg(validated_data)
    final_data = apply_health(processed_data)
    
    final_data.to_csv("data/output.csv", index=False)
    
    print("Pipeline executed successfully")
    print("Output saved to data/output.csv")

logging.info("Data cleaned")
logging.info("Data validated")
logging.info("Processing completed")
logging.info("Health classification applied")
logging.info("Pipeline completed successfully")

if __name__ == "__main__":
    run_pipeline()