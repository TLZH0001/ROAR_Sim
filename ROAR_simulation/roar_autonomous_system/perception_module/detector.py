from abc import ABC, abstractmethod
import logging
from ROAR_simulation.roar_autonomous_system.utilities_module.vehicle_models import (
    Vehicle,
)
from ROAR_simulation.roar_autonomous_system.utilities_module.camera_models import Camera
import numpy as np
from  typing import Any


class Detector(ABC):
    def __init__(self, vehicle: Vehicle, camera: Camera):
        self.logger = logging
        self.logger = logging.getLogger(__name__)
        self.vehicle: Vehicle = vehicle
        self.camera: Camera = camera

    @abstractmethod
    def run_step(self, vehicle: Vehicle, new_data: np.array) -> Any:
        """
        On every step, detect something from the current frame

        Args:
            vehicle: Current Vehicle State
            new_data: new data

        Returns:
            Any
        """
        self.sync_data(vehicle=vehicle, new_data=new_data)
        return None

    def sync_data(self, vehicle: Vehicle, new_data: np.ndarray) -> None:
        """
        Sync data

        Args:
            vehicle: new vehicle state
            new_data: new data

        Returns:
            None

        """
        self.vehicle = vehicle
        self.camera.data = new_data
