import os, pickle, subprocess

if os.path.exists('/content/drive/MyDrive/arialist.pkl'):
  with open('/content/drive/MyDrive/arialist.pkl', 'rb') as f:
      arialines = pickle.load(f)

if arialines:
  for line in arialines:
    if not '4x-UltraSharp.pth' in line:
      ariaexecline = line[2:].replace('\\n",', '').replace('/content/drive/MyDrive/stable-diffusion-webui', '/content/drive/MyDrive/volatile-concentration-localux')
      try:
        subprocess.run(ariaexecline, shell=True, check=True)
      except Exception as e:
          print("Exception: " + str(e))