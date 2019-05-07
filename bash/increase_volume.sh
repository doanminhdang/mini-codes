if [ "$#" -ne 2 ]; then
    echo "This command needs 2 parameters: input_video_name output_video_name"
else
    ffmpeg -i $1 -vcodec copy -af "volume=20dB" $2
fi
