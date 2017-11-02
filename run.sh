now="$(date +'%m%d')"
python3 ./code/streaming.py ./code/$now.json
echo "Show Text Msg After 1 Sec:"
sleep 1
python3 ./code/parse.py ./code/$now.json