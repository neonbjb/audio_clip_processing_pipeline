# Audio clips processing pipeline

## Overview

This repo contains a listing of scripts I have used to process a bulk dataset consisting of large primarily-speech files
(for example, audiobooks or podcasts) and turn them into a dataset of utterances, each 2-15 seconds in length with a 
paired text annotation generated from my speech recognition model. Along the way, the dataset is cleaned up of clips
that are unsuitable because they:

- Have multiple voices talking at the same time
- Have music playing in the background
- Have environmental noise

I also generate a masking file which allows you to remove dataset elements which appear to have had their frequency
data clipped below 16kHz, which removes clips from substandard sources such as poor recordings or recordings of phone
calls, for example.

All audio outputted is at 22050Hz. The output format is currently .wav, which is currently necessary for efficient
processing in Python, though I am working on support for a [faster MP3 decoder](https://github.com/neonbjb/pyfastmp3decoder).

Note that this pipeline has been split up into many steps, but it is almost certainly more efficient to combine these
steps. The reason for this is that these steps were built one-at-a-time by me and I never expended the effort to 
combine them. If you do so and find success, I urge you to open a PR.

## Usage

### Quick tips

Most of these scripts will take a **long** time to execute with a sufficiently large number of files. Most scripts have
two undocumented flags which should help you deal with the processing time incurred:

`num_workers` Specifies the number of processes spawned to concurrently handle your files.

`resume` Allows you to pick a script back up from where it failed. Iteration count is printed out as the script executes
and is often found in the output files as well.

### Step 1 - Gather data

I'll leave this step undocumented for now. You need to download a large number of audio clips. Might I recommend
crawling podcasts, for example? I may upload some of the script I used to gather a large number of clips in the future
and will link it here.

### Step 2 - Split on silence

This step attempts to find 2-15 second clips from every \[*.mp3, *.ogg, *.wav\] file in the specified input directory.

```shell
python split_on_silence.py --path <input_directory> --out <where_clips_should_be_stored>
```

### Step 3 - Produce filter files using clip classifier model

<TODO>

### Step 4 - Use the filter generated above to separate clips into classification directories

### Step 5 - Remove folders with 1 or less files

### Note - you're pretty much done here.

At this point, you have a functional dataset for many tasks that need an unsupervised voice dataset. The following
steps are optional depending on your use-cases.

### *(Optional)* Step 6 - Create a filter file for audio clips that are missing high-frequency data

This step generates an exclusion list for audio files that are suspected to contain <= 16kHz data. This filters out
things like substandard recordings or recordings of phone calls and may be useful if you are after a model that learns
to produce hi-fidelity speech.

```shell
python filter_clips_with_no_hifreq_data.py --path <input_directory> --glob *.wav --out <filter_file.txt>
```

### *(Optional)* Step 7 - Encode everything as an MP3

This dramatically compresses your dataset, by up to a factor of 10x. The cost of SSDs to hold my data was becoming
unpalatable after hitting the 20M clips mark.

```shell
python convert_to_mp3.py --path <input_directory> --glob *.wav --out <output_directory>
```

Note: This step takes a particularly long time.