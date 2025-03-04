from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig, DataValidationConfig
import sys

if __name__ == '__main__':
    try:
        # Step 1: Create TrainingPipelineConfig object
        training_pipeline_config = TrainingPipelineConfig()

        # Step 2: Create DataIngestionConfig object
        data_ingestion_config = DataIngestionConfig(training_pipeline_config)

        # Step 3: Initialize DataIngestion
        data_ingestion = DataIngestion(data_ingestion_config)

        # Step 4: Initiate data ingestion
        logging.info("Initiate Data Ingestion")
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
        logging.info("Data Ingestion Completed")
        print(data_ingestion_artifact)

        # Step 5: Initialize DataValidation
        data_validation_config = DataValidationConfig(training_pipeline_config)
        data_validation = DataValidation(data_ingestion_artifact, data_validation_config)

        # Step 6: Initiate data validation
        logging.info("Initiate data validation")
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info("Data validation completed")
        print(data_validation_artifact)

    except Exception as e:
        raise NetworkSecurityException(
            error_message="Error occurred in main.py",
            error_details=e  # Pass the exception object
        )