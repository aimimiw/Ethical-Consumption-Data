import subprocess

def call_vard(jar_file, setup_folder, threshold, f_score, input_dir, search_subfolders, output_dir,use_normalization_cache):
  """
  description: runs the VARD spelling normalization tool through the command line.

  Note: all inputs should be strings. logical inputs should not be capitalized (e.g. true instead of True)

  inputs: jar_file - the folder containing 'clui.jar'
          setup_folder - the folder containing VARD setup and spell checking docs
          threshold - normalization threshold
          f_score - indicates a balance between precision and recall. Use integers (e.g. 1,2,...,5) or fractions (1,1/2,...,1/5)
          input_dir - folder containing the texts to be normalized
          search_subfolders - whether or not to search subfolders in the input directory
          output_dir - folder to output normalized texts
          use_normalization_cache: whether or not to use the normalization cache
  output: provides a folder containing normalized texts in the same format as the input           files.
  """

  subprocess.call([
    'java',
    '-Xms256M',
    '-Xmx512M',
    '-jar',
    str(jar_file),
    str(setup_folder),
    str(threshold),
    str(f_score),
    str(input_dir),
    str(search_subfolders),
    str(output_dir),
    str(use_normalization_cache)
  ])