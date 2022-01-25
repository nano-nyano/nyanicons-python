import os
from typing import List


class TxtAvatarComponentCategory:
    def __init__(self, component_dir: str):
        self._component_dir: str = os.fsdecode(component_dir)
        self._components: List[str] = self._load_components(self._component_dir)

    @staticmethod
    def _load_components(component_dir: str) -> List[str]:
        paths = [os.path.join(component_dir, p) for p in os.listdir(component_dir)]
        txt_file_paths = [p for p in paths if os.path.isfile(p) and p.endswith('.txt')]

        components: List[str] = []
        for file_path in txt_file_paths:
            with open(file_path) as file:
                file_data = file.readline()  # single line for testing with txt files
                components.append(file_data)

        return components

    @property
    def component_dir(self) -> str:
        return self._component_dir

    @property
    def components(self) -> List[str]:
        return self._components
