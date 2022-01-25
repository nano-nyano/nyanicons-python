import os
from typing import List

import svgutils.transform
from svgutils.transform import SVGFigure


class AvatarComponentCategory:
    def __init__(self, component_dir: str):
        self._component_dir: str = os.fsdecode(component_dir)
        self._components: List[SVGFigure] = self._load_components(self._component_dir)

    @staticmethod
    def _load_components(component_dir: str) -> List[SVGFigure]:
        components: List[SVGFigure] = []

        file_names: str
        txt_file_paths = [os.path.join(component_dir, f)
                          for f in os.listdir(component_dir)
                          if f.lower().endswith('.svg')]
        for file_path in txt_file_paths:
            svg: SVGFigure = svgutils.transform.fromfile(file_path)
            components.append(svg)

        return components

    @property
    def component_dir(self) -> str:
        return self._component_dir

    @property
    def components(self) -> List[SVGFigure]:
        return self._components
