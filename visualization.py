import nibabel
import os
import matplotlib.pyplot as plt
from skimage import io

print(os.path.join('brats/Task02_Heart/imagesTr/la_003.nii.gz'))
struct = nibabel.load(os.path.join('./brats/Task02_Heart/imagesTr/la_003.nii.gz'))

struct_arr = struct.get_data()
print(struct_arr)
plt.figure()
plt.imshow(struct_arr[110], aspect=0.5)

#struct_arr = io.imread('./brats/Task02_Heart/imagesTr/la_003.nii.gz')
plt.show()
