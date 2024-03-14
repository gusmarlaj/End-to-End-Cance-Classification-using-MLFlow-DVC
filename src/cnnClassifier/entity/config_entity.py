#entity that will be paste in config_entity.py
from dataclasses import dataclass
from pathlib import Path

#connected with confige.yaml
#data class is called entity
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path