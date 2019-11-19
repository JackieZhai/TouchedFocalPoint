# https://github.com/seung-lab/kimimaro

import numpy as np
import kimimaro
import pickle
from PIL import Image

labels = np.load('./origin.npy')
# labels = all_labels[0:50, 0:600, 0:1200]
# del all_labels
print(labels.shape)

skels = kimimaro.skeletonize(
  labels, 
  # teasar_params={
  #   'scale': 4,
  #   'const': 500, # physical units
  #   'pdrf_exponent': 4,
  #   'pdrf_scale': 100000,
  #   'soma_detection_threshold': 1100, # physical units
  #   'soma_acceptance_threshold': 3500, # physical units
  #   'soma_invalidation_scale': 1.0,
  #   'soma_invalidation_const': 300, # physical units
  #   'max_paths': 50, # default None
  # },
  object_ids=[84293, 86245, 22308], # process only the specified labels
  # extra_targets_before=[ (27,33,100), (44,45,46) ], # target points in voxels
  # extra_targets_after=[ (27,33,100), (44,45,46) ], # target points in voxels
  dust_threshold=82944, # skip connected components with fewer than this many voxels
  anisotropy=(30,3,3), # default True
  fix_branching=True, # default True
  fix_borders=True, # default True
  progress=True, # default False, show progress bar
  parallel=12, # <= 0 all cpu, 1 single process, 2+ multiprocess
  parallel_chunk_size=100, # how many skeletons to process before updating progress bar
)
# print(skels[48])
# print(skels[48].vertices)

skels_vertices = {}
skels_edges = {}
skels_radius = {}
for key in skels.keys():
  skels_vertices[key] = skels[key].vertices
  skels_edges[key] = skels[key].edges
  skels_radius[key] = skels[key].radius

f = open('skel_ans_extra.pkl', 'wb')
pickle.dump([skels_vertices, skels_edges, skels_radius], f)
f.close()

# LISTING 2: Combining skeletons produced from 
#            adjacent or overlapping images.

# import kimimaro
# from cloudvolume import PrecomputedSkeleton

# skels = ... # a set of skeletons produced from the same label id
# skel = PrecomputedSkeleton.simple_merge(skels).consolidate()
# skel = kimimaro.postprocess(
#   skel, 
#   dust_threshold=1000, # physical units
#   tick_threshold=3500 # physical units
# )

# # Split input skeletons into connected components and
# # then join the two nearest vertices within `radius` distance
# # of each other until there is only a single connected component
# # or no pairs of points nearer than `radius` exist. 
# # Fuse all remaining components into a single skeleton.
# skel = kimimaro.join_close_components([skel1, skel2], radius=1500) # 1500 units threshold
# skel = kimimaro.join_close_components([skel1, skel2], radius=None) # no threshold
