import subprocess
import glob
from pathlib import Path
import os

bad_path = []
for ct_path in sorted(glob.glob("data/nifti/*/CT.nii")):
    target_path = str(Path(ct_path).with_name("CT_stripped.nii"))
    target_mask_path = str(Path(ct_path).with_name("CT_stripped_mask.nii"))
    if os.path.exists(target_path) and os.path.exists(target_mask_path):
        continue

    else:
        try:
            subprocess.run(
                f"python3 synthstrip-docker -i {ct_path} -o {target_path} -m {target_mask_path} ",
                shell=True,
                universal_newlines=True,
                check=True,
            )
        except:
            bad_path.append(ct_path)
            continue
print(bad_path)
