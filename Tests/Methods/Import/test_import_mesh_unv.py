# -*- coding: utf-8 -*-

# TODO: debug mesh with mix of elements (not handled in pyuff)

import pytest

from pyleecan.Classes.ImportMeshMat import ImportMeshMat
from pyleecan.Classes.MeshSolution import MeshSolution

list_param = [
    {
        "path": "Tests\Data\Mesh\mesh_test_quad_consecutive.unv",
        "n_points": 8,
        "element_types": ["quad"],
        "n_elements": [6],
    },
    {
        "path": "Tests\Data\Mesh\mesh_test_quad.unv",
        "n_points": 8,
        "element_types": ["quad"],
        "n_elements": [6],
    },
    {
        "path": "Tests\Data\Mesh\mesh_test_tri.unv",
        "n_points": 4,
        "element_types": ["triangle"],
        "n_elements": [4],
    },
    # {
    #     "path": 'Tests\Data\Mesh\mesh_test_mixte.unv',
    #     "n_points": 5,
    #     "element_types": ['triangle','quad'],
    #     "n_elements": [3, 1],
    # },
]


@pytest.mark.mesh  # to skip or run only mesh related tests
@pytest.mark.parametrize(
    "unv_file",
    list_param,
)
@pytest.mark.mesh  # to skip or run only mesh related tests
def test_import_mesh_unv(unv_file):
    """ Check that .unv file are correctly imported"""

    test_obj = ImportMeshMat(
        file_path=unv_file["path"],
    )
    mesh = test_obj.get_data()

    # assert points.shape[0] == unv_file["n_points"]
    # for elt_type, n_elt in zip(unv_file["element_types"], unv_file["n_elements"]):
    #     assert elements[elt_type].shape[0] == n_elt

    meshsol = MeshSolution()
    meshsol.mesh = [mesh]
    meshsol.plot_mesh(save_path='D:/test.png', is_show_fig=False)

if __name__ == "__main__":
    for param in list_param:
        test_import_mesh_unv(param)