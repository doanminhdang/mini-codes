#!/bin/sh                                                                                                                                                     
# This code converts all files in M4V format (video H264, audio mp4a) to MP4
# Corrected from https://wiki.videolan.org/VLC_HowTo/Transcode_multiple_videos/
# https://wiki.videolan.org/Codec/
######################## Transcode the files using ... ########################
vcodec="h264"
acodec="mp4a"
vb="1024"
ab="128"
mux="mp4"
###############################################################################
set -x

# Store path to VLC in $vlc
if command -pv vlc >/dev/null 2>&1; then
    # Linux should find "vlc" when searching PATH
    vlc="vlc"
else
    # macOS seems to need an alias
    vlc="/Applications/Utilities/VLC.app/Contents/MacOS/VLC"
fi
# Sanity check
if ! command -pv "$vlc" >/dev/null 2>&1; then
    printf '%s\n' "Cannot find path to VLC. Abort." >&2
    exit 1
fi
 
for filename in *; do
    printf '%s\n' "=> Transcoding '$filename'... "
    mainname="${filename%.*}"
    "$vlc" -I dummy -q "$filename" \
       --sout=#transcode{vcodec="$vcodec",vb="$vb",acodec="$acodec",ab="$ab"}:standard{mux="$mux",dst="$mainname.mp4",access=file} \
       vlc://quit
    ls -lh "$filename" "$mainname.mp4"
    printf '\n'
done
