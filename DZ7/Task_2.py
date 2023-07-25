import os

def rename_files(newname, digits, originalextension, targetextension, range, path='.'):
    count = 1
    for filename in os.listdir(path):
        if filename.endswith(originalextension):
            originalfilename = os.path.splitext(filename)[0]
            origfilenamesubstr = originalfilename[range[0]:range[1]] if range else ""
            newfilename = f"{origfilenamesubstr}{newname}{str(count).zfill(digits)}{targetextension}"
            os.rename(os.path.join(path, filename), os.path.join(path, newfilename))
            count += 1

rename_files('replaced', 6, '.dll', '.txt', [1, 6], './temp')