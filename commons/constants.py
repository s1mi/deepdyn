# Bilateral Filter Constants
BILATERAL_KERNEL_SIZE = 41
BILATERAL_SIGMA_COLOR = 20
BILATERAL_SIGMA_SPACE = 20

# Gabor filter Constants
GABOR_KERNEL_SIZE1 = 31
GABOR_KERNEL_GAMMA1 = 0.7
GABOR_KERNEL_LAMBDA1 = 5
GABOR_KERNEL_SIGMA1 = 2

GABOR_KERNEL_SIZE2 = 31
GABOR_KERNEL_GAMMA2 = 0.7
GABOR_KERNEL_LAMBDA2 = 8
GABOR_KERNEL_SIGMA2 = 3

GABOR_KERNEL_SIZE3 = 31
GABOR_KERNEL_GAMMA3 = 0.7
GABOR_KERNEL_LAMBDA3 = 11
GABOR_KERNEL_SIGMA3 = 4

GABOR_KERNEL_NUM_OF_ORIENTATIONS = 64
GABOR_KERNEL_PSI = 0

SKELETONIZE_THRESHOLD = 20

# Image lattice constants
IMG_LATTICE_EIGHT_CONNECTED = False
IMG_LATTICE_COST_ASSIGNMENT_ALPHA = 5

IMG_LATTICE_COST_ORIGINAL_IMAGE_CONTRIBUTION = 0.4
IMG_LATTICE_COST_GABOR_IMAGE_CONTRIBUTION = 0.6

# MST algorithm parameters
GRAPH_WEIGHT_METRICS = 'cost'
SEGMENTATION_THRESHOLD = 7.5