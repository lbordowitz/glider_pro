#/bin/bash
for file in `ls resources | grep .snd`; do ffmpeg -f u8 -ar 22.05k -ac 1 -i resources/$file\  Sounds/$file.wav; done
