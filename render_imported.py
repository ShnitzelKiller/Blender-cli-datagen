# blender --background --python render_imported.py -- blender-cli-rendering/output/test 100 256

import bpy
import sys
import math
import os
import random
from typing import List, Tuple

working_dir_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(working_dir_path)

import utils


def get_output_file_path() -> str:
    return bpy.path.relpath(str(sys.argv[sys.argv.index('--') + 1]))


def get_resolution_percentage() -> int:
    return int(sys.argv[sys.argv.index('--') + 2])


def get_num_samples() -> int:
    return int(sys.argv[sys.argv.index('--') + 3])


if __name__ == "__main__":
    # Args
    output_file_path = get_output_file_path()
    resolution_percentage = get_resolution_percentage()
    num_samples = get_num_samples()

    # Setting
    scene = bpy.context.scene
    camera_object = bpy.data.objects["Camera"]
    utils.set_cycles_renderer(scene, camera_object, num_samples)

    # utils.clean_objects()

    for i in range(3):
        stl_path = os.path.abspath(os.path.join("assets/meshes", f"0{i+1}.stl"))
        print(stl_path)
        bpy.ops.import_mesh.stl(filepath=stl_path)
        utils.set_output_properties(scene, resolution_percentage, output_file_path + str(i))
        bpy.ops.render.render(write_still=True)
