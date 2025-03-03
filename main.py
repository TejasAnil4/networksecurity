

from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig
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
        print(data_ingestion_artifact)

    except Exception as e:
        raise NetworkSecurityException(
            error_message="Error occurred in main.py",
            error_details=str(e)
        )