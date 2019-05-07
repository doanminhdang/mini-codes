if [ "$#" -ne 2 ]; then
    echo "This command needs 2 parameters: list_of_videos_in_order.txt output_video_name"
    else ffmpeg -f concat -i $1 -c copy $2
fi
#ffmpeg -f concat -i joinlist.txt -c copy video_out.mp4
#Ref: https://stackoverflow.com/questions/7333232/how-to-concatenate-two-mp4-files-using-ffmpeg
