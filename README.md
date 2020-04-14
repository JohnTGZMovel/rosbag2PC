#Required Dependencies

1. Open3D [Documention](https://github.com/intel-isl/Open3D)
..* pip install open3d
2. joblib to enable python multi-threading
..* pip install joblib

#Workflow

1. Extract depth and rgb images from rosbag
..* put rosbags into dataset/datasetX (where X is an arbitrary number)
..* change subscriber topics in grabrgb.py and grabdepth.py depending on camera
..* depth array needs to be in the units of millimeters, bag data from intelrealsense is already in these units, no normalization required
..* sh truedepthandrgb.sh

2. Make sure the number of frames in dataset/datasetX/color matches dataset/datasetX/depth, there might be an additional frame or 2 due to the sampling discrepancy, in that case, delete the extra frames

3. Set camera intrinsics and put in dataset/datasetX/_____.json

5. Modify the following parameters on config file located in config/config1/_____.json
..* "path_dataset": (path of dataset) eg. "../../dataset/datasetX"
..* "path_intrinsic" : (path of camera intrinsics) eg. "../../dataset/datasetX/_____.json"
..* "voxel_size":
..* "icp_method": "color", "
..* "global_registration": "ransac",

6. Run reconstruction on depth and rgb images
..* python run_system.py config/configX/intelrs_d400.json --make --register --refine --integrate
..* [--make](http://www.open3d.org/docs/release/tutorial/ReconstructionSystem/make_fragments.html): Make fragments from rgbd images
..* [--register](http://www.open3d.org/docs/release/tutorial/ReconstructionSystem/register_fragments.html): Register Fragments
..* [--refine](http://www.open3d.org/docs/release/tutorial/ReconstructionSystem/refine_registration.html): Refine registration
..* [--integrate](http://www.open3d.org/docs/release/tutorial/ReconstructionSystem/integrate_scene.html): Integrate scene into a single TSDF volume and extract a mesh model for the scene

7. Point clouds are automatically saved in dataset/datasetX/scene as integrated.ply
..* The point clouds can be visualized with open3D using: open3d.io.read_triangle_mesh("folder_path/integrated.ply")

#Workflow (w/o annotation)
Assuming:
..* rosbag is placed in the correct location
..* subscriber topics in grabrgb.py and grabdepth.py are set properly
..* paths are set properly in config files
..* camera instrinsics are defined

sh truedepthandrgb.sh
python run_system.py config/configX/intelrs_d400.json --make --register --refine --integrate


#File Directory Structure

(repo root)
├── config
|   └── config1
|       └── intelrs_d400.json       //Camera intrinsics 
└── dataset
    └── dataset1
        ├── rosbag.bag              //Place ROSbag here
        ├── d400_intrinsics.json    //Camera Intrinsics
        ├── color                   //RGB Images
        │   ├── 000000.jpg
        │   ├── :
        └── depth                   //Depth Images
            ├── 000000.png
            ├── :
# rosbag2PC
# rosbag2PC
