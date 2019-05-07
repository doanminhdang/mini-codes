if [ "$#" -ne 4 ]; then
    echo "This command needs 4 parameters: input_video_name start:time stop:time output_video_name"
    else ffmpeg -i $1 -ss $2 -to $3 -c:v copy -c:a copy $4
fi
#ffmpeg -i input.mp4 -ss 01:10:27 -to 02:18:51 -c:v copy -c:a copy output.mp4
